###gcc命令参数解析
1. SYNOPSIS

        gcc [-c|-S|-E] [-std=standard]
            [-g] [-pg] [-Olevel]
            [-Wwarn...] [-pedantic]
            [-Idir...] [-Ldir...]
            [-Dmacro[=defn]...] [-Umacro]
            [-foption...] [-mmachine-option...]
            [-o outfile] [@file] infile...

2. -std: 决定c标准, 可能的值: c89, c90, c99等
3. -Wall： 打印警告信息
4. -g: 添加调试信息到文件
5. -O: 优化选项-O0(default), -O1, -O2, -O3, -Os, -Ofast
6. -D, -U : 定义和取消宏定义
7. -I: 指定头文件的搜索位置
8. -L 指定动态链接库的搜索位置
9. -l 指定引用的库
10. -static 只链接静态库
11. -shared 编译为动态
11. -E: 输出预处理后的文件(.i)
12. -S: 输出编译生成的汇编文件(.s)
13. -c: 输出汇编生成的目标文件(.o)
14. -o: 指定输出文件名
15. -v: 输出编译过程详细信息

静态库过程:

    gcc -c stack.c
    ar rs libstack.a stack.o

动态库过程:

    gcc -Wall -fPIC -c stack.c // PIC是其中一种，表示生成位置无关代码(Position Independent Code)
    gcc -shared -o libstack.so stack.o

