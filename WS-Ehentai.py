#这是加过延时的版本，当然没有用，应该是要代理了
import requests
from bs4 import BeautifulSoup
import os
import re
import time  # 导入time模块

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Sending GET request...")
response = requests.get("https://e-hentai.org/g/2812978/cc49236dbb/", headers=headers)

if response.ok:
    print("GET request successful. Parsing HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_='gdtm')  # 找到所有class为'gdtm'的div元素
    print(f"Found {len(divs)} div elements with class 'gdtm'")
    for i, div in enumerate(divs):
        a = div.find('a')  # 在div元素中找到a元素
        if a:
            page_url = a.get('href')  # 从a元素的href属性中获取URL
            if page_url:
                print(f"Found page URL: {page_url}")
                # 发送一个请求到页面的url，获取页面
                print("Sending GET request to page...")
                page_response = requests.get(page_url, headers=headers)
                if page_response.ok:
                    print("GET request to page successful. Parsing HTML...")
                    page_soup = BeautifulSoup(page_response.text, 'html.parser')
                    img = page_soup.find('img', id='img')  # 在页面中找到id为'img'的img元素
                    if img:
                        image_url = img.get('src')  # 从img元素的src属性中获取URL
                        if image_url:
                            print(f"Found image URL: {image_url}")
                            # 发送一个请求到图片的url，下载图片
                            print("Downloading image...")
                            time.sleep(5)  # 在下载图片之前暂停5秒
                            img_response = requests.get(image_url, stream=True, headers=headers)
                            if img_response.ok:
                                # 打开一个新的文件，在二进制模式下写入
                                with open('img' + str(i) + '.jpg', 'wb') as out_file:
                                    # 将响应的内容写入到文件中
                                    out_file.write(img_response.content)
                                print(f"Image downloaded successfully: img{i}.jpg")
                            else:
                                print(f"Image couldn't be retreived: {image_url}")
                else:
                    print(f"Page couldn't be retreived: {page_url}")
else:
    print("Fail:", response.status_code)


'''
原代码（随便找了个page少的）
<div class="gdtm" style="background:transparent url(https://ehgt.org/m/002812/2812665-00.jpg) -300px 0 no-repeat">
    <a href="https://e-hentai.org/s/a7f8111c79/2812665-4">
        <img alt="4" title="" src="https://ehgt.org/g/blank.gif" style="width: 100px; height: 141px; margin: -1px 0px 0px -1px;">
    </a>
</div>
'''