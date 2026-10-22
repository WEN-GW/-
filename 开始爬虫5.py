# 第 5 课：一页变一百页（翻页的真相）
#
# 这节课只讲一件事：
#   翻页没有魔法。第 2 页只是“换了个网址”而已。
#   你只要找到网址的变化规律，用一个循环就能抓完全部。
#
# 运行：python 05_一页变一百页.py

import time

import requests
from bs4 import BeautifulSoup

# 观察一下这两个网址：
#   第 1 页： https://quotes.toscrape.com/
#   第 2 页： https://quotes.toscrape.com/page/2/
#   第 3 页： https://quotes.toscrape.com/page/3/
#
# 规律很明显：除了第 1 页，其余都是 /page/数字/
# 所以让数字变一下，就能拿到每一页 —— 这就是翻页的底层原理。

out = open("第5课-作者名单.txt", "w", encoding="utf-8")  # 打开一个文件准备写

# range(1, 4) 会产生 1、2、3 三个数字（注意：不含 4）
for page in range(1, 4):

    # 第 1 页网址特殊，单独处理；其余按规律拼
    if page == 1:
        url = "https://quotes.toscrape.com/"
    else:
        # f"..." 是“把变量塞进字符串”的写法，{page} 会被换成真实数字
        url = f"https://quotes.toscrape.com/page/{page}/"

    html = requests.get(url, timeout=10).text          # 抓这一页的文字
    soup = BeautifulSoup(html, "lxml")                 # 变成树

    # 找出这一页所有作者名，一行一个写进文件
    for node in soup.select("small.author"):
        out.write(node.get_text(strip=True) + "\n")

    print("第", page, "页抓完了 ->", url)

    # 每抓一页停 1 秒。
    # 为什么要停？因为服务器是别人的。你一口气发几百个请求，
    # 轻则被拒绝（状态码 429），重则被封 IP。慢一点，才能长久。
    time.sleep(1)

out.close()  # 写完要关文件，否则内容可能还没真正存到硬盘
print()
print("全部完成，打开 第5课-作者名单.txt 看看")
print(">>> 一句话总结：翻页 = 改网址里的数字 + 循环。")
print(">>> 真实网站可能是 ?page=2、?p=2、或者点“下一页”拿到新网址，道理完全一样。")