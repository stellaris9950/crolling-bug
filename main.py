import requests
from bs4 import BeautifulSoup
import os

def download_image(url, folder="images"):
    # 如果不存在文件夹，就创建一个
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    if response.status_code == 200:
        # 图片文件名可以从url中获取，或者自己命名
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)

def fetch_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设图片在<img>标签的'src'属性中
    for img in soup.find_all('img'):
        img_url = img.get('src')
        download_image(img_url)

# 示例网站URL
url = 'https://comic.acgn.cc/view-337585.html'
fetch_images(url)
