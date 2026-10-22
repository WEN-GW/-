import csv
import requests

from bs4 import BeautifulSoup

# 修正 1：原来写的是 'hthttps://...'，多打了 ht，
# requests 只认识 http:// 或 https:// 开头的网址，
# 所以报错：InvalidSchema: No connection adapters were found
URL = 'https://stats.gd.gov.cn/gmjjzyzb/content/post_4932845.html'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 修正 2：删掉了 from GDP import cells, gdp_growth
# GDP.py 是另一课的脚本，import 它会把那一课整个跑一遍，
# 而且 cells / gdp_growth 在本课里用不上（下面自己解析表格）

resp = requests.get(URL, headers=HEADERS, timeout=10)  # 发请求，最多等待10秒
resp.encoding = 'utf-8'  # 该网站是 utf-8 编码，直接指定，修中文乱码

html = resp.text

print(resp.status_code)  # 状态码，200 表示成功
print(len(html))  # 源码长度

print('源码里面有72281.05吗：', '72281.05' in html)  # 判断源码里面是否有72281.05

soup = BeautifulSoup(html, 'lxml')  # lxml解析器 解析html
table = soup.select_one('table')
print('页面标题：', soup.title.get_text(strip=True))
print('表格行数：', len(table.select('tr')))

# 修正 3：data 必须是字典 {}，原来写成列表 []，
# 列表不能用 data[name] 这种写法，会报 TypeError
data = {}

# 修正 4：循环里原来用的是 cells（那是从 GDP.py import 来的变量），
# 这里解析出来的是 cols，要用 cols
rows = table.select('tr')[1:]
for tr in rows:
    cols = []
    for td in tr.select('td'):
        text = td.get_text(strip=True)
        text = text.replace('\xa0', '')
        cols.append(text)

    if len(cols) != 3:  # 跳过表头等不足3列的行
        continue

    name, value, growth = cols  # 修正 5：原来写成了 cells

    # 修正 6：页面里有 3 行都叫「扣除物价增长（%）」，
    # 字典重名会互相覆盖，重名的加 #2、#3 区分
    if name in data:
        n = 2
        while f'{name}#{n}' in data:
            n += 1
        name = f'{name}#{n}'

    data[name] = (value, growth)

print('解析出', len(data), '行指标')

# 修正 7：这个页面的指标名带单位，叫「地区生产总值（亿元）」，
# 原来找的是「地区生产总值」，永远找不到
if '地区生产总值（亿元）' not in data:
    print('没找到[地区生产总值（亿元）], 页面改版了')
    print('现在有的指标是：', list(data.keys()))
    exit()

gdp_value, gdp_growth = data['地区生产总值（亿元）']
gdp = float(gdp_value)  # 数值列才有数字；增长率列保持原样

print()
print('2026年1-6月广东主要统计指标')
print('地区生产总值（GDP）：', gdp, '亿元')
print('比上年增长：', gdp_growth, '%')
print('换算一下：', round(gdp / 10000, 2), '万亿元')

# 修正 8：原来找的「扣除物价增长」「农民居民人均可支配收入」名字不对，
# 页面上叫「居民人均可支配收入（元）」，而且那几行不能拿来当 GDP 校验
if '居民人均可支配收入（元）' in data:
    inc_value, inc_growth = data['居民人均可支配收入（元）']
    print()
    print('居民人均可支配收入：', inc_value, '元')
    print('比上年增长：', inc_growth, '%')

with open('2026年1-6月广东主要统计指标.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('指标', '1-6月', '增长率%'))
    for name, (value, growth) in data.items():
        writer.writerow((name, value, growth))

print()
print('保存到 2026年1-6月广东主要统计指标.csv')
