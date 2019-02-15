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
    # 爬取连接文章内容
    s = get_text(soup.Content.string)
    if s is False:
        soup.Content.string = "请发送公众号文章连接"
        return soup

    # 转为音频 MP3
    mp3_name = make_mp3(soup.ToUserName.string)
    # mp3_name = "oH-qc1R3KtLpsIEoyIBwgiAM07C4"
    mp3_url = f"http://39.96.190.86/music/get/{mp3_name}.mp3"

    # 修改xml
    soup.MsgType.string = "music"
    music = soup.new_tag("Music")
    title = soup.new_tag("Title")
    desc = soup.new_tag("Description")
    title.string = s
    desc.string = ""
    music.append(title)
    music.append(desc)
    musurl = soup.new_tag("MusicUrl")
    hqmusurl = soup.new_tag("HQMusicUrl")
    thumbid = soup.new_tag("ThumbMediaId")
    musurl.string = mp3_url
    hqmusurl.string = mp3_url
    thumbid.string = "WaPOTn8FGx9Xug29nk9U0uLAn7Hq424Zmf44v5qi9B0"
    music.append(musurl)
    music.append(hqmusurl)
    music.append(thumbid)
    soup.MsgType.insert_after(music)
    soup.Content.extract()

    return soup


# 连接内容回复方式
def link_type(soup):

    # 爬取连接文章内容
    get_text(soup.Url.string)

    # 转为音频 MP3
    mp3_name = make_mp3(soup.ToUserName.string)
    # mp3_name = "oH-qc1R3KtLpsIEoyIBwgiAM07C4"
    mp3_url = f"http://39.96.190.86/music/get/{mp3_name}.mp3"

    # 修改xml
    soup.MsgType.string = "music"
    music = soup.new_tag("Music")
    music.append(soup.Title)
    music.append(soup.Description)
    musurl = soup.new_tag("MusicUrl")
    hqmusurl = soup.new_tag("HQMusicUrl")
    thumbid = soup.new_tag("ThumbMediaId")
    musurl.string = mp3_url
    hqmusurl.string = mp3_url
    thumbid.string = "WaPOTn8FGx9Xug29nk9U0uLAn7Hq424Zmf44v5qi9B0"
    music.append(musurl)
    music.append(hqmusurl)
    music.append(thumbid)
    soup.MsgType.insert_after(music)
    soup.Url.extract()

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
