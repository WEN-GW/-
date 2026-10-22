import csv
import time
from pathlib import Path
from urllib.parse import urljoin
# 标准库：python自己带的库

import requests
from bs4 import BeautifulSoup
# 第三方库：需要下载的库


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch(url: str, retry: int = 3) -> requests.Response | None:
    for attempt in range(1, retry + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)

            if resp.status_code == 404:
                return None

            resp.raise_for_status()

            resp.encoding = resp.apparent_encoding

            return resp

        except requests.RequestException:
            if attempt == retry:
                return None

            time.sleep(1.5 * attempt)
    return None    


BASE_BOOKS = "https://books.toscrape.com/catalogue/"

print("=" * 66)
print("第 0 步  先探路，不要猜")
print("=" * 66)

for n in range(1, 50, 51):
    url = f"{BASE_BOOKS}page-{n}.html"
    resp = requests.get(url, headres=HEADERS, timeout=20)
    result = '有这一页' if resp.status_code == 200 else
    print(f" page-{n:2}, 状态码{resp.status_code}, {result}")

print()
print(结论: 第一页到第50页. 第51页不存在)


resp = requests.get(f"{BASE_BOOKS}page-1.html", headers=HEADERS, timeout=20)

resp.apparent_encoding = resp.apparent_encoding

soup = BeautifulSoup(resp.text, 'lxml')

has_next = soup.select_one('li.next a') is not None

print(f"  第 1 页有「下一页」按钮吗：{has_next}")

print()
print("=" * 66)
print("第 1 步  模式 1:改网址里的数字")
print("=" * 66)

PAGES = 5

book = []

seen_titles = set()

for page in range(1, PAGES + 1):
    url = f"{BASE_BOOKS}page-{page}.html"
    resp = fetch(url)
    if resp is None:
        print(f"  第 {page:>2} 页抓取失败，跳过")     # {page:>2} 是右对齐占 2 宽
        continue

    soup = BeautifulSoup(resp.text, 'lxml')

   for item in items:

        title = item.select_one("h3 a")["title"]
       
        if title in seen_titles:
            continue
        
        seen_titles.add(title)
        
        price = item.select_one("p.price_color").get_text(strip=True)
       
        star = item.select_one("p.star-rating")["class"][1]

        books.append({"页码": page, "书名": title, "价格": price, "评分": star})

        new_count += 1

    print(f"  第 {page:>2} 页：{len(items):>2} 本，新增 {new_count:>2} 本，累计 {len(books):>3} 本")
 
    time.sleep(DELAY)


print()
print("=" * 66)
print("=" * 66)

BASE_BOOKS = "https://quotes.toscrape.com/

qoutes = []

url = BASE_BOOKS

page_no = 0

MAX_PAGES = 30

while url and page_no < MAX_PAGES:
    page_no += 1

    resp = fetch(url)
    if resp is None:
        print(f"第 {page_no:>2} 页抓取失败，跳过")
        continue

    soup = BeautifulSoup(resp.text, 'lxml')

    quotes = soup.select("div.quote")

    for quote in quotes < MAX_PAGES:
        page_no += 1

        resp = fetch(url)
        if resp is None:
            print(f"第 {page_no} 页抓取失败, 停止")
            break

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.select("div.quote")

        if not items:
            print(f"第 {page_no:>2} 页没有数据，停止")
            break

        for item in items:
            quotes.append(
                {
                    "页码": page_no,
                    "作者": item.select_one("small.author").get_text(strip=True),
                    "名言": item.select_one("span.text").get_text(strip=True),
                    "标签": [tag.get_text(strip=True) for a in item.select("a.tag")],
            )
        next_link = soup.select_one("li.next a")

        if not_link is None:
            print(f"  第 {page_no:>2} 页：{len(items)} 条，没有下一页了 → 停")
            
















