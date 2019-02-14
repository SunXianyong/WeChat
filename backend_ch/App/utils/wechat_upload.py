# coding=utf-8

import os
import urllib3


# 获取access_token
http = urllib3.PoolManager()
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx22567ecd41dcc21b&secret=a886e801f66de74eeefe44cd73e09840'
r = http.request('GET', url)
dic = json.loads(r.data.decode('utf-8'))
access = dic.get
input()
r.read
# 上传缩略图
filname = "mbry.JPG"
cmd = f'curl -F media=@{filname} "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=access_token&type=image"'
output = os.popen(cmd)
print(output.read())
