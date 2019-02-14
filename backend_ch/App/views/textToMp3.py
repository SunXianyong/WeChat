# coding=utf-8
from aip import AipSpeech
import threading

""" 你的 APPID AK SK """
APP_ID = '15508666'
API_KEY = 'tgBwyd0UCMT2LdOCTW6olIiF'
SECRET_KEY = '8TgXdXee1STlAO8HbW4l2TRmmDZUmQbL'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 生成音频二进制
def get_bin(text,user):

    result = client.synthesis(text, 'zh', 1, {
        'vol': 5, 'per': 3,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        return result
        # with open(f'{user}.mp3', 'ab') as f:
        #     f.write(result)
    else:
        raise RuntimeError("转音频错误")


# 文本读取
def make_mp3(user):
    mp3_lis = []
    with open('txt','r',encoding='utf8') as f:
        lenth = 0
        text = ''
        for i in f:
            i_len = len(bytes(i, encoding='utf-8'))
            if lenth + i_len >= 1023:
                t = threading.Thread(target=get_bin, args=(text,user))
                mp3_lis.append(t.start())
                text = ''
                lenth = 0
            lenth += i_len
            text += i
        t = threading.Thread(target=get_bin, args=(text, user))
        mp3_lis.append(t.start())

    with open(f'{user}.mp3', 'wb') as f:
        for i in mp3_lis:
            f.write(i)
    return user