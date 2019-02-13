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

    soup = BeautifulSoup(request.data,features="lxml-xml")
    print(str(soup.xml))
    print("-"*40)

    # 互换 收发人
    to_addr = soup.ToUserName.string
    from_addr = soup.FromUserName.string

    soup.ToUserName.string = from_addr
    soup.FromUserName.string = to_addr

    # 用户消息
    print(str(soup.xml))

    if hasattr(sys.modules['__main__'], soup.MsgType.string):
        soup = getattr(sys.modules['__main__'], soup.MsgType.string+'_type')(soup)
    else:
        return 'success'

    soup.CreateTime.string = str(int(time.time()))
    return str(soup.xml)


# 文本内容回复方式
def text_type(soup):
    return soup


# 连接内容回复方式
def link_type(soup):
    get_text(soup.Url.string)
    make_mp3()
    soup.MusicURL.string = "https://music.163.com/#/song?id=516728102"
    soup.ThumbMediaId.string = "https://music.163.com/#/song?id=516728102"


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
