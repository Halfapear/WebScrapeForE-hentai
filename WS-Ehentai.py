import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get("https://e-hentai.org/g/2812665/5355b535a3/", headers=headers)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        print(image['src'])
else:
    print("Fail:", response.status_code)
 #我发现你有刚才那个代码搞下来的图片的网址不对。 搞出来一堆多余的东西，那么我有个问题。按f12看源码 我改这么辅助你找到正确的image代码呢