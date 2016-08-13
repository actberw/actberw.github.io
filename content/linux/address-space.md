Title: 地址空间

## 线性地址空间

Kernel space & virtual space are concepts of virtual memory....it doesn't mean Ram(your actual memory) is divided into kernel & User space. Each process is given virtual memory which is divided into kernel & user space. In fact, the limitations are more severe than that. Linux kernels split the 4GB address space between user processes and the kernel; under the most common configuration, the first 3GB of the 32-bit range are given over to user space, and the kernel gets the final 1GB starting at 0xc0000000(`PAGE_OFFSET`). Sharing the address space gives a number of performance benefits; in particular, the hardware's address translation buffer(TLB) can be shared between the kernel and user space. A typical 32bit Linux virtual memory map is like:

- 0x00000000-0xbfffffff: user space(3GB)

- 0xc0000000-0xffffffff: kernel space (1GB)


## 物理内存

memory node(numa), memory zone, page frame 

real computer architectures have hardware constraints that may limit the way page frames can be used. In particular, the Linux kernel must deal with two hardware constraints of the 80 x 86 architecture:

- The Direct Memory Access (DMA) processors for old ISA buses have a strong limitation: they are able to address only the first 16 MB of RAM.
- In modern 32-bit computers with lots of RAM, the CPU cannot directly access all physical memory because the linear address space is too small

物理内存被划分为:

- ZONE DMA: Some older I/O devices can only address memory up to 16M
- ZONE NORMAL: Regular memory up to 896M
- ZONE HIGHMEM: Memory above 896M

高端内存(high memory)是物理内存中的一个概念, 32位系统内核地址空间只有1G不能访问超过1G的物理内存. 没有线性地址的高端内存中的页框不能被内核访问, linux 为了能够管理高端内存将内核线性地址空间最后128MB中的一部分专门用于映射高端内存页框, 这种映射是暂时的否则只有128MB的高端内存可以被访问, 通过重复使用线性地址，使得整个高端内存能够在不同的时间被访问。 内核可以采用三种不同的机制将页框映射到高端内存，分别叫做永久内核映射、临时内核映射和非连续内存分配。

Low memory continues to be mapped directly into the kernel's address space, and is thus always reachable via a kernel-space pointer. High memory, instead, has no direct kernel mapping. When the kernel needs to work with a page in high memory, it must explicitly set up a special page table to map it into the kernel's address space first. This operation can be expensive, and there are limits on the number of high-memory pages which can be mapped at any particular time.

The kernel allocates a virtual memory area for the application, but does not allocate physical memory for it. Only when the area is accessed physical memory is allocated. This is known as “memory overcommit”, and there are ways to disable it.


refer:

- [https://lwn.net/Articles/75174/](https://lwn.net/Articles/75174/)
- [http://linux-mm.org/HighMemory](http://linux-mm.org/HighMemory)
- [https://www.cs.columbia.edu/~smb/classes/s06-4118/l19.pdf](https://www.cs.columbia.edu/~smb/classes/s06-4118/l19.pdf)
- [http://guojing.me/linux-kernel-architecture/posts/thread-page-table-and-kernel-page-table/](http://guojing.me/linux-kernel-architecture/posts/thread-page-table-and-kernel-page-table/)
- [http://duartes.org/gustavo/blog/post/page-cache-the-affair-between-memory-and-files/](http://duartes.org/gustavo/blog/post/page-cache-the-affair-between-memory-and-files/)
