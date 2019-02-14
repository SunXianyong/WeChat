# coding=utf-8

from bs4 import BeautifulSoup
import urllib3


def get_text(url):
    url ="http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&amp;mid=2650168151&amp;idx=1&amp;sn=e6848e64f140d375f7d007359032fec8&amp;chksm=be4b562f893cdf394b04f71167ed89c1c3a95c37a829adf13a11ed216b1b3a9923c074bec1bb&amp;scene=0&amp;xtrack=1#rd"
    http = urllib3.PoolManager()
    html = http.request('GET',url)

    soup = BeautifulSoup(html.data,features="lxml")
    all_content = soup.find('div',id='img-content')
    main_content = all_content.find("div",id="js_content")

    all_p = main_content.find_all("p")

    with open("txt","w",encoding="utf8") as f:

        for i in all_p:
            if len(i.text) == 1:
                continue
            f.write(i.text+"\n")

    return "5"
