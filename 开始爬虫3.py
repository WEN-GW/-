# 第 3 课：从一大段文字里，抠出你要的东西
#
# 这节课只讲一件事：
#   解析网页 = 在一段文字里“按规则找片段”。
#   任何解析库（BeautifulSoup、lxml、parsel）做的都是这件事，只是帮你少写代码。
#
# 先用最笨的办法（纯字符串）做一遍，你才会明白库到底帮你干了什么。
#
# 运行：python 03_从文字里抠数据.py


from pydoc import stripid

import requests

url = "https://quotes.toscrape.com/"
html = requests.get(url, timeout=10).text  # 拿到那一大段文字



# 第一部分：不用任何库，只用字符串的“查找”和“切片”
# ======================================================================
# 网页里每一条名言长这样（在浏览器按 F12 能看到）：
#     <span class="text" itemprop="text">“这里才是名言内容”</span>
#                                    <small class="author">作者名</small>
#
# 所以我们只要：找到开头那串标记 → 找到结束标记 → 把中间夹着的字切出来。
# 这就是“解析”的全部原理。

# find() 找“这段文字第一次出现在第几个字符的位置”，找不到返回 -1
tag_start = html.find('<span class="text"')
print("开头标记的位置：", tag_start)

# 从开头标记往后，找第一个 ">"，标签本身到这里才结束
content_start = html.find(">", tag_start)

# 再找结束标记 "</span>" 的位置
content_end = html.find("</span>", content_start)

# 切片 [a:b] 的意思是“取第 a 个字符到第 b 个字符之间”
quote = html[content_start + 1 : content_end]
print("抠出来的第一条名言：", quote)

# 用同样的套路抠作者
author_start = html.find('<small class="author"')
author_gt = html.find(">", author_start)
author_end = html.find("</small>", author_gt)
author = html[author_gt + 1 : author_end]
print("抠出来的作者：", author)



# 第二部分：同样的事，用 BeautifulSoup 只要两行
# ======================================================================
# 那为什么还要用库？因为真实网页里：
#   - 标签可能换行、属性顺序会变
#   - 有的没写 itemprop
#   - 大小写、空格不统一
# 用 find 一遍遍找，网页一改版你的代码就全废。
# BeautifulSoup 会先把 HTML 变成“结构”，让你按“标签名 + class”去找，不用管排版细节。

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")  # 把文字变成可以“查询”的结构
first = soup.select_one("div.quote")  # 找第一个 class 叫 quote 的 div

print()
print("BeautifulSoup 抠出来的名言：", first.select_one("span.text").get_text(strip=True))
print("BeautifulSoup 抠出来的作者：", first.select_one("small.author").get_text(strip=True))

# get_text(strip=True) 的意思是：只要标签里面的文字，并且去掉首尾空格。

print()
print(">>> 一句话总结：解析 = 按规则在文字里找片段。")
print(">>> 库不是魔法，它只是把“找标签”这件事变得不用你亲手算位置。")