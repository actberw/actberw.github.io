There are four privilege levels, numbered 0 (most privileged) to 3 (least privileged), and three main resources being protected: memory, I/O ports, and the ability to execute certain machine instructions. At any given time, an x86 CPU is running in a specific privilege level, which determines what code can and cannot do. These privilege levels are often described as protection rings, with the innermost ring corresponding to highest privilege. Most modern x86 kernels use only two privilege levels, 0 and 3:

The code segment register (cs) is, however, magical. First, its contents cannot be set directly by load instructions such as mov, but rather only by instructions that alter the flow of program execution, like call. Second, and importantly for us, instead of an RPL field that can be set by code, cs has a Current Privilege Level (CPL) field maintained by the CPU itself. This 2-bit CPL field in the code segment register is always equal to the CPU’s current privilege level. 

cs寄存器还有一个很重要的功能，cs has a Current Privilege Level (CPL) field maintained by the CPU itself. 用以指明CPU的当前特权级（Current Privilege Level，CPL）。值为0代表最高优先级，而值为3代表最低优先级。Linux只用0级和3级，分别称之为内核态和用户态。

Due to restricted access to memory and I/O ports, user mode can do almost nothing to the outside world without calling on the kernel. It can’t open files, send network packets, print to the screen, or allocate memory. User processes run in a severely limited sandbox set up by the gods of ring zero.


The CPU protects memory at two crucial points: when a segment selector is loaded and when a page of memory is accessed with a linear address. 


Useful memory protection is done in the paging unit when a linear address is converted into a physical address. Each memory page is a block of bytes described by a page table entry containing two fields related to protection: a supervisor flag and a read/write flag. The supervisor flag is the primary x86 memory protection mechanism used by kernels. 

refer:

- [http://duartes.org/gustavo/blog/post/cpu-rings-privilege-and-protection/](http://duartes.org/gustavo/blog/post/cpu-rings-privilege-and-protection/)
- [http://www.mouseos.com/arch/descriptor.html](http://www.mouseos.com/arch/descriptor.html)
- [http://blog.codinghorror.com/understanding-user-and-kernel-mode/](http://blog.codinghorror.com/understanding-user-and-kernel-mode/)
