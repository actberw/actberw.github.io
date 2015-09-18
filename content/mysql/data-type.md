Title: mysql中的引号
Tags: mysql, quote
Date: 2014-07-10 20:44:00
mysql字符串指用单引号(‘'’)或双引号(‘"’)引起来的字符序列。例如：

'a string'

"another string"

如果SQL服务器模式启用了ANSI_QUOTES，可以只用单引号引用字符串。用双引号引用的字符串被解释为一个识别符。

### 隐式类型转换

https://vividcortex.com/blog/2014/07/21/type-conversion-rules/
http://blog.eood.cn/mysql_params
https://dev.mysql.com/doc/refman/5.6/en/type-conversion.html
http://www.zhdba.com/mysqlops/2011/08/26/sql-convert-type/
http://blog.xupeng.me/2012/02/08/type-conversion-and-index-selection-of-mysql/

### 存储空间

https://dev.mysql.com/doc/refman/5.6/en/storage-requirements.html


### 各版本区别
http://www.zhdba.com/mysqlops/2012/03/09/mysql%E5%90%84%E7%89%88%E6%9C%AC%E7%9A%84%E6%96%B0%E7%89%B9%E6%80%A7%E6%95%B4%E7%90%86/


refer:

- [http://dev.mysql.com/doc/refman/5.6/en/string-literals.html](http://dev.mysql.com/doc/refman/5.6/en/string-literals.html)
- [http://dev.mysql.com/doc/refman/5.6/en/sql-mode.html#sqlmode_ansi_quotes](http://dev.mysql.com/doc/refman/5.6/en/sql-mode.html#sqlmode_ansi_quotes)
- [http://segmentfault.com/q/1010000000236690](http://segmentfault.com/q/1010000000236690)
