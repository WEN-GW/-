# import requests

# url = "https://news.sciencenet.cn/sbhtmlnews/2026/8/390740.shtm"
# student = requests.get(url).content
# print(student)
# open('student111.word','wb').write(student)



import requests

url = "https://news.sciencenet.cn/sbhtmlnews/2026/8/390740.shtm"
resp = requests.get(url)      # 发请求，拿到 Response 对象
print(resp.content)           # 打印网页原始字节

with open("news.html", mode="wb") as f:   # wb = 二进制写入，会自动关闭
    f.write(resp.content)

print("已保存为 news.html")


