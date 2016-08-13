Title: 内存分页

从80386开始，所有的80x86处理器都支持分页，它通过设置cr0寄存器的PG标志启用。当PG=0时，线性地址就被解释成物理地址。

### linear address

The 32 bits of a linear address are divided into three fields:

- Directory, The most significant 10 bits
- Table, The intermediate 10 bits
- Offset, The least significant 12 bits


### 页帧(page frame)

The virtual address space is divided into pages, The physical address space is likewise divided into page frames. The MMU is responsible for maintaing a map of pages to page frames. A page frame will be the same size as a page, and it will have the same page alignment.

### 页表(page table)
把线性地址映射到物理地址的数据结构称为页表（page table），页表存放在主存中，并在启动分页单元之前必须由内核对页表进行适当的初始化。

页表用于向每个进程提供一致的虚拟地址空间。应用程序看到的地址空间是一个连续的内存区，该表也将虚拟内存映射到物理内存，因而支持共享内存的实现，还可以在不额外增加物理内存的情况下，将页换出到设备来增加有效的可用内存。 层次化的页表用于支持对大地址空间的快速、高效的管理

每个活动进程必须有一个分配给它的页目录。不过，没有必要马上为进程的所有页表都分配RAM，只有进程在实际需要一个页表时才给该页表分配RAM会更有效率, 正在使用的页目录的物理地址存放在控制寄存器cr3中.

线性地址内的Directory字段决定页目录中的目录项，而目录项指向适当的页表, 地址址的Table字段依次又决定页表中的表项，而表项含有页所在页帧的物理地址, Offset字段决定页帧内的相对位置.

![paging unit](/img/paging-unit.png)

 Linux内核软件架构习惯于分成硬件相关层和硬件无关层。对于页表管理，2.6.10以前（包括2.6.10）在硬件无关层使用了3级页表目录管理的方式，它不管底层硬件是否实现的也是3级的页表管理：

Page Global Directory (PGD)

Page Middle Directory (PMD)

Page Table (PTE)

从2.6.11开始，为了配合64位CPU的体系结构，硬件无关层则使用了4级页表目录管理的方式：

Page Global Directory (PGD)

Page Upper Directory (PUD)

Page Middle Directory (PMD)

Page Table (PTE)


### Page Frame Reclaiming Algorithm (PFRA)

Linux uses kswapd deamon for reclaiming frames. Kswapd traverses lru list and reclaims pages until free memory size > some threshold. Linux 引入了两个页面标志符 PG_active 和 PG_referenced 用于标识页面的活跃程度，从而决定如何在两个链表之间移动页面。PG_active 用于表示页面当前是否是活跃的，如果该位被置位，则表示该页面是活跃的。PG_referenced 用于表示页面最近是否被访问过，每次页面被访问，该位都会被置位。

    The LRU Lists
    ■ Two linked lists of pages for each zone(struct zone): the active list and the inactive list
    ■ Clearly, we reclaim pages from the inactive list first
    ■ If a page hasn’t been referenced lately, it moves to the inactive list
    ■ If a page is referenced, it doesn’t get moved to the active list immediately


    The first time a page is accessed, the PG referenced flag is set
    ■ The next time it’s accessed, it’s moved to the active list(PG_active)
    ■ That is, it takes two accesses for a page to be declared active
    ■ More precisely, it takes two accesses in different scans for a page to become
    active
    ■ If the second access doesn’t happen soon enough, PG referenced is reset

见链接[PFRA](https://www.cs.columbia.edu/~smb/classes/s06-4118/l19.pdf)

refer:

- [http://guojing.me/linux-kernel-architecture/posts/system-paging-unit/](http://guojing.me/linux-kernel-architecture/posts/system-paging-unit/)
- [http://www.slideshare.net/zijia/linux-13101650](http://www.slideshare.net/zijia/linux-13101650)
- [http://larmbr.me/2014/01/19/the-evolution-of-4-level-page-talbe-in-linux/](http://larmbr.me/2014/01/19/the-evolution-of-4-level-page-talbe-in-linux/)
- [http://duartes.org/gustavo/blog/post/anatomy-of-a-program-in-memory/](http://duartes.org/gustavo/blog/post/anatomy-of-a-program-in-memory/)
- [http://duartes.org/gustavo/blog/post/how-the-kernel-manages-your-memory/](http://duartes.org/gustavo/blog/post/how-the-kernel-manages-your-memory/)
- [https://courses.engr.illinois.edu/ece391/references/descriptors.pdf](https://courses.engr.illinois.edu/ece391/references/descriptors.pdf)
- [http://www.cs.uni.edu/~diesburg/courses/cs3430_sp14/sessions/s14/s14_caching_and_tlbs.pdf](http://www.cs.uni.edu/~diesburg/courses/cs3430_sp14/sessions/s14/s14_caching_and_tlbs.pdf)
- [https://www.cs.rutgers.edu/~pxk/416/notes/09a-paging.html](https://www.cs.rutgers.edu/~pxk/416/notes/09a-paging.html)
