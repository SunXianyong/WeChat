# coding=utf-8
from aip import AipSpeech
import threading
import time

""" APPID AK SK """
APP_ID = '15508666'
API_KEY = 'tgBwyd0UCMT2LdOCTW6olIiF'
SECRET_KEY = '8TgXdXee1STlAO8HbW4l2TRmmDZUmQbL'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

q = []


# 生成音频二进制
def get_bin(n,text):
    """
    lan	必填	固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
    spd	选填	语速，取值0-15，默认为5中语速
    pit	选填	音调，取值0-15，默认为5中语调
    vol	选填	音量，取值0-15，默认为5中音量
    per	选填	发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
    aue	选填	3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）;
        注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。
    """

    # 百度配置项
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5, 'per': 4, 'spd': 4,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        q.append((n, result))

    else:
        raise RuntimeError("转音频错误")


# 文本读取
def make_mp3(user):

    # 多线程排序需要
    mp3_lis = []

    # 读取文件调用多线程
    with open(f'./data/{user}/txt','r',encoding='utf8') as f:
        lenth = 0
        text = ''
        for n,i in enumerate(f):
            i_len = len(bytes(i, encoding='utf-8'))
            if lenth + i_len >= 1023:
                t = threading.Thread(target=get_bin, args=(n,text))
                t.start()
                mp3_lis.append(t)
                text = ''
                lenth = 0
            lenth += i_len
            text += i

        t = threading.Thread(target=get_bin, args=(n+1,text))
        t.start()
        mp3_lis.append(t)

    # 所有线程执行结束
    [i.join() for i in mp3_lis]

    # 写入MP3文件
    name = str(time.time())
    with open(f'./data/{user}/{name}.mp3', 'wb') as f:
        q.sort(key=lambda i: i[0])
        for i in q:
            f.write(i[1])
        q.clear()

    return name