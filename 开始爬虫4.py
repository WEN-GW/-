# 第 4 课：网页其实是一棵树
#
# 这节课讲清“选择器”到底是什么：
#   HTML 是“标签套标签”的结构，套起来就像一棵倒着的树。
#   所谓“选择器”，就是【从树根往下走的一条路径】。
#
# 运行：python 04_网页是一棵树.py

import requests
from bs4 import BeautifulSoup

html = requests.get('https://quotes.toscrape.com/', timeout=10).text
soup = BeautifulSoup(html, 'lxml')   #把文字变成树

# 第一部分：亲眼看看这棵树长什么样
# ======================================================================
# 真实的 HTML 是这样的（缩进代表“谁套在谁里面”）：
#
#   <html>
#     <body>
#       <div class="container">
#         <div class="row">
#           <div class="col-md-8">
#             <div class="quote">        <- 一条名言
#               <span class="text">...</span>
#               <small class="author">...</small>
#
# 越往右越深。想拿 span.text，就要从根一路走下来。

print("整个网页最外层标签是：", soup.html.name)      # name 就是标签名
print("它的下一层是：", soup.html.body.name)

# find_all(recursive=False) 的意思是：只看“直接子节点”，不要往下深挖。
# 这样打印出来就是树的前两层，一眼能看懂结构。

print()
print("--------- body 的直接子节点 ---------")
for child in soup.html.body.find_all(recursive=False):
    print("  <" + child.name + ">  class =", child.get("class"))
    
    # 再往下一层看看
    for grandchild in child.find_all(recursive=False):
        print("      └─ <" + grandchild.name + ">  class =", grandchild.get("class"))


# 第二部分：选择器 = 从根往下走的路径
# ======================================================================
# 下面这行字符串就是“选择器”，它描述了一条路径：
#   在 body 里面 → 找 class 含 container 的 div → 再往下找 class 含 quote 的 div
# 空格表示“里面的”，点点表示“class 叫这个名字”。

path = "body div.container div.quote"

quotes = soup.select(path)  # select 会把这条路径上所有匹配的都找出来
print()
print("用路径 '" + path + "' 找到", len(quotes), "条名言")

# 打印第一条，验证确实找到了
first = quotes[0]
print("第一条：", first.select_one("span.text").get_text(strip=True)[:40], "...")
print("作者：", first.select_one("small.author").get_text(strip=True))


# 第三部分：为什么通常只写 "div.quote" 就够了
# ======================================================================
# 因为 select 是“在整个网页里找所有符合条件的”，
# 只要 class 名够独特，写最短的那个就行，不用写全路径。
# 只有出现“同名的东西在别处也有”时，才需要写长路径来区分。

print()
print(">>> 一句话总结：HTML 是树，选择器是从根到叶的一条路。")
print(">>> 写选择器的诀窍：在浏览器 F12 里点一下元素，看它叫什么标签、什么 class，照着抄。")
