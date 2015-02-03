Title: 系统调用(system call)
Tags: linux, system call
Date: 2014-10-27

System calls provide userland processes a way to request services from the kernel, services which are managed by operating system like storage, memory, network, process management etc. System calls provide an essential interface between a process and the operating system.Usually, system calls are not invoked directly, instead, most system calls have corresponding C library wrapper functions which perform the steps required (e.g., trapping to kernel mode) in order to invoke the system call. 

### Information and Control Flow Across Priviledge Levels
As system call is processed in kernel mode, when a user space process invokes a system call, a transition between user mode and kernel mode is required and executes the appropriate kernel function.

But no process context switch(mode switch vs context switch see refer[3]) is necessary – although a privilege context switch does occur, it is processed in the context of whichever ever process invoked it. Multiple indirections, switching from user mode to kernel mode and back (much more expensive than a function call)  
![image](/img/syscall.gif)

### Implementation  
In order to actually do the switch from user mode to kernel mode there are some assembly instructions.For x86 architectures there are two possibilities: software interrupt(int $0x80) or the newer "sysenter". 

Regardless of how the *system call handler* is invoked, both possibilities cause:

 - the CPU to switch to kernel mode,
 - the necessary registers to be saved
 - some validity checks
 - invoke the system call corresponding to the number provided by the user space process.  

Simply entering kernel-space alone is not sufficient because there are multiple system calls, all of which enter the kernel in the same manner. Thus, the system call number must be passed into the kernel. On x86, the syscall number is fed to the kernel via the %eax register.  System calls are identified by their numbers. The number of the call foo is __NR_foo. For example, the number of _llseek used above is __NR__llseek, defined as 140 in /usr/include/asm-i386/unistd.h. Different architectures have different numbers.  Often, the kernel routine that handles the call foo is called sys_foo. One finds the association between numbers and names in the sys_call_table, for example in arch/i386/kernel/entry.S.  

In addition to the system call number, most syscalls require that one or more parameters be passed to them. Somehow, user-space must relay the parameters to the kernel during the trap. The easiest way to do this is via the same means that the syscall number is passed: The parameters are stored in registers. On x86, the registers ebx, ecx, edx, esi, and edi contain, in order, the first five arguments. In the unlikely case of six or more arguments, a single register is used to hold a pointer to user-space where all the parameters are stored.  

The return value is sent to user-space also via register, it is written into the %eax register on x86.The return value is defined by the system call being invoked, in general, a 0 return value indicates  success, a -1 return value indicates an error, and an error code is stored in errno.

refer:

- [0][http://en.wikipedia.org/wiki/System_call](http://en.wikipedia.org/wiki/System_call)
- [1][http://articles.manugarg.com/systemcallinlinux2_6.html](http://articles.manugarg.com/systemcallinlinux2_6.html)
- [2][http://www.enseignement.polytechnique.fr/informatique/INF583/INF583_3.pdf](http://www.enseignement.polytechnique.fr/informatique/INF583/INF583_3.pdf)
- [3][http://stackoverflow.com/questions/9238326/system-call-and-context-switch](http://stackoverflow.com/questions/9238326/system-call-and-context-switch)
- [4][http://people.ee.ethz.ch/~arkeller/linux/multi/kernel_user_space_howto-5.html](http://people.ee.ethz.ch/~arkeller/linux/multi/kernel_user_space_howto-5.html)
- [5][http://web.cs.ucdavis.edu/~wu/ecs251/KernelScheduledEntity_FreeBSD_2000.pdf](http://web.cs.ucdavis.edu/~wu/ecs251/KernelScheduledEntity_FreeBSD_2000.pdf)
