import csv
import requests
from bs4 import BeautifulSoup

# ============================================================
# 修复版2：在「广东主要统计指标.py」原版基础上，只改出错的地方
# 原版文件保持原样，本文件是独立副本，互不影响
# ============================================================

# 【修正1】删掉 from GDP import cells, gdp_growth
#   GDP.py 是上一课的脚本，import 它会把那一课整段跑一遍，
#   而且本课自己解析表格，根本不需要它的 cells / gdp_growth。
#   原版报「解析出 0 行指标」就是因为循环里用了这个外来的 cells。

URL = 'https://stats.gd.gov.cn/gmjjzyzb/content/post_4932845.html'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

resp = requests.get(URL, headers=HEADERS, timeout=10)
resp.encoding = resp.apparent_encoding          # 修中文乱码
html = resp.text

print(resp.status_code)
print(len(html))
print('源码里面有72281.05吗：', '72281.05' in html)

soup = BeautifulSoup(html, 'lxml')
table = soup.select_one('table')
print('页面标题：', soup.title.get_text(strip=True))
print('表格行数：', len(table.select('tr')))

# 【修正2】data 必须是字典 {}，不能用列表 []
#   列表只能按位置取（data[0]），字典才能按名字取（data['地区生产总值']）；
#   原版 data = [] 之后又写 data[name] = ...，最后 data.keys() 就报
#   AttributeError: 'list' object has no attribute 'keys'
data = {}

rows = table.select('tr')[1:]                   # 跳过表头那一行
for tr in rows:
    cols = []
    for td in tr.select('td'):
        text = td.get_text(strip=True)
        text = text.replace('\xa0', '')         # 去掉不换行空格
        cols.append(text)

    # 【修正3】原版写的是 cells，这里解析出来的是 cols
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

# 【修正5】页面上的指标名带单位，叫「地区生产总值（亿元）」，括号是全角的，
#   原版找的是「地区生产总值」，所以永远找不到
GDP_KEY = '地区生产总值（亿元）'
if GDP_KEY not in data:
    print('没找到[地区生产总值（亿元）], 页面改版了')
    print('现在有的指标是：', list(data.keys()))   # 【修正5】list() 不能再写成 list[Any]()
    exit()

gdp_value, gdp_growth = data[GDP_KEY]
gdp = float(gdp_value)

print()
print('2026年1-6月广东主要统计指标')
print('地区生产总值（GDP）：', gdp, '亿元')
print('比上年增长：', gdp_growth, '%')
print('换算一下：', round(gdp / 10000, 2), '万亿元')

# 【修正6】原版那三行「扣除物价增长 / 农民居民人均可支配收入」名字不存在，
#   而且拿它们去凑 GDP 校验在业务上也不成立，改成只读居民人均可支配收入
INC_KEY = '居民人均可支配收入（元）'
if INC_KEY in data:
    inc_value, inc_growth = data[INC_KEY]
    print()
    print('居民人均可支配收入：', inc_value, '元')
    print('比上年增长：', inc_growth, '%')

# 【修正7】文件编码用 utf-8-sig，Excel 双击打开才不会乱码
with open('2026年1-6月广东主要统计指标3.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('指标', '1-6月', '增长率%'))
    for name, (value, growth) in data.items():
        writer.writerow((name, value, growth))

print()
print('保存到 2026年1-6月广东主要统计指标.csv')
