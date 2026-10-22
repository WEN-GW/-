url = 'https://c.53326.com/d/file/newpc202302/erieljwp13b.jpg'     # 把要访问的网址存进变量 url
import requests     # 导入第三方库 requests

B = requests.get(url).content   
# ① requests.get(url) 向服务器发请求 → 返回一个 Response（回应）对象；② .content 从回应中取出原始字节（bytes 类型，网页的“原材料”）；③ 存进变量 B

print(B)

open('图片.jpg','wb').write(B)






# 把图片的网址存进变量 url。
url = 'https://c.53326.com/d/file/newpc202302/erieljwp13b.jpg'   

# 导入第三方库 requests。
import requests 

# 核心行，链式调用分两步：① requests.get(url) 向服务器发请求，返回 Response（回应）对象；② .content 从回应中取出原始字节（bytes 类型）​，存进变量 b
B = requests.get(url).content   

# 打印字节。终端会显示 b'\xff\xd8\xff\xe0...' 这样一堆——这就是图片的原始数据（\xff\xd8 是 jpg 文件的标准开头）
print(B)

# 新建文件 b1_图片.jpg，用二进制写入模式（wb）把字节写进去，就完成了“下载”
open('图片.jpg','wb').write(B)