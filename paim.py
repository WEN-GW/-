import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(response))
print(response.status_code == requests.codes.ok)
print(len(response.text))
print(response.text[:210])
if response.status_code == requests.codes.ok:
    with open("rj.txt", "w", encoding="utf-8") as f:
        f.write(response.text)