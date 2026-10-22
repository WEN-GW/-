# from urllib.request import urlopen
# url = 'https://www.macroview.club/region/guangdong/gdp'
# resp = urlopen(url)
# print(resp.read())

# with open('guangdong_gdp.html', 'w') as f:

#     f.write(resp.read().decode('utf-8'))
# print('done')




# import requests

# url = 'https://www.macroview.club/region/guangdong/gdp'     # 获取网站

# resp = requests.get(url)   #调用requests库中的get方法，获取网站内容


# print(resp)  #打印响应状态码  200表示成功 404表示失败 

# print(resp.text)  #打印响应内容    
# 请求失败，可以去浏览器按F12 网络 标头 Request Headers 里面复制User-Agent 伪装成浏览器  
#  比如：headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0'}"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0" }
#  比如：dic = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0'}"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0" }



# import requests

# url = 'https://www.macroview.club/region/guangdong/gdp'    

# dic = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0'}"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0" }

# resp = requests.get(url, headers = dic)   


# print(resp) 

# print(resp.text)   # 处理反爬虫 dic



import requests

url = 'https://www.macroview.club/region/guangdong/gdp'    


resp = requests.get(url, headers = dic)   

print(resp) 

print(resp.text)