Title: 函数调用过程分析
Tags: callstack, stack frame, _cdecl
Date: 2014-09-24

参数传递
X86时代，参数传递是通过入栈实现的，相对CPU来说，存储器访问太慢；这样函数调用的效率就不高，在x86-64时代，寄存器数量多了，GCC就可以利用多达6个寄存器来存储参数，多于6个的参数，依然还是通过入栈实现。了解这些对我们写代码很有帮助，起码有两点启示


_cdecl 
_stdcall


refer:

- [http://www.unixwiz.net/techtips/win32-callconv-asm.html](http://www.unixwiz.net/techtips/win32-callconv-asm.html)
- [http://www.searchtb.com/2013/03/x86-64_register_and_function_frame.html](http://www.searchtb.com/2013/03/x86-64_register_and_function_frame.html)
