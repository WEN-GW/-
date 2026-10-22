# 第 7 课（实战总结）：爬取广东省 2025 年 GDP
#
# 这个文件把前 6 课全部用上了，一步都不跳。请对照着看：
#     第 1 步 = 第 1 课（网页就是一段文字）
#     第 2 步 = 第 2 课（看服务器到底回了什么）
#     第 3 步 = 第 6 课（先确认数据在不在源码里）
#     第 4 步 = 第 4 课（HTML 是树，用路径找节点）
#     第 5 步 = 第 3 课（从文字里抠数据）
#     第 6 步 = 第 5 课（循环 + 落地成文件）
#
# 数据来源：广东省统计局官网（stats.gd.gov.cn）公开发布的
#           《2025年广东地区生产总值初步核算结果》
#
# 运行：python 07_实战_广东2025年GDP.py

import sys  # 用于出错时干净地退出程序

import requests
from bs4 import BeautifulSoup

# 要抓的网址。这是省统计局的一条公开数据发布页。
URL = "https://stats.gd.gov.cn/jdgnsczz/content/post_4854890.html"

# 带上浏览器身份。不带的话，很多政府网站会直接拒绝脚本访问。
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    )
}

# 【第 5 课的规矩】动手前先看 robots.txt。
# 这个站的 robots.txt 返回 404（没有提供），按惯例视为未做限制。
# 但本项目仍然只请求 1 次、不循环、不并发 —— 慢，是爬虫的基本礼貌。


# print("=" * 62)
# print("第 1 步：把网页抓下来（第 1 课）")
# print("=" * 62)

# requests.get 去取网页。timeout=20：政府网站有时慢，多等一会。
resp = requests.get(URL, headers=HEADERS, timeout=20)

# 状态码必须先看：200 才是成功。
if resp.status_code != 200:
    print("抓取失败，状态码：", resp.status_code)
    print("可能原因：网址变了 / 服务器暂时不可用 / 被风控拦截")
    sys.exit()  # 直接结束，不要拿着错误页面继续往下解析

# 修正编码，防止中文变成乱码（政府网站常见 GBK/UTF-8 混用）
resp.encoding = resp.apparent_encoding

html = resp.text  # 这一大段文字，就是整个网页

print("状态码：", resp.status_code)
print("网页文字长度：", len(html), "个字符")

# 顺手存一份到本地。出问题时可以直接打开看，比反复请求别人服务器好。
with open("第7课-广东GDP网页.html", "w", encoding="utf-8") as f:
    f.write(html)
print("已存成 第7课-广东GDP网页.html")


print()
print("=" * 62)
print("第 2 步：看服务器的原文长什么样（第 2 课）")
print("=" * 62)

# 第 2 课教过：服务器回来的东西，前面是"说明书"，后面是正文。
# 这里我们不再手写 socket，而是直接在文字里找目标数据，看它周围是什么。
needle = "145846.76"  # 这是我们要找的 GDP 数字
pos = html.find(needle)  # find 返回它在第几个字符的位置，找不到返回 -1

print("GDP 数字出现在第", pos, "个字符的位置")

if pos == -1:
    print("没找到这个数字，页面可能改版了。请打开 第7课-广东GDP网页.html 看看。")
    sys.exit()

# 打印数字前后各 300 个字符的"上下文"。
# 这一步等价于在浏览器里按 F12 查看元素，只是用代码来做。
print()
print("--------- 数字周围的原始 HTML（重点看它被什么标签包着）---------")
print(html[pos - 300 : pos + 120])


print()
print("=" * 62)
print("第 3 步：数据在源码里吗（第 6 课）")
print("=" * 62)

# 第 6 课的核心检验：数据到底在不在服务器发来的文字里？
# 这一步能提前判断"这是静态页还是动态页"，避免白折腾。
if needle in html:
    print('"' + needle + '" 在源码里 -> 是静态页，requests 能抓到，可以继续')
else:
    print("数据不在源码里 -> 是 JavaScript 渲染的页面，需要换思路")
    sys.exit()


print()
print("=" * 62)
print("第 4 步：把文字变成树，找到那张表（第 4 课）")
print("=" * 62)

# BeautifulSoup 把一大段文字变成可以"按路径查询"的结构
soup = BeautifulSoup(html, "lxml")

# 先看页面标题，确认打开的是对的那一页（防止被跳到首页或错误页）
print("页面标题：", soup.title.get_text(strip=True))

# 上面第 2 步看到数据在 <td>（表格单元格）里，说明它在一张表格中。
# 先数一数这一页有几个表格，避免抓错。
tables = soup.select("table")
print("页面中表格数量：", len(tables))

if not tables:
    print("没找到表格，页面结构可能变了")
    sys.exit()

table = tables[0]  # 只有一张，取第一个


print()
print("=" * 62)
print("第 5 步：一行一行读表格（第 3 课）")
print("=" * 62)

# tr = table row，表格的"行"；td = table data，行里的"单元格"
rows = table.select("tr")
print("这张表一共有", len(rows), "行")

# 准备一个字典，把「指标名称」和它的两个数字存起来，方便后面按名字取。
# 形如：{"地区生产总值": (145846.76, 3.9), "第一产业": (5891.80, 4.5), ...}
data = {}

for tr in rows:

    # 找出这一行里所有的单元格
    cells = tr.select("td")

    # 逐个取文字：get_text(strip=True) 去掉前后空白。
    # 为什么要 replace("\xa0", "")？
    #   \xa0 是网页里的"不间断空格"（HTML 里写 &nbsp;），它长得像空格但不是普通空格，
    #   如果混在指标名里，就会出现"看起来叫'地区生产总值'但怎么也匹配不上"的诡异问题。
    values = [td.get_text(strip=True).replace("\xa0", "") for td in cells]

    # 只处理"正好 3 列"的行。
    # 为什么？因为表格最后一行是备注（合并了单元格，只有 1 列），
    # 直接取 values[1] 会报"下标越界"的错。
    if len(values) != 3:
        continue  # 跳过这一行，继续看下一行

    name, total_text, growth_text = values  # 三列分别是：指标名、总量、增长

    # 表头行（"指标名称/总量（亿元）/增长（%）"）也是 3 列，会被混进来。
    # 怎么区分？用"能不能转成数字"来判断：
    #   "145846.76" 能转成小数 -> 是数据
    #   "总量（亿元）" 转不了   -> 是表头，跳过
    try:
        total = float(total_text)
        growth = float(growth_text)
    except ValueError:
        continue  # 转不了数字，说明不是数据行

    # 两列都是数字，才存进字典
    data[name] = (total, growth)

print("成功解析出", len(data), "行数据")


print()
print("=" * 62)
print("第 6 步：取出要的指标，并做校验（第 3 课 + 第 5 课）")
print("=" * 62)

# 按名称取值，取不到会报 KeyError，所以先检查名字是否存在。
# 这一步也顺便验证了 replace("\xa0") 的必要性。
if "地区生产总值" not in data:
    print("没找到『地区生产总值』这一行，现有指标是：")
    print(list(data.keys()))
    sys.exit()

gdp_total, gdp_growth = data["地区生产总值"]

print("广东省 2025 年地区生产总值（GDP）：", gdp_total, "亿元")
print("比上年增长：", gdp_growth, "%")
print()
print("换算一下：", round(gdp_total / 10000, 2), "万亿元")
# round(数字, 2) = 保留 2 位小数。145846.76 亿元 ≈ 14.58 万亿元。


print()
print("--------- 三次产业 ----------")

for name in ("第一产业", "第二产业", "第三产业"):
    if name in data:  # 有这一行才打印，防止某个年份缺数据时报错
        total, growth = data[name]
        print(f"{name}：{total} 亿元，增长 {growth}%")

# 实战里最重要的一步：校验。
# 三次产业之和应该等于 GDP 总量。如果对不上，说明解析串行/漏行了。
# 这一步能救你 90% 的"数据看起来对但其实是错的"问题。
first = data["第一产业"][0]
second = data["第二产业"][0]
third = data["第三产业"][0]
total_check = first + second + third

print()
print("校验：一产 + 二产 + 三产 =", round(total_check, 2), "亿元")
print("      官方公布的 GDP 总量 =", gdp_total, "亿元")
print("      差额 =", round(total_check - gdp_total, 2), "亿元（0 表示数据一致）")


# ----------------------------------------------------------------------
# 落地成文件（第 3 课的 CSV 写法）
# ----------------------------------------------------------------------
import csv  # 放在这里导入，是为了让上面的流程读起来更连贯

with open("第7课-广东2025年GDP.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["指标名称", "总量（亿元）", "增长（%）"])  # 表头

    # 把字典里所有指标一条条写出去
    for name, (total, growth) in data.items():
        writer.writerow([name, total, growth])

print()
print("已保存：第7课-广东2025年GDP.csv（可直接用 Excel 打开）")


print()
print("=" * 62)
print("实战总结：六课是怎么拼起来的")
print("=" * 62)
print("第 1 课  拿网页      -> requests.get 把整段文字取回来")
print("第 2 课  看原文      -> 打印数字前后的 HTML，弄清它被什么标签包着")
print("第 6 课  先验证      -> '145846.76' in html，确认不是 JS 动态页")
print("第 4 课  找节点      -> soup.select('table') / select('tr') / select('td')")
print("第 3 课  取文字      -> get_text(strip=True)，清掉 &nbsp; 再转数字")
print("第 5 课  循环 + 落地 -> for 遍历每一行，写进 CSV")
print()
print("整套流程没有一行是“高级技巧”，全是这六课里的东西。")
print("换一个网站，把这六步重做一遍，就是一次新的爬虫。")
