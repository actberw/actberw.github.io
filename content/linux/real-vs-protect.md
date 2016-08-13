Title: x86实模式(real mode)和保护模式(protect mode)
Tags: real mode, protect mode, gdt, ldt, cpu ring, ring, x86
Date: 2014-09-21 21:00:00

### 8086  
1978年intel发布了8086 16-bit cpu, 20位地址总线, 最大可寻址$2^{20}$ = 1M, 同时引入了一个非常重要的概念----段, 以支持20位的地址总线。

为了支持分段机制，Intel在8086的CPU里新增了4个段寄存器: CS, DS, SS, ES. 寻址方法是：segment:offset, 物理地址 = 段地址 * 0x10 + 偏移地址.  8086的诞生标志着Intel 正式进入了x86时代. 段机制虽然实现了地址空间的提升, 但是也带来的一些问题:  

 - 同一个物理地址有多种表示方法, 例如0x01C0:0x0000和0x0000:0x1C00所表示的物理地址都是0x01C00。
 - 地址空间缺乏保护机制

### 80286及80386  
由于8086的上述问题，1982年Intel在80286的CPU里首次引入的保护模式。同时为了保持向后兼容8086, 80286支持实模式, 在实模式下工作方式跟8086相同, 寻址方式依然是: segment:offset. 支持保护模式的x86启动时工作在实模式下, Protected mode may only be entered after the system software sets up several descriptor tables and enables the Protection Enable (PE) bit in the control register 0 (CR0).

### 保护模式下的寻址  
为了实现保护模式，光是用段寄存器来确定一个基地址是不够的，至少还要有一个地址段的长度，并且还需要一些诸如访问权限之类的其他信息, 这个时候段寄存器远远不能满足要求了. 

原因有二：段寄存器只有16位，保存不了这么多信息；段寄存器个数有限，不能保存内存中所有段的信息。

所以引入了段描述符(segment descriptor), 和段描述符表(segment descriptor table, GDT and LDT)，还有四个寄存器: GDTR、LDTR、IDTR和TR. 段描述符表存放在内存中, 段寄存器也不再存储段首地址了，而是段选择器(segment selector). 下图描述了逻辑地址到线性地址的转换过程, 逻辑地址的偏移量与段描述符的Base字段的值相加就得到了线性地址.

![translation](/img/segment-address-translation.jpg)


refer:

- [0][http://blog.sina.com.cn/s/blog_65db99840100lc6g.html](http://blog.sina.com.cn/s/blog_65db99840100lc6g.html)
- [1][http://blog.chinaunix.net/uid-23069658-id-3569341.html](http://blog.chinaunix.net/uid-23069658-id-3569341.html)

