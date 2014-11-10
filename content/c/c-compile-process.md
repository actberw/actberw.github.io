Title: c编译编译过程
Tags: c, compile
Date: 2014-08-05

总共包含四步:

 - 预处理(Pre-Processing) (宏定义指令, 条件编译指令, 头文件)
 - 编译(Compiling)
 - 汇编(Assembling)
 - 链接(Linking)


           pre-processing     compiling          assembling         linking  
        .c --------------> .i --------------> .s --------------> .o ------------> binary  
           (cpp / gcc -E)     (cc / gcc -S )     (as / gcc -c)      (gcc / ld)  

