Title: linux 内存地址

Three kinds of addresses:

- Logical address
- Linear address (also known as virtual address)
- Physical address

The Memory Management Unit (MMU) transforms a logical address into a linear address by means of a hardware circuit called a segmentation unit ; subsequently, a second hardware circuit called a paging unit transforms the linear address into a physical address.

![mmu](/img/mmu.png)


## Segmentation in Hardware

### Segment Selectors

 Logical address consists of two parts: a segment identifier and an offset that specifies the relative address within the segment. The segment identifier is a 16-bit field called the Segment Selector (see Figure 2-2), while the offset is a 32-bit field. fields of Segment Selectors.

![segment-selector](/img/segment-selector.png)

index: 指定了放在GDT或LDT中的相应段描述符坐标, GDT中GDTR + index * 8 就可以得到描述符地址(每个描述符是8B).  
TI: Table-Indicator, 指明了段描述符是在GDT(TI=0)中还是在LDT(TI=1)中  
RPL:  当相应的段选择符装入到cs寄存器中时指示出CPU当前的特权级, The value 0 denotes the highest privilege level, while the value 3 denotes the lowest one. Linux uses only levels 0 and 3, which are respectively called Kernel Mode and User Mode.

### 段描述符

每个段由一个8字节的段描述符（Segment Descriptor）表示，它描述了段的特征。段描述符放在全局描述符表（Global Descriptor Table，GDT）或局部描述符表（Local Descriptor Table，LDT）中。

![segment-descriptor-format.png](/img/segment-descriptor-format.png)

字段描述:

- Base 31:24, Base 23:16, Base 15:00(32): 基地址.
- Seg. Limit 19:16, Segment Limit 15:00(20): 段的长度, 跟据G的值可以表示1M~4M的. 
- G(1): Granularity. 0 则段大小以 bytes 为单位，反之以 4096 bytes 为单位
- D/B(1): Default operation size. Specifies 16-bit or 32-bit operations on this segment. Set this field to 1 for 32-bit operations always.
- 0(1): 保留位 
- AVL(1):可以由操作系统使用，但是被Linux忽略
- P(1): Segmen-Present.表示该段是否在内存中，Linux 中，段常驻内存，因而不会被 swap out 到硬盘，所以为1
- DPL: 用来表示可以访问该段的最低 CPU 优先级 (privilege)，0 最高，只有 kernel mode 的进程才可以访问，3最低，任何 CPL 值都可以访问
- S: Descriptor Type. 如果是0表示是系统描述符(system descriptor, LDT, TSS), 如果是1则是一般的代码或数据段.
- Type: 表示段类型以及相应的访问权限 
    - Code Segment Descriptor: 对应指令段 (code segment)，S=1，GDT/LDT皆可；
    - Data Segment Descriptor: 对应数据段 (data segment)， S=1，包含 stack segment，GDT/LDT皆可；
    - Task State Segment Descriptor(TSSD): 对应任务状态段 (task state segment)，用来存储寄存器的内容，只能处于 GDT，S=0，Type=9/11；
    - Local Descriptor Table Descriptor(LDTD): 对应包含 LDT 的 segment，同3，只能处于 GDT，S=0，Type=2


### GDT和LDT
每个cpu一个GDT, 而每个进程除了存放在GDT中的段之外如果还需要创建附加的段，可以拥有自己的LDT. GDT和LDT中的段描述符格式是一样的. 

### GDTR和LDTR

全局描述符表寄存器GDTR 48位寄存器, 用于存放全局描述符表GDT的32位的线性基地址和16位的表长限值, GDT中的段描述符的最大数目是$2^{16 - 3} - 1$.

局部描述符表寄存器LDTR 16位寄存器, 用于存放局部描述符段(表) LDT 16位的选择符。

任务寄存器TR 16位寄存器, 用于存放任务状态段(表) TSS 16位的选择符.

中断描述符表寄存器IDTR 48位寄存器, 与GDTR的作用类似用于存放中断描述符表IDT的32位线性基地址和16位表长度值.

在系统中 GDT, IDT 只有一个, 所以GDTR,IDTR中存放的是该表入口地址；而任务不只一个，所以LDTR，TR存放的是当前任务的选择符。

### 段寄存器及缓存
段寄存器地唯一目的是存放段选择器, 共有六个: cs、ss、ds、es、fs和gs, 前三个是专用的:

- cs 代码段寄存器，指向包含程序指令的段。
- ss 栈段寄存器，指向包含当前程序栈的段。
- ds 数据段寄存器，指向包含静态数据或者全局数据段。

其他三个段寄存器用作一般用途，可以指向任意的段.

每当一个段选择器被装入段寄存器时，相应的段描述符就由内存装入到对应的非编程CPU寄存器, 以后针对那个段的逻辑地址转换就可以不访问主存中的GDT或LDT。Every segment register has a "visible" portion and an "hidden" portion, the "hidden" part used to store the cached descriptor that corresponds to its segment selector. see [Segment Descriptor Cache](http://www.logix.cz/michal/doc/i386/chp05-01.htm)

## linux 实现(32 bit)

80x86处理器中的分段鼓励程序员把程序分成逻辑上相关的实体, Linux更喜欢分页的方式. 也是为了移植性考虑, 采用flat address 在 arch/x86/include/asm/segment.h中定义了:

    #define GDT_ENTRY_KERNEL_BASE   12
    #define GDT_ENTRY_KERNEL_CS             (GDT_ENTRY_KERNEL_BASE + 0)
    #define GDT_ENTRY_KERNEL_DS             (GDT_ENTRY_KERNEL_BASE + 1)
    
    #define GDT_ENTRY_DEFAULT_USER_CS       14
    
    #define GDT_ENTRY_DEFAULT_USER_DS       15
    
    #define __KERNEL_CS     (GDT_ENTRY_KERNEL_CS * 8)
    #define __KERNEL_DS     (GDT_ENTRY_KERNEL_DS * 8)
    #define __USER_DS     (GDT_ENTRY_DEFAULT_USER_DS* 8 + 3)
    #define __USER_CS     (GDT_ENTRY_DEFAULT_USER_CS* 8 + 3)


用户态 `__USER_DS` 和 `__USER_CS`,  用户态进程都使用一对相同的段描述符来对指令和数据寻址, 内核态的 `__KERNEL_CS` 和 `__KERNEL_DS`. 所有段从0开始可寻址空间位4G($2^32$), 所以Linux下逻辑地址与线性地址是一致的，即逻辑地址的偏移量字段的值与相应的线性地址的值总是一致的。

Finally, the classic “Segmentation fault” Unix error message is not due to x86-style segments, but rather invalid memory addresses normally detected by the paging unit.

linux GDT布局

![linux-gdt](/img/linux-gdt.png)

大多数用户态下的Linux程序不使用局部描述符表，内核就定义了一个缺省的LDT, 缺省的局部描述附表放在default_ldt数组中。

refer:

- [2][http://duartes.org/gustavo/blog/post/memory-translation-and-segmentation/](http://duartes.org/gustavo/blog/post/memory-translation-and-segmentation/)
- [3][段描述符](https://courses.engr.illinois.edu/ece391/references/descriptors.pdf)
- [4][http://guojing.me/linux-kernel-architecture/posts/segment-descriptor/](http://guojing.me/linux-kernel-architecture/posts/segment-descriptor/)
- [5][http://blog.zhengdong.me/2010/07/20/linux-memory-management-addressing-1](http://blog.zhengdong.me/2010/07/20/linux-memory-management-addressing-1)
