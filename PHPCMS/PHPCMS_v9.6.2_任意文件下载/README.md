# PHPCMS_v9.6.2_任意文件下载

## Affected Version

- PHPCMS v9.6.1
- PHPCMS v9.6.2

## PoC

复现的时候需要注意两点：

1. 新安装的 PHPCMS_v9.6.2 目录 \PHPCMS_v9.6.2\caches\caches_commons\caches_data 缺少缓存模型文件 model.cache.php 可以通过复制 PHPCMS_v9.6.1 响应目录的文件得到。

2. 通过 xxx.php/ 的方式绕过文件后缀名检测需要在 PHP 版本为 5.2.x 时 才可以成功读取文件。

![poc.png](poc.png)

## References

1. http://www.lybbn.cn/data/datas.php?yw=176
2. https://www.seebug.org/vuldb/ssvid-93121