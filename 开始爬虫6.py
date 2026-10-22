# 第 6 课：为什么有的网页，怎么抓都是空的？
#
# 这是新手最大的困惑，也是爬虫最核心的一个原理：
#   requests 拿到的，是服务器【一开始】发来的那份 HTML。
#   而浏览器还会继续执行网页里的 JavaScript，把内容“填”进页面。
#   那个“填”的过程，requests 完全不参与 —— 所以它看到的页面是空的。
#
# 本课用两个页面做对比，用事实说话。
#
# 运行：python 06_为什么有的网页抓不到.py

import requests

# 这两个网站内容一模一样，但一个“内容写在源码里”，一个“内容靠 JS 填”
static_url = "https://quotes.toscrape.com/"      # 静态页：内容直接在源码里
dynamic_url = "https://quotes.toscrape.com/js/"  # 动态页：内容由 JavaScript 生成

static_html = requests.get(static_url, timeout=10).text
dynamic_html = requests.get(dynamic_url, timeout=10).text

print("静态页源码长度：", len(static_html))
print("动态页源码长度：", len(dynamic_html))

# ======================================================================
# 关键实验：直接在自己拿到的文字里，搜“Einstein”这个名字
# ======================================================================
# in 是“在不在里面”的判断，返回 True / False。
# 这一步能直接证明：数据到底有没有在服务器发来的文字里。

print()
print("静态页源码里有 Einstein 吗？", "Einstein" in static_html)
print("动态页源码里有 Einstein 吗？", "Einstein" in dynamic_html)

print()
print("结论：")
print("  静态页 = 数据本来就写在 HTML 里，requests 一抓就有。")
print("  动态页 = HTML 只是个空壳，数据是浏览器执行 JS 之后才补上去的。")
print("           requests 不执行 JS，所以它看到的永远是那个空壳。")


# ======================================================================
# 那怎么办？先别急着上工具，先看有没有“更省事的路”
# ======================================================================
print()
print("--------- 正确的排查顺序 ---------")
print("第 1 步：在浏览器按 F12 → 打开 Network（网络）→ 选 Fetch/XHR → 刷新页面")
print("        看有没有一个请求，返回的是干净的 JSON 数据。")
print("        如果有，直接 requests.get(那个地址)，比什么都快、都稳。")
print()
print("第 2 步：如果没有独立接口，才需要“真的开一个浏览器”去跑 JS。")
print("        Python 里的 Playwright 就是干这个的：它能开一个看不见的 Chrome，")
print("        等 JS 跑完，再把渲染好的网页交给你。")
print()
print("第 3 步：如果连浏览器都拿不到（比如要登录、要验证码），")
print("        那基本说明对方不希望你抓。到这一步就该停手，而不是硬闯。")

print()
print(">>> 一句话总结：requests 只拿“第一手 HTML”，不执行 JS。")
print(">>> 抓不到内容时，先找接口（JSON），再考虑开浏览器。")