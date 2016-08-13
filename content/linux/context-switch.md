Title: 进程切换和线程切换

## TSS
Specifically, the following information is stored in the TSS:

- Processor register state
- I/O port permissions
- Inner-level stack pointers
- Previous TSS link

Linux并不使用硬件上下文切换，但是强制它为系统中每个不同的CPU创建一个TSS，这样做主要有两个理由：

- 当80x86的一个CPU从用户态切换到内核态时，它就从TSS中后去内核态堆栈的地址。
- 当用户态进程试图通过in或out指令访问一个I/O端口时，CPU需要访问存放在TSS中的I/O许可位图以检查该进程是否有访问端口的权利。

## kernel stack

Like all other architectures, x86_64 has a kernel stack for every active thread.  These thread stacks are THREAD_SIZE (2*PAGE_SIZE) big.  These stacks contain useful data as long as a thread is alive or a zombie. While the thread is in user space the kernel stack is empty except for the thread_info structure at the bottom.

Switching the Kernel Mode stack: 保存 kernel stack 地址到task_struct 的thread_struct.esp中(switch_to 中的 `load_sp0`).

## process context switch

Process switching occurs only in Kernel Mode.The contents of all registers used by a process in User Mode have already been saved on the Kernel Mode stack before performing process switching .

The set of data that must be loaded into the registers before the process resumes its execution on the CPU is called the hardware context . The 80x86 architecture includes a specific segment type called the Task State Segment (TSS), to store hardware contexts. In Linux, a part of the hardware context of a process is stored in the process descriptor, while the remaining part is saved in the Kernel Mode stack.

every process switch consists of two steps:

1. Switching the Page Global Directory to install a new address space
2. Switching the Kernel Mode stack and the hardware context, which provides all the information needed by the kernel to execute the new process, including the CPU registers.

refer:

- [http://nanxiao.me/linux-kernel-note-50-context-switch-and-mode-switch/](http://nanxiao.me/linux-kernel-note-50-context-switch-and-mode-switch/)
- [https://www.kernel.org/doc/Documentation/x86/kernel-stacks](https://www.kernel.org/doc/Documentation/x86/kernel-stacks)
