Title: inode


- 文件的字节数
- 文件拥有者的User ID
- 文件的Group ID
- 文件的读、写、执行权限
- 文件的时间戳，共有三个：ctime指inode上一次变动的时间，mtime指文件内容上一次变动的时间，atime指文件上一次打开的时间。
- 链接数，即有多少文件名指向这个inode
- 文件数据block的位置

可以用stat命令查看

http://www.ruanyifeng.com/blog/2011/12/inode.html
http://www.cnblogs.com/vamei/p/3506566.html

https://www.ibm.com/developerworks/cn/linux/l-linux-filesystem/


http://djt.qq.com/article/view/620
https://www.ibm.com/developerworks/cn/linux/l-cn-hardandsymb-links/


file descriptor table
http://www.cs.ucsb.edu/~rich/class/cs170/notes/FileSystem/filetable.rich.jpg
http://www.usna.edu/Users/cs/aviv/classes/ic221/s14/lec/18/lec.html
