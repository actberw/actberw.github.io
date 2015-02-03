
共享内存可以说是最有用的进程间通信方式，也是最快的IPC形式。两个不同进程A、B共享内存的意思是，同一块物理内存被映射到进程A、B各自的进程地址空间。进程A可以即时看到进程B对共享内存中数据的更新，反之亦然。由于多个进程共享同一块内存区域，必然需要某种同步机制，互斥锁和信号量都可以。

tmpfs is a temporary filesystem that resides in memory and/or your swap partition(s), depending on how much you fill it up. 

refer:

- [http://blog.sae.sina.com.cn/archives/1953](http://blog.sae.sina.com.cn/archives/1953)
