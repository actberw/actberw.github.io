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
           (cpp / gcc -E)     (cc1 / gcc -S )     (as / gcc -c)      (gcc / ld)  


`strace -f gcc hello.c |& grep exec` 查看调用过程, linux下cc一般是一个符号连接指向gcc, cc1可以完成预处理和编译工作. 


refer:

- [http://mooc.guokr.com/note/13202/](http://mooc.guokr.com/note/13202/)
- [https://bojieli.com/2014/11/c-compiler/](https://bojieli.com/2014/11/c-compiler/)
- [http://alpha-blog.wanglianghome.org/2011/04/14/collect2/comment-page-1/](http://alpha-blog.wanglianghome.org/2011/04/14/collect2/comment-page-1/)
- [http://cs.lmu.edu/~ray/notes/compilerarchitecture/](http://cs.lmu.edu/~ray/notes/compilerarchitecture/)
- [http://cs.boisestate.edu/~uh/cs451/lectures/meeting_01.pdf](http://cs.boisestate.edu/~uh/cs451/lectures/meeting_01.pdf)
