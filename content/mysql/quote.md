Title: mysql中的引号
Tags: mysql, quote
Date: 2014-07-10 20:44:00
mysql字符串指用单引号(‘'’)或双引号(‘"’)引起来的字符序列。例如：

'a string'

"another string"

如果SQL服务器模式启用了ANSI_QUOTES，可以只用单引号引用字符串。用双引号引用的字符串被解释为一个识别符。

refer:

- [http://dev.mysql.com/doc/refman/5.6/en/string-literals.html](http://dev.mysql.com/doc/refman/5.6/en/string-literals.html)
- [http://dev.mysql.com/doc/refman/5.6/en/sql-mode.html#sqlmode_ansi_quotes](http://dev.mysql.com/doc/refman/5.6/en/sql-mode.html#sqlmode_ansi_quotes)
- [http://segmentfault.com/q/1010000000236690](http://segmentfault.com/q/1010000000236690)
