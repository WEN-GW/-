import csv
import time


import requests

from bs4 import BeautifulSoup

URL = 'https://stats.gd.gov.cn/gmjjzyzb/content/post_4932845.html'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

resp = requests.get(URL, headers=HEADERS, timeout=10)  # 发请求，最多等待10秒
resp.encoding = resp.apparent_encoding   #修中文乱码

html = resp.text

print(resp.status_code)  #状态码
print(len(html))  #长度


print('源码里面有72281.05吗：', '72281.05' in html)    #判断源码里面是否有72281.05


soup = BeautifulSoup(html, 'lxml')    # lxml解析器 解析html   固
table = soup.select_one('table')
print('页面标题：', soup.title.get_text(strip=True))
print('表格行数：', len(table.select('tr')))


data: list[Any] = {}
rows = table.select('tr')[1:]
for tr in rows:
    cols: list[Any] = []
    for td in tr.select('td'):
        text: str = td.get_text(strip=True)
        text: str = text.replace('\xa0', '')
        cols.append(text)

    if len(cols) != 3:
        continue

    name, value, growth = cols                  # 【修正3】同样由 cells 改成 cols

    # 【修正4】页面里有 3 行都叫「扣除物价增长（%）」，
    #   字典同名会互相覆盖，重名的加 #2、#3 区分开
    if name in data:
        n = 2
        while f'{name}#{n}' in data:
            n += 1
        name = f'{name}#{n}'

    data[name] = (value, growth)                # 先原样存字符串，用时再转数字

print('解析出', len(data), '行指标')


GDP_KEY = '地区生产总值（亿元）'
if GDP_KEY not in data:
    print('没找到[地区生产总值（亿元）], 页面改版了')
    print('现在有的指标是：', list(data.keys()))   # 【修正5】list() 不能再写成 list[Any]()
    exit()

# gdp, gdp_growth = data['地区生产总值']
gdp_value, gdp_growth = data[GDP_KEY]
gdp = float(gdp_value)


print()
print('2026年1-6月广东主要统计指标', gdp, '亿元')
print("比上年增长：", gdp_growth, "%")
print("换算一下：", round(gdp / 10000, 2), "万亿元")


INC_KEY = '居民人均可支配收入（元）'
if INC_KEY in data:
    inc_value, inc_growth = data[INC_KEY]
    print()
    print('居民人均可支配收入：', inc_value, '元')
    print('比上年增长：', inc_growth, '%')


# print()
# for name in ('扣除物价增长', '农民居民人均可支配收入', '扣除物价增长'):
#     time, growth = data[name]
#     print(f'{name}(亿元 or 万吨, %), {time}, ')

# check = data['扣除物价增长'][0] + data['农民居民人均可支配收入'][0] + data['扣除物价增长'][0]


# print()
# print("校验：扣除 + 农民 + 扣除 =", round(check, 2), "亿元")
# print("      官方公布的 GDP    =", gdp, "亿元")
# print("      差额              =", round(check - gdp, 2), "亿元 (0 就是对上了）")


with open('2026年1-6月广东主要统计指标1.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('指标', '1-6月', '增长率'))
    for name, (time, growth) in data.items():
        writer.writerow((name, time, growth))

print()
print('保存到 2026年1-6月广东主要统计指标.csv')
