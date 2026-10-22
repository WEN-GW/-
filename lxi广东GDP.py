import csv
from webbrowser import Mozilla

import requests
from bs4 import BeautifulSoup
import sys

URL = "https://stats.gd.gov.cn/jdgnsczz/content/post_4854890.html"

HEADERS = {
    "User-Agent":(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
        '(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'
    )
}



# resp = requests.get(URL, headers=HEADERS, timeout=20)

# if resp.status_code != 200:

#     print('出现错误', resp.status_code)
#     print('请检查URL是否正确','服务器不可用')
#     sys.exit()

# resp.encoding = resp.apparent_encoding

# html = resp.text

# print(resp.status_code)

# print(len(html))

# print(html[:500])

# with open('广东GDP.html', 'w', encoding='utf-8') as f:

#     f.write(html)
resp = requests.get(URL, headers=HEADERS, timeout=20)  
resp.encoding = resp.apparent_encoding               
html = resp.text                                      

print("状态码：", resp.status_code, " (200 就是成功）")
print("网页长度：", len(html), "个字符")




print("源码里有 145846.76 吗：", "145846.76" in html)

soup = BeautifulSoup(html, "lxml")

tables = soup.select_one("table")

data = {}

rows = tables.select("tr")[1:]

for tr in rows:
    cell = []
    for td in tr.select("td"):
        text = td.get_text(strip=True)
        text = text.replace("\xa0", "")
        cell.append(text)

    if len(cell) != 3:
        continue

    name, total, growth = cell

    data[name] = (float(total), float(growth))

print('解析出', len(data), '行指标')

if '地区生产总值' not in data:
    print('没有找到地区生产总值')
    print('现在的指标是：', list(data.keys()))
    exit()

gdp, gdp_growth = data["地区生产总值"]

print()
print('广东省2025年地区总值:', gdp, '亿元')
print('同比增长:', gdp_growth, '%')
print('换算一下:', round(gdp / 10000, 2), '万亿元')

print()
for name in ['第一产业', '第二产业', '第三产业']:
    total, growth = data[name]
    print(f'{name}: {total}亿元, 同比增长{growth}%')

check = data["第一产业"][0] + data["第二产业"][0] + data["第三产业"][0]

print()
print()
print("校验：一产 + 二产 + 三产 =", round(check, 2), "亿元")
print("      官方公布的 GDP    =", gdp, "亿元")
print("      差额              =", round(check - gdp, 2), "亿元(0 就是对上了）")

with open("广东GDP2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["指标名称", "总值（亿元）", "增长（%)"])
    for name, (total, growth) in data.items():
        writer.writerow([name, total, growth])

print()
print('数据已保存到广东GDP.csv')
print()
print("抓网页 = 拿文字 -> 确认数据在里面 -> 变树 -> 走路径 -> 取文字 -> 存文件。")
print("换一个网站，把这六步重做一遍，就是一次新的爬虫。")
print('注意：')
print('1. 数据来自国家统计局，可能存在误差')
print('2. 数据仅供参考，不作为投资建议')
print('3. 本程序不保证数据准确性和安全性')
print('4. 本程序不承担任何法律责任')
