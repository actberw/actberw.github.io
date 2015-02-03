Closing File Descriptors

n<&-
Close input file descriptor n.

0<&-, <&-
Close stdin.

n>&-
Close output file descriptor n.

1>&-, >&-
Close stdout.



cmd 2>file      把文件描述符2重定向到file，即把错误输出存到file中。
cmd > file 2>&1 stderr和stdout都被输出到file中
cmd &>file      功能与上一个相同，更为简便的写法。
cmd >& file     功能仍与上一个相同。
cmd > f1 2>f2   把stdout重定向f1，而把stderr重定向到f2
