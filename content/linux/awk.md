Title: awk 命令

An  AWK  program  is  a  sequence  of pattern {action} pairs and function definitions.  Short programs are entered on the command line usually enclosed in ' ' to avoid shell interpretation.  Longer programs can be read in from a file with the -f option.

awk程序由三部分组成，分别为：初始化（处理输入前做的准备,放在BEGIN块中），数据处理（处理输入数据），收尾处理（处理输入完成后要进行的处理，放到END块中）。

awk 'pattern {action}'

refer:

- [http://dongxicheng.org/script/awk-usage/](http://dongxicheng.org/script/awk-usage/)
- [http://coolshell.cn/articles/9070.html](http://coolshell.cn/articles/9070.html)
