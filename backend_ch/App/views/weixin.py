# from ..extensions import db
import sys
import time
import hashlib
from flask import Blueprint, request
from bs4 import BeautifulSoup
from .WeChat_text import get_text
from .textToMp3 import make_mp3


weixin = Blueprint("weixin", __name__)

@weixin.route("/weixin", methods=["GET","POST"])
def weiXin():
    # 微信官方验证
    if request.method == "GET":
        return weixinyanzheng()

    soup = BeautifulSoup(request.data,features="lxml-xml",from_encoding="utf-8")
    print(str(soup.xml))
    print("-"*40)

    # 互换 收发人
    to_addr = soup.ToUserName.string
    from_addr = soup.FromUserName.string

    soup.ToUserName.string = from_addr
    soup.FromUserName.string = to_addr

    # 用户消息

    if hasattr(sys.modules['App.views.weixin'], soup.MsgType.string + "_type"):
        soup = getattr(sys.modules['App.views.weixin'], soup.MsgType.string+'_type')(soup)
    else:
        return 'success'

    soup.CreateTime.string = str(int(time.time()))
    print(str(soup.xml))
    return str(soup.xml)


# 文本内容回复方式
def text_type(soup):
    return soup


# 连接内容回复方式
def link_type(soup):

    # 爬取连接文章内容
    get_text(soup.Url.string)

    # 转为音频 MP3
    make_mp3()

    # 修改xml
    soup.MsgType.string = "image"
    music = soup.new_tag("Music")
    music.append(soup.Title)
    music.append(soup.Description)
    musurl = soup.new_tag("MusicUrl")
    thumbid = soup.new_tag("ThumbMediaId")
    musurl.string = "http://m8.music.126.net/20190214151958/3efdf845da55dd9625ccf4cb1bf52fd2/ymusic/5258/0f5f/015c/e23eb784398544031837660e6d233a6e.mp3"
    thumbid.string = "WaPOTn8FGx9Xug29nk9U0uLAn7Hq424Zmf44v5qi9B0"
    music.append(musurl)
    music.append(thumbid)
    soup.MsgType.insert_after(music)
    soup.Url.extract()
    my_xml = "<xml>" \
             "<ToUserName>oH-qc1R3KtLpsIEoyIBwgiAM07C4</ToUserName>" \
             "<FromUserName>gh_c704f0a5b415</FromUserName>" \
             "<CreateTime>1550121899</CreateTime>" \
             "<MsgType>music</MsgType>" \
             "<Music>" \
             "<ThumbMediaId>WaPOTn8FGx9Xug29nk9U0uLAn7Hq424Zmf44v5qi9B0</ThumbMediaId>" \
             "</Music>" \
             "</xml>"
    return soup


# 微信官方验证
def weixinyanzheng():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    token = "sxy122333"  # 请按照公众平台官网\基本配置中信息填写

    list = [token, timestamp, nonce]

    list.sort()
    sha1 = hashlib.sha1()
    for i in list:
        sha1.update(bytes(i,encoding="utf-8"))
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return echostr
    else:
        return "失败"
