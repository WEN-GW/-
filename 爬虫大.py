# import requests

# url = 'https://www.macroview.club/region/guangdong/gdp'

# resp = requests.get('url, timeout=10)')


# print(resp.status_code)



# 第 1 课：把一个网页"拿"回来
# 文件：01_看到网页.py　｜　学完能做到：用代码把一个网页的内容取到手里，并判断成没成功。
#
# 【怎么运行】
#   1. 终端里先跑着靶场（如果没跑：python site/mock_server.py）
#   2. 在 VSCode 里打开本文件
#   3. 点右上角 ▶ 按钮，或者按 Ctrl+F5
#
# 【这一课只学一件事】
#   用 3 行代码，把网上的一个网页，变成你电脑里的一段文字。

# 第一步：发请求，获取响应对象

import requests    # 借一个"专门跑腿的人"，它叫 requests

url = 'http://127.0.0.1:8000'    # 要去的地址（这就是"网址"）

resp = requests.get(url, timeout=10)   # 去这个地址敲门，把"回应"装进名叫 resp 的盒子
                                                 # timeout=10 意思是：最多等 10 秒，别一直傻等


print(resp.status_code)   # 200 表示请求成功 404 表示请求失败 403 表示没有权限访问

print(len(resp.text))
# resp.text 就是那个网页的全部内容，也就是"网页源码"

print(resp.text[:300])
# [:300] 的意思是"只要前 300 个字"，不然屏幕会被刷满

# 看完这段，你应该知道
# requests.get(url, timeout=10) 就是「去敲门」，回应整个装进 resp。
# resp.status_code 是对方的暗号：200 可以进、404 没这东西、403 不让进。
# resp.text 是整页源码，一个超长字符串 —— 后面 9 课全都在处理它








# 第 2 课：从一大串文字里，找出一个书名
# 文件：02_找到一个书名.py　｜　学完能做到：知道某个数据在哪，就能用代码把它取出来
#
# 【动手前，先在浏览器里做一遍 —— 这一步不能跳】
#   1. 浏览器打开 http://127.0.0.1:8000/
#   2. 随便右键点一个书名 → 选「检查」
#   3. 你会看到这样一行：
#        <a class="title" href="/book/1">Python 编程从入门到实践</a>
#   4. 看懂这行字：它是一只"碗"（标签 a），碗上贴着名字（class="title"），
#      碗里装着那块肉（书名文字）
#
# 【这一课只学一件事】
#   告诉电脑：去找"名字叫 title 的那只碗，把碗里的文字端出来"


import requests
from parsel import Selector     # 再借一个人，它专门"按地址找东西"


resp = requests.get("http://127.0.0.1:8000/", timeout=10)

sel = Selector(text=resp.text)
# 上一行：把那一大串文字，变成一个"能按地址查找"的东西

name = sel.css("a.title::text").get()
# 拆开看：
#   a.title      = 找标签叫 a、名字（class）叫 title 的那只碗
#   ::text       = 我不要碗，我要碗里的文字
#   .get()       = 取第一个结果

print(name)

# 【改一改，你就懂了】把下面这句前面的 # 删掉，再运行一次
#
# print(sel.css("span.author::text").get())     # 换成找作者
# print(sel.css("span.downloads::text").get())   # 换成找下载量
# print(sel.css("h1::text").get())              # 找大标题
#
# 改完你会发现：只有 class 名字变了，其他全一样。
# 这就是"选择器"的全部秘密 —— 它只是一个地址。
####看完这段，你应该知道
# Selector(text=resp.text) 把字符串变成「能按地址查」的结构，这一步不能漏。
# a.title = 标签名 a + 点 + class 名 title；::text 表示只要文字。
# .get() 取第一个；找不到时返回 None，不报错 —— 所以写错选择器时你看到的是 None 而不是红字。




# 第 3 课：把这一页的 5 本书全抓出来
#
# 【这一课只学一件事】
#   先"找到装每一本书的盒子"，再在盒子里取书名。
#   这个"先大后小"的顺序，是爬虫最容易搞错的地方。
#
# 【回看第 2 课】上次是直接全页搜 a.title，结果只拿到了第 1 个。
#   因为 .get() 只取第一个。要拿全部，得先知道"一共有几个盒子"。
 
 
import requests
from parsel import Selector
 
resp = requests.get("http://127.0.0.1:8000/", timeout=10)
sel = Selector(text=resp.text)
 
cards = sel.css("li.book-item")
# li.book-item = 每一本书外面那个"盒子"
# 不加 .get()，拿到的是一堆盒子本身（不是一个结果）
 
print("这一页一共", len(cards), "本书")
print("-" * 30)
 
for card in cards:
    # 下面两行都在「某一个盒子内部」找，所以前面不加 sel. 而写 card.
    name = card.css("a.title::text").get()
    downloads = card.css("span.downloads::text").get()
    print(name, "|", downloads)
 
 
# ─────────────────────────────────────────────
# 【改一改，你就懂了】
#
# ① 把 card.css("span.downloads...") 里的 downloads 改成 author，看结果变了没
#
# ② 把 cards = sel.css("li.book-item") 改成 span.downloads 试试，
#    你会发现只打印出下载量、没有书名。为什么？
#    —— 因为盒子换了，盒子里当然找不到 a.title。
#    这就是新手最常遇到的问题："为什么我的结果是 None"

# 看完这段，你应该知道
# sel.css("li.book-item") 不加 .get()，拿到的是一整批盒子（可以 len() 数出几个）。
# 循环里必须写 card.css(...)，写成 sel.css(...) 的话每本书都会变成第一本。
# 结果不对时先 print(len(cards)) 数盒子，别急着改取值那一行 —— 新手 80% 的时间浪费在这。