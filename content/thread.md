Title:线程(thread)
Tags: linux, thread, user thread, kernel thread
Date: 2014-10-28

线程是操作系统调度的基本单位(thread is a basic unit of CPU utilization), 它被包含在进程之中, 线程提供了一种并行的方式, 可以利用多核cpu(kernel thread). 一个进程中可以并发多个线程. 同一进程中的多条线程将共享该进程中的资源，如text区, data区, 虚拟地址空间，文件描述符和信号处理, 但线程有自己的调用栈, 寄存器环境(包括pc register), 本地存储, signal mask等. 进程是操作系统分配资源的最小单元, 相对于进程线程有以下优势:

- 创建速度快, 占用资源少
- 线程间切换比进程间更快
- 线程共享地址空间, 通讯更方便(straightforward)

![muiti thread process](/img/thread_processes.jpg)

线程有两种实现: kernel thread 和user thread.

### kernel thread  
通常说的内核线程有两种含义:

 - 运行在内核态daemon线程
 - 可以被内核调度的实体

内核线程由内核管理创建, 调度 永远都运行在内核态，抢占式的调度, 内核线程只能之用大于PAGE_OFFSET（即3GB）的地址空间，而普通进程则可以使用整个4GB的地址空间。内核线程只能调用内核函数，而普通进程必须通过系统调用才能使用内核函数.

### user thread  
用户级线程由运行时库管理创建, 调度等, 既可以运行在用户态也可以运行在内核态(参见[系统调用](/posts/misc/systemcall.html)), 对于操作系统是不可见的，因此无法操作系统被调度. 

相对于内核线程切换速度更快在用户态就可以完成，不需要内核参与. user threads differ from fibers in that each user thread has its own thread context instead of sharing the thread context of a single thread. 
### thread model  
常见有三种线程模型:

 - M:1: 多个用户线程对应一个内核线程, 来自用户线程的系统调用都由这个内核线程来处理, 这样有个很大的缺点如果有个阻塞的系统调用则所有线程都被阻塞了, 也不能利用多cpu.
 - 1:1: 每个用户线程对应一个内核线程, 解决了M: 1的问题, linux就是这种实现.
 - M:N: M个用户线程对应N内核线程, 参见refer[6]

### linux 线程实现  
从Linux内核的角度而言，并不存在线程这个概念。内核对线程并没有设立特别的数据结构，而是与进程一样使用task_struct结构进行描述.

也就是说线程在内核中也是以一个进程而存在的，都是通过系统调用clone创建, 只不过它和同类的进程共享某些资源，例如进程地址空间，进程的信号，打开的文件等(Calling clone() with CLONE_FS, CLONE_VM, CLONE_SIGHAND, and CLONE_FILES, as all of these data structures will be shared), 我们将这类特殊的进程称之为轻量级进程(Light Weight Process). 

pthread_create 函数在linxu上就是包装的clone. 另外POSIX标准规定在一个多线程的应用程序中，所有线程都必须具有相同的PID。从线程在内核中的实现可得知，每个线程其实都有自己的pid, 为此Linux引入了线程组的概念。在一个多线程的程序中，所有线程形成一个线程组。每一个线程通常是由主线程创建的，主线程即为调用pthread_create()的线程, 对于线程组中的线程来说，其task_struct结构中的tgid字段保存该线程组中主线程的pid，而pid字段则保存每个轻量级进程的本身的pid。对于普通的进程而言，tgid和pid是相同的。事实上，getpid()系统调用中返回的是进程的tgid而不是pid。

refer:
 - [0][http://blog.jobbole.com/38696/](http://blog.jobbole.com/38696/)
 - [1][http://www.tutorialspoint.com/operating_system/os_multi_threading.htm](http://www.tutorialspoint.com/operating_system/os_multi_threading.htm)
 - [2][http://edsionte.com/techblog/archives/tag/pthread](http://edsionte.com/techblog/archives/tag/pthread)
 - [3][http://www.evanjones.ca/software/threading.html](http://www.evanjones.ca/software/threading.html)
 - [4][http://www.linuxjournal.com/article/1363](http://www.linuxjournal.com/article/1363)
 - [5][http://stackoverflow.com/questions/1178785/relationship-between-a-kernel-and-a-user-thread](http://stackoverflow.com/questions/1178785/relationship-between-a-kernel-and-a-user-thread)
 - [6][http://courses.cs.vt.edu/cs5204/fall09-kafura/Presentations/Scheduler-Activations.pdf](http://courses.cs.vt.edu/cs5204/fall09-kafura/Presentations/Scheduler-Activations.pdf)
 - [7][http://landley.net/kdocs/ols/2002/ols2002-pages-330-337.pdf](http://landley.net/kdocs/ols/2002/ols2002-pages-330-337.pdf)
 - [8][http://web.cs.ucdavis.edu/~wu/ecs251/KernelScheduledEntity_FreeBSD_2000.pdf](http://web.cs.ucdavis.edu/~wu/ecs251/KernelScheduledEntity_FreeBSD_2000.pdf)
 - [9][https://courses.cs.washington.edu/courses/cse451/11au/section/kim_au_section4.pdf](https://courses.cs.washington.edu/courses/cse451/11au/section/kim_au_section4.pdf)
