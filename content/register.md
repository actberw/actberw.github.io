Title: x86 register
Tags: register, assembly
Date: 2014-09-21 20:00:00

### 数据寄存器  
8086 有8个8位数据寄存器，这些8位寄存器可分别组成16位寄存器:  
AH & AL＝AX(accumulator register):累加寄存器，常用于运算   
BH & BL＝BX(base register):基址寄存器，常用于地址索引   
CH & CL＝CX(count register):计数寄存器，常用于计数   
DH & DL＝DX(data register):数据寄存器，常用于数据传递。  

### 段寄存器  
8086设定了4个段寄存器，专门用来保存段地址, 386及以后保护模式下用来保存段选择器(segment selector), 但是仍是16位:  
CS(Code Segment):代码段寄存器   
DS(Data Segment):数据段寄存器   
SS(Stack Segment):堆栈段寄存器   
ES(Extra Segment):附加段寄存器。  
386后增加了FS,GS

### 特殊功能的寄存器  
SP(Stack Pointer):堆栈指针寄存器，可指向目前的堆栈位置。  
BP(Base Pointer):基址指针寄存器, 参见[callstack](/posts/c/function-call.html)  
SI(Source Index):源变址寄存器可用来存放相对于DS段之源变址指针  
DI(Destination Index):目的变址寄存器，可用来存放相对于 ES 段之目的变址指针。  
IP(Instruction Pointer):指令指针寄存器  
FLAGS: 标识寄存器

注: BX,BP为基址寄存器;SI,DI为变址寄存器. 32位cpu除了段寄存器外其他的加e前缀，64位cpu加r前缀. 64位cpu其他寄存器参见refer[3].

refer:

- [0][http://cseweb.ucsd.edu/classes/sp11/cse141/pdf/02/S01_x86_64.key.pdf](http://cseweb.ucsd.edu/classes/sp11/cse141/pdf/02/S01_x86_64.key.pdf)
- [1][http://nannan408.iteye.com/blog/982942](http://nannan408.iteye.com/blog/982942)
- [2][http://blog.csdn.net/hgd_dingjun/article/details/2809958](http://blog.csdn.net/hgd_dingjun/article/details/2809958)
- [3][https://software.intel.com/en-us/articles/introduction-to-x64-assembly](https://software.intel.com/en-us/articles/introduction-to-x64-assembly)
- [http://www.findfunaax.com/notes/file/262](http://www.findfunaax.com/notes/file/262)
