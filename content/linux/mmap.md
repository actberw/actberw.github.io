zero copy

传统的 Linux 操作系统的标准 I/O 接口是基于数据拷贝操作的，即 I/O 操作会导致数据在操作系统内核地址空间的缓冲区和应用程序地址空间定义的缓冲区之间进行传输。这样做最大的好处是可以减少磁盘 I/O 的操作，因为如果所请求的数据已经存放在操作系统的高速缓冲存储器中，那么就不需要再进行实际的物理磁盘 I/O 操作。但是数据传输过程中的数据拷贝操作却导致了极大的 CPU 开销，限制了操作系统有效进行数据传输操作的能力。

现代的 CPU 和存储体系结构提供了很多相关的功能来减少或避免 I/O 操作过程中产生的不必要的 CPU 数据拷贝操作


零拷贝技术分类

- 直接 I/O：对于这种数据传输方式来说，应用程序可以直接访问硬件存储，操作系统内核只是辅助数据传输：这类零拷贝技术针对的是操作系统内核并不需要对数据进行直接处理的情况，数据可以在应用程序地址空间的缓冲区和磁盘之间直接进行传输，完全不需要 Linux 操作系统内核提供的页缓存的支持。
- 在数据传输的过程中，避免数据在操作系统内核地址空间的缓冲区和用户应用程序地址空间的缓冲区之间进行拷贝。有的时候，应用程序在数据进行传输的过程中不需要对数据进行访问，那么，将数据从 Linux 的页缓存拷贝到用户进程的缓冲区中就可以完全避免，传输的数据在页缓存中就可以得到处理。在某些特殊的情况下，这种零拷贝技术可以获得较好的性能。Linux 中提供类似的系统调用主要有 mmap()，sendfile() 以及 splice()。
- 对数据在 Linux 的页缓存和用户进程的缓冲区之间的传输过程进行优化。该零拷贝技术侧重于灵活地处理数据在用户进程的缓冲区和操作系统的页缓存之间的拷贝操作。这种方法延续了传统的通信方式，但是更加灵活。在　 Linux 　中，该方法主要利用了写时复制技术。

硬件和软件之间的数据传输可以通过使用 DMA 来进行，DMA 　进行数据传输的过程中几乎不需要　 CPU 　参与，这样就可以把 CPU 解放出来去做更多其他的事情，但是当数据需要在用户地址空间的缓冲区和　 Linux 　操作系统内核的页缓存之间进行传输的时候，并没有类似　 DMA 　这种工具可以使用，CPU 　需要全程参与到这种数据拷贝操作中，所以这第三类方法的目的是可以有效地改善数据在用户地址空间和操作系统内核地址空间之间传递的效率。

mmap系统调用是将硬盘文件映射到用内存中，说的底层一些是将page cache中的页直接映射到用户进程地址空间中，从而进程可以直接访问自身地址空间的虚拟地址来访问page cache中的页, 没有内存拷贝.


 the mmap system call causes the file contents to be copied into a kernel buffer by the DMA engine. The buffer is shared then with the user process, without any copy being performed between the kernel and user memory spaces.

refer:

- [http://www.cnblogs.com/beifei/archive/2011/06/12/2078840.html](http://www.cnblogs.com/beifei/archive/2011/06/12/2078840.html)
- [http://www.linuxjournal.com/article/6345](http://www.linuxjournal.com/article/6345)
- [http://www.ibm.com/developerworks/cn/linux/l-cn-zerocopy1/](http://www.ibm.com/developerworks/cn/linux/l-cn-zerocopy1/)
- [http://lwn.net/Articles/28548/](http://lwn.net/Articles/28548/)
- [http://www.cs.ucsb.edu/~rich/class/cs170/notes/FileSystem/filetable.rich.jpg](http://www.cs.ucsb.edu/~rich/class/cs170/notes/FileSystem/filetable.rich.jpg)
