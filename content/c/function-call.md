Title: 函数调用过程分析
Tags: callstack, stack frame, function call
Date: 2014-09-24

参数传递
X86时代，参数传递是通过入栈实现的，相对CPU来说，存储器访问太慢；这样函数调用的效率就不高，在x86-64时代，寄存器数量多了，GCC就可以利用多达6个寄存器来存储参数，多于6个的参数，依然还是通过入栈实现。了解这些对我们写代码很有帮助，起码有两点启示

refer:

- http://www.cnblogs.com/bangerlee/archive/2012/05/22/2508772.html
- http://www.unixwiz.net/techtips/win32-callconv-asm.html
- http://learn.akae.cn/media/ch19s01.html
