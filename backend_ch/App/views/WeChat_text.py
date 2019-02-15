# coding=utf-8

from bs4 import BeautifulSoup
import urllib3


def get_text(url):
    http = urllib3.PoolManager()
    html = http.request('GET',url)

    if html.status != 200:
        return "请发送公众号文章连接"

    soup = BeautifulSoup(html.data,features="lxml")
    all_content = soup.find('div',id='img-content')
    main_content = all_content.find("div",id="js_content")

    all_p = main_content.find_all("p")

    with open("txt","w",encoding="utf8") as f:

        for i in all_p:
            if len(i.text) == 1:
                continue
            f.write(i.text+"\n")

