Title: assembly
Tags: assembly, gas
Date: 2014-09-21 15:00:00

### 语法格式

绝大多数 Linux 程序员以前只接触过DOS/Windows 下的汇编语言，这些汇编代码都是 Intel 风格的。但在 Unix 和 Linux 系统中，更多>采用的还是 AT&T 格式，两者在语法格式上有着很大的不同：

- 在 AT&T 汇编格式中，寄存器名要加上 '%' 作为前缀；而在 Intel 汇编格式中，寄存器名不需要加前缀
- 在 AT&T 汇编格式中，用 '$' 前缀表示一个立即操作数；而在 Intel 汇编格式中，立即数的表示不用带任何前缀
- AT&T 和 Intel 格式中的源操作数和目标操作数的位置正好相反。在 Intel 汇编格式中，目标操作数在源操作数的左边；而在 AT&T 汇>编格式中，目标操作数在源操作数的右边。
- 在 AT&T 汇编格式中，操作数的字长由操作符的最后一个字母决定，后缀'b'、'w'、'l'分别表示操作数为字节（byte，8 比特）、字（word，16 比特）和长字（long，32比特）；而在 Intel 汇编格式中，操作数的字长是用 "byte ptr" 和 "word ptr" 等前缀来表示的。

AT&T 格式 | Intel 格式
----|------
movb val, %al | mov al, byte ptr val

- 在 AT&T 汇编格式中，绝对转移和调用指令（jump/call）的操作数前要加上'*'作为前缀，而在 Intel 格式中则不需要。
- 远程转移指令和远程子调用指令的操作码，在 AT&T 汇编格式中为 "ljump" 和 "lcall"，而在 Intel 汇编格式中则为 "jmp far" 和 "call far"，即：
- 在 AT&T 汇编格式中，内存操作数的寻址方式是`section:disp(base, index, scale)`, 而在 Intel 汇编格式中，内存操作数的寻址方>式为`section:[base + index*scale + disp]`


CPU总是周而复始地做同一件事: 从内存取指令，然后解释执行它，然后再取下一条指令，再解释执行。CPU最核心的功能单元包括：

- 寄存器（Register），是CPU内部的高速存储器，像内存一样可以存取数据，但比访问内存快得多。随后的几章我们会详细介绍x86的寄存器eax、esp、eip等等，有些寄存器只能用于某种特定的用途，比如eip用作程序计数器，这称为特殊寄存器（Special-purpose Register），而另外一些寄存器可以用在各种运算和读写内存的指令中，比如eax寄存器，这称为通用寄存器（General-purpose Register）。

- 程序计数器（PC，Program Counter），是一种特殊寄存器，保存着CPU取下一条指令的地址，CPU按程序计数器保存的地址去内存中取指令然后解释执行，这时程序计数器保存的地址会自动加上该指令的长度，指向内存中的下一条指令。

- 指令译码器（Instruction Decoder）。CPU取上来的指令由若干个字节组成，这些字节中有些位表示内存地址，有些位表示寄存器编号，有些位表示这种指令做什么操作，是加减乘除还是读写内存，指令译码器负责解释这条指令的含义，然后调动相应的执行单元去执行它。
- 算术逻辑单元（ALU，Arithmetic and Logic Unit）。如果译码器将一条指令解释为运算指令，就调动算术逻辑单元去做运算，比如加减乘除、位运算、逻辑运算。指令中会指示运算结果保存到哪里，可能保存到寄存器中，也可能保存到内存中。

- 地址和数据总线（Bus）。CPU和内存之间用地址总线、数据总线和控制线连接起来，每条线上有1和0两种状态。如果在执行指令过程中>需要访问内存，比如从内存读一个数到寄存器，执行过程可以想像成这样

refer:

- http://www.ruanyifeng.com/blog/2013/10/register.html
- http://www.cnblogs.com/BoyXiao/archive/2010/11/20/1882716.html
- http://www.searchtb.com/2013/03/x86-64_register_and_function_frame.html
- http://blog.jobbole.com/40844/
- http://cseweb.ucsd.edu/classes/sp11/cse141/pdf/02/S01_x86_64.key.pdf
- https://github.com/actberw/learn-plan/blob/master/c-note/assemble.md
- http://www.mouseos.com/arch/segment_registers.html
- http://blog.csdn.net/hgd_dingjun/article/details/2809958
- http://en.wikipedia.org/wiki/X86
- http://oss.org.cn/kernel-book/ch02/2.6.1.htm
- http://www.ibm.com/developerworks/cn/linux/l-assembly/
- http://learn.akae.cn/media/ch18s01.html
- http://en.wikibooks.org/wiki/X86_Assembly/GAS_Syntax
