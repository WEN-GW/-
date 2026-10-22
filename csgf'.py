# import requests
uRL = "https://paper.sciencenet.cn/sbhtmlnews/2026/8/390740.shtm?id=390740"
import requests
# OUTPUT = "文.docx"
bac = requests.get(uRL).content 
print(bac)
open('图片0cc0.docx','wb').write(bac)