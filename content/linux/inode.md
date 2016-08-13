Title: inode


- 文件的字节数
- 文件拥有者的User ID
- 文件的Group ID
- 文件的读、写、执行权限
- 文件的时间戳，共有三个：ctime指inode上一次变动的时间，mtime指文件内容上一次变动的时间，atime指文件上一次打开的时间。atime 的更新跟 `mount`的选项有关, 默认是 "relatime".
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

## cache and buffer

Short answer: Cached is the size of the page cache. Buffers is the size of in-memory block I/O buffers. Cached matters; Buffers is largely irrelevant.

Linux performs all file I/O through the page cache. Writes are implemented as simply marking as dirty the corresponding pages in the page cache; the flusher threads then periodically write back to disk any dirty pages. Reads are implemented by returning the data from the page cache; if the data is not yet in the cache, it is first populated. 

Prior to Linux kernel version 2.4, the two caches were distinct: Files were in the page cache, disk blocks were in the buffer cache. Given that most files are represented by a filesystem on a disk, data was represented twice, once in each of the caches. Many Unix systems follow a similar pattern. Starting with Linux kernel version 2.4, the contents of the two caches were unified. The VM subsystem now drives I/O and it does so out of the page cache. If cached data has both a file and a block representation—as most data does—the buffer cache will simply point into the page cache; thus only one instance of the data is cached in memory.

