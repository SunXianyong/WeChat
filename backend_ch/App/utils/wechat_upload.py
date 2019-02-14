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
    print(access)
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


# 获取缩略图id
def thumb_id():
    http = urllib3.PoolManager()
    access = get_acc()
    data = {'media_id': "WaPOTn8FGx9Xug29nk9U0uLAn7Hq424Zmf44v5qi9B0"}
    encoded_data = json.dumps(data).encode('utf-8')
    url = f"https://api.weixin.qq.com/cgi-bin/material/get_material?access_token={access}"
    r = http.request('POST', url, body=encoded_data, headers={'Content-Type': 'application/json'})
    dic = json.loads(r.data.decode('utf-8'))
    print(dic)

thumb_id()