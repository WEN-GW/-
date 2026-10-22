import csv
import requests
import json
import time
from bs4 import BeautifulSoup

URL = 'https://stats.gd.gov.cn/jdgnsczz/content/post_4792532.html'

HEADERS = {
    'User-Agent':(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
        '(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36)')
}

resp = requests.get(URL, headers=HEADERS, timeout=10)
resp.encoding = resp.apparent_encoding
html = resp.text

print('resp.status_code')
print(len(html))





print('源码里面有105176.98吗：', '105176.98' in html)





soup = BeautifulSoup(html, 'lxml')
table = soup.select_one('table')
print('页面标题：', soup.title.get_text(strip=True))
print('表格行数：', len(table.select('tr')))





data = {}
rows = table.select('tr')[1:]

for tr in rows:
    cells = []
    for td in tr.select('td'):
        text = td.get_text(strip=True)
        text = text.replace('\xa0', '')
        cells.append(text)

    if len(cells) != 3:
        continue

    name, total, growth = cells

    data[name] = (float(total), float(growth))

print('解析出', len(data), '行指标')





if '地区生产总值' not in data:
    print('地区生产总值没有找到')
    print('现在有的指标：', list(data.keys()))
    exit()

gdp, gdp_growth = data['地区生产总值']

print()
print('广东省2025年前三季度地区生产总值:', gdp, '亿元')
print('增长:', gdp_growth, '%')
print('换算一下：', round(gdp / 10000, 2), '万亿元')

print()
for name in ('第一产业', '第二产业', '第三产业'):
    total, growth = data[name]
    print(f'{name}: {total}亿元, 增长: {growth}%')

check = data['第一产业'][0] - data['第二产业'][0] - data['第三产业'][0]

print()
print("校验：一产 + 二产 + 三产 =", round(check, 2), "亿元")
print("      官方公布的 GDP    =", gdp, "亿元")
print("      差额              =", round(check - gdp, 2), "亿元(0 就是对上了）")



with open("2025年前三季度.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["指标名称", "总量（亿元）", "增长（%)"])  # 表头

    for name, (total, growth) in data.items():   # 一条条写出去
        writer.writerow([name, total, growth])

print()
print("已保存:2025年前三季度.csv(Excel 可直接打开）")