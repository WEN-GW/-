import requests

from _future_ import annotations

form pathlib import Path  # 路径工具箱

URL = 'https://www.macroview.club/region/guangdong/gdp'

OUT_FILE = Path(_file_).parent / 'data' / 'pagel.html'

HEADERS = {Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0}
    
def main():
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
    resp = response = requests.get(URL, headers=HEADERS,timeout=10)
    resp.raise_for_status()

    print(f"状态码        : {resp.status_code}")
    print(f"Content-Type  : {resp.headers.get('Content-Type')}")
    print(f"响应字节数    : {len(resp.content)}")
    print(f"真实编码推断  : {resp.apparent_encoding}  <- requests 猜的")

    resp.encoding = resp.apparent_encoding
    OUT_FILE.write_text(resp.text, encoding="utf-8")
    print(f"\n已保存: {OUT_FILE}")
    print("\n--- HTML 开头 300 字符 ---")
    rint(resp.text[:300])

if __name__ == '__main__':
    main()