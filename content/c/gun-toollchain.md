###GNU工具链
1. GNU工具链包含一下几部分:
 - GCC (GNU Compiler Collection) 编译器集合
 - gnu make 自动化编译和构建工具
 - binutils (GNU Binary Utilities) as, ld等工具
 - gdb (GNU Debugger) 调试器 
 - autotools(GNU build system)
    - Autoconf
    - Autoheader
    - Automake
    - Libtool
 - glibc

2. makefile编写参见pdf(跟我一起写Makefile)
3. gcc
 - 功能: 高级语言(.c, .cpp, .F) -> (.s)
 - 组成: 一些可执行程序 + 库 (例如:cpp, gcc, g++)

4. binutils
 - 功能: 汇编语言(.s) -> 目标文件 -> 可执行程序, 查看二进制文件信息
 - 组成: 包含的命令:

  command | desc
  ----|------
  as      | assembler popularly known as GAS (Gnu ASsembler)
  ld      | linker
  gprof   | profiler
  addr2line | convert address to file and line
  ar      | create, modify, and extract from archives
  c++filt | demangling filter for C++ sy mbols
  dlltool | creation of Windows dynamic-link libraries
  gold    | alternative linker
  nlmconv | object file conversion to a NetWare Loadable Module
  nm      | list symbols in object files
  objcopy | copy object files, possibly maki     ng changes
  objdump | dump information about object files
  ranlib  | generate indexes for archives
  readelf | display content of ELF files
  size    | list total and section sizes
  strings | list printable strings
  strip   | remove symbols from an object file
  windmc  | generates Windows message resources
  windres | compiler for Windows resource files    

5. autotools(refer#1)
6. glibc
 - 功能: 提供语言和操作系统的标准函数库
 - 组成: 一些命令 + 大量库(例如: ldd, iconv, locale, posix)

7. 文件扩展名的默认含义

  扩展名 | 含义
  -------|--------
  .c, .cc| 需要预处理
  .i, .ii| 不需要预处理
  .S     | 需要预处理的汇编
  .s     | 不需要与处理的汇编
  .o     | 目标文件
  .a     | 静态库
  .s     | 动态库

refer:

- http://blog.csdn.net/scucj/article/details/6079052
