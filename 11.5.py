# """最简版：爬一篇文章 → 生成 Word。

# 用法：改下面 URL 后运行。依赖：pip install requests parsel python-docx
# """

# from io import BytesIO
# from urllib.parse import urljoin

# import requests
# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.oxml.ns import qn
# from docx.shared import Cm, Pt, RGBColor
# from parsel import Selector

# URL = "https://paper.sciencenet.cn/sbhtmlnews/2026/8/390740.shtm?id=390740"
# OUTPUT = "最简版文章.docx"
# UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36"}


# def set_font(run, size=10.5, color=None):
#     """设置字体。中文必须写 eastAsia 属性，只设 font.name 中文仍是宋体。"""
#     run.font.name = "微软雅黑"
#     run.font.size = Pt(size)
#     if color:
#         run.font.color.rgb = RGBColor.from_string(color)
#     run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "微软雅黑")


# # ---------- 一、下载网页，取出标题 / 作者行 / 正文块 ----------
# response = requests.get(URL, headers=UA, timeout=20)
# response.encoding = response.apparent_encoding          # 自动识别编码，防中文乱码
# selector = Selector(response.text)

# cells = [" ".join(t.split()) for t in selector.css("div#content1 table td::text").getall()]
# cells = [t for t in cells if t]                          # 丢掉空格子
# subtitle = cells[0] if len(cells) > 1 else ""
# title = cells[1] if len(cells) > 1 else (cells[0] if cells else "文章")
# meta = " ".join("".join(selector.xpath('(//table[@id="content"]//div)[1]//text()').getall()).split())

# items = []
# for node in selector.css("div#content1").xpath("./p | ./div"):
#     text = " ".join("".join(node.css("::text").getall()).split())
#     image = node.css("img::attr(src)").get()
#     if image:
#         items.append(("image", urljoin(URL, image)))     # 图片是相对路径，补成完整网址
#     if text:
#         items.append(("text", text))

# # ---------- 二、排成 Word ----------
# doc = Document()
# for text, size, color in ((subtitle, 14, None), (title, 18, None), (meta, 9, "808080")):
#     if text:
#         p = doc.add_paragraph()
#         p.alignment = WD_ALIGN_PARAGRAPH.CENTER
#         set_font(p.add_run(text), size=size, color=color)

# for kind, value in items:
#     if kind == "text":
#         p = doc.add_paragraph()
#         p.paragraph_format.first_line_indent = Pt(21)    # 首行缩进两字（10.5pt × 2）
#         p.paragraph_format.line_spacing = 1.5
#         set_font(p.add_run(value))
#     else:
#         try:
#             data = requests.get(value, headers=UA, timeout=20).content
#         except requests.RequestException:
#             continue                                     # 单张图失败就跳过，不影响整体
#         p = doc.add_paragraph()
#         p.alignment = WD_ALIGN_PARAGRAPH.CENTER
#         p.add_run().add_picture(BytesIO(data), width=Cm(14))     # 图片走内存，不落盘

# doc.save(OUTPUT)
# print(f"已生成 {OUTPUT}：{len(items)} 个内容块")



