# coding=utf-8

import urllib3
import json


# 获取access_token
def get_acc():
    http = urllib3.PoolManager()
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx22567ecd41dcc21b&secret=a886e801f66de74eeefe44cd73e09840'
    r = http.request('GET', url)
    dic = json.loads(r.data.decode('utf-8'))
    access = dic.get("access_token")
    if not access:
        raise RuntimeError("获取access 失败")

    return access


# 上传缩略图
def up_thumb():
    http = urllib3.PoolManager()
    access = get_acc()
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={access}&type=thumb"
    filname = "mbry.JPG"
    with open(filname, "rb") as f:
        file_data = f.read()
    r = http.request('POST', url, fields={'media': (filname, file_data),})
    dic = json.loads(r.data.decode('utf-8'))
    return dic
