# from ..extensions import db
import os
import hashlib
from flask import Blueprint, request, send_file, send_from_directory
from .WeChat_text import get_text
from .textToMp3 import make_mp3


music = Blueprint("music", __name__)


@music.route("/get/<filename>", methods=["GET","POST"])
def weiXin(filename):
    path = os.getcwd()

    return send_from_directory(path, filename, as_attachment=True)


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
    soup.MsgType.string = "music"
    music = soup.new_tag("Music")
    music.append(soup.Title)
    music.append(soup.Description)
    musurl = soup.new_tag("MusicUrl")
    hqmusurl = soup.new_tag("HQMusicUrl")
    thumbid = soup.new_tag("ThumbMediaId")
    musurl.string = "http://m8.music.126.net/20190214165153/b706911f1fa51d7ad3cdbd0e33504bcc/ymusic/0a18/e88d/979f/6d5282fba78b1674f3103ab87342846a.mp3"
    hqmusurl.string = "http://m8.music.126.net/20190214165153/b706911f1fa51d7ad3cdbd0e33504bcc/ymusic/0a18/e88d/979f/6d5282fba78b1674f3103ab87342846a.mp3"
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
