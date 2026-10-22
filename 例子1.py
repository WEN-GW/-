# ======================== 配置区：只改这两行 ========================
URL = "https://paper.sciencenet.cn/sbhtmlnews/2026/8/390740.shtm?id=390740"
OUTPUT = "我的文章.docx"
# ==================================================================
IMAGE_DIR = Path("文章图片")      # 正文图片会下载到这个文件夹

# 带上浏览器身份：不带的话有些网站会直接拒绝（返回 403）
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Referer": "https://paper.sciencenet.cn/",
}


def set_font(run, size=10.5, bold=False, color=None):
    """设置字体。

    run 是 Word 里的一段文字。为什么不能只写 run.font.name：
    那样只有英文会变字体，中文仍然是宋体——中文必须额外写 eastAsia 属性。
    """
    run.font.name = "微软雅黑"
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "微软雅黑")


# ============ 第 1 步：把网页下载下来 ============
print("正在下载网页……")
resp = requests.get(URL, headers=HEADERS, timeout=20)
resp.raise_for_status()                     # 网址打不开（404、403）时这里直接报错，不会静默失败
resp.encoding = resp.apparent_encoding      # 自动识别网页编码，防止中文乱码
html = resp.text
print(f"下载完成，共 {len(html)} 个字符")

# ============ 第 2 步：把内容从 HTML 里挖出来 ============
selector = Selector(html)

# 标题：科学网把标题放在 div#content1 里的表格单元格中，前两个非空的是副标题和主标题
cells = [" ".join(text.split()) for text in selector.css("div#content1 table td::text").getall()]
cells = [text for text in cells if text]          # 去掉空格子
subtitle = cells[0] if len(cells) > 1 else ""
title = cells[1] if len(cells) > 1 else (cells[0] if cells else "未命名文章")

# 作者行：形如「作者：刘思嘉 张婧瑶 来源：中国科学报 发布时间：2026-8-4」
meta = " ".join(
    "".join(selector.xpath('(//table[@id="content"]//div)[1]//text()').getall()).split()
)

# 正文：按先后顺序收集段落文字和图片地址
# items 里每个元素都是 ("text", 文字) 或 ("image", 图片地址)
items = []
for node in selector.css("div#content1").xpath("./p | ./div"):
    text = " ".join("".join(node.css("::text").getall()).split())
    img_src = node.css("img::attr(src)").get()     # 这个段落里有图片吗
    if img_src:
        items.append(("image", urljoin(URL, img_src)))   # 图片是相对路径，要补成完整网址
    if text:
        items.append(("text", text))

print(f"解析完成：{title}")
print(f"  作者信息：{meta}")
print(f"  正文共 {len(items)} 个内容块")

# ============ 第 3 步：把图片下载到本地 ============
IMAGE_DIR.mkdir(exist_ok=True)             # 文件夹不存在就创建
saved_images = {}                          # {第几个块: 本地图片路径}
for index, (kind, value) in enumerate(items):
    if kind != "image":
        continue
    try:
        img_resp = requests.get(value, headers=HEADERS, timeout=20)
        img_resp.raise_for_status()
        suffix = Path(value.split("?")[0]).suffix or ".jpg"
        path = IMAGE_DIR / f"图{index:02d}{suffix}"
        path.write_bytes(img_resp.content)
        saved_images[index] = path
        print(f"  图片已保存：{path.name}（{len(img_resp.content) // 1024} KB）")
    except requests.RequestException as error:
        # 单张图片失败不该让整个程序崩掉，跳过就行
        print(f"  图片没下下来，跳过：{error}")

# ============ 第 4 步：生成 Word ============
doc = Document()

if subtitle:                                # 副标题（有的文章没有）
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(p.add_run(subtitle), size=14, bold=True)

p = doc.add_paragraph()                     # 主标题
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_font(p.add_run(title), size=18, bold=True)

p = doc.add_paragraph()                     # 作者、来源、发布时间
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_font(p.add_run(meta), size=9, color="808080")

for index, (kind, value) in enumerate(items):
    if kind == "text":
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Pt(21)   # 首行缩进两个字
        p.paragraph_format.line_spacing = 1.5           # 1.5 倍行距，读起来舒服
        set_font(p.add_run(value))
    elif index in saved_images:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(saved_images[index]), width=Cm(14))

doc.save(OUTPUT)
print(f"\n完成！Word 已保存到：{Path(OUTPUT).resolve()}")