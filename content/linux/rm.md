Title: rm 命令

coreutils 代码

rm -> rm_fts -> excise -> unlinkat

glbic 代码

./sysdeps/unix/sysv/linux/unlinkat.c

kernel 代码

fs/namei.c SYSCALL_DEFINE3 -> do_unlinkat
fs/inode.c iput 

include/linux/fs.h 中定义了 "struct inode", 其中i_count, i_nlink 分别表示文件的使用数(open)和硬链接数.

refer:

- [http://archive09.linux.com/feature/58142](http://archive09.linux.com/feature/58142)
- [http://www.hackinglinuxexposed.com/articles/20020430.html](http://www.hackinglinuxexposed.com/articles/20020430.html)
- [http://blog.csdn.net/dlutbrucezhang/article/details/9159431](http://blog.csdn.net/dlutbrucezhang/article/details/9159431)
- [http://www.ibm.com/developerworks/cn/linux/l-cn-commands/](http://www.ibm.com/developerworks/cn/linux/l-cn-commands/)
