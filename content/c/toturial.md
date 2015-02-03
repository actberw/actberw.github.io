1. main两种声明形式  

        int main(void);  
        //or
        int main(int argc, char *argv[]);  

3. 常量指针和指针常量
4. C99还提供了一个头文件 <stdbool.h> 定义了bool代表_Bool，true代表1，false代表0。只要导入 stdbool.h ，就能非常方便的操作布尔类型了。
5. 数组长度:`sizeof(ARRAY)/sizeof(ARRAY_ELEMENT)`
6. Storage class specifiers:
    http://www.geeksforgeeks.org/understanding-extern-keyword-in-c/
> There are five keywords under the category of storage class specifiers, although one of them, typedef, is there more out of convenience than utility; it has its own section later since it doesn't really belong here. The ones remaining are auto, extern, register, and static.
    Storage class specifiers help you to specify the type of storage used for data objects. Only one storage class specifier is permitted in a declaration—this makes sense, as there is only one way of storing things—and if you omit the storage class specifier in a declaration, a default is chosen. The default depends on whether the declaration is made outside a function (external declarations) or inside a function (internal declarations). For external declarations the default storage class specifier will be extern and for internal declarations it will be auto. The only exception to this rule is the declaration of functions, whose default storage class specifier is always extern.
    The positioning of a declaration, the storage class specifiers used (or their defaults) and, in some cases, preceding declarations of the same name, can all affect the linkage of a name, although fortunately not its scope or duration. We will investigate the easier items first.


7. 指针数组和指向数组得指针
> 指针数组: int *p[5], 数组指针: int (*p)[5]

8. Side Effect与Sequence Point
> Accessing a volatile object, modifying an object, modifying a file, or calling a function that does any of those operations are all side effects, which are changes in the state of the execution environment. Evaluation of an expression may produce side effects. At certain specified points in the execution sequence called sequence points, all side effects of previous evaluations shall be complete and no side effects of subsequent evaluations shall have taken place.  
 写表达式应遵循的原则:
  - 在两个Sequence Point之间，同一个变量的值只允许被改变一次
  - 如果在两个Sequence Point之间既要读一个变量的值又要改它的值，只有在读写顺序确定的情况下才可以这么写。

9. C99引入了一个专门给size_t用的%zu(printf)

10. CFLAGS  

        #include <stdio.h>  
        int main(void)  
        {  
                int a;  
                    printf("%d\n", a);  
        }  

考虑下面两种编译代码的方式 ：
 - cc -Wall a.c
 - cc -Wall -O a.c
 前一种是不会编译出a未初化的警告信息的，而只有在-O的情况下，才会有未初始化的警告信息。这点就是为什么我们在makefile里的CFLAGS上总是需要-Wall和 -O。

11. 数组与指针

        #include <stdio.h>
        int main(void)
        {
            int a[5];
            printf("%x\n", a);
            printf("%x\n", a+1);
            printf("%x\n", &a);
            printf("%x\n", &a+1);
        }

如我们的a的地址是：0Xbfe2e100, 而且是32位机，那么这个程序会输出什么？

第一条printf语句应该没有问题，就是 bfe2e100
第二条printf语句你可能会以为是bfe2e101。那就错了，a+1，编译器会编译成 a+ 1*sizeof(int)，int在32位下是4字节，所以是加4，也就是bfe2e104
第三条printf语句可能是你最头疼的，我们怎么知道a的地址？我不知道吗？可不就是bfe2e100。那岂不成了a==&a啦？这怎么可能？自己存自己的？也许很多人会觉得指针和数组是一回事，那么你就错了。如果是 int *a，那么没有问题，因为a是指针，所以 &a 是指针的地址，a 和 &a不一样。但是这是数组啊a[]，所以&a其实是被编译成了 &a[0]。
第四条printf语句就很自然了，就是bfe2e104。还是不对，因为是&a是数组，被看成int(\*)[5]，所以sizeof(a)是5，也就是5*sizeof(int)，也就是bfe2e114。

Dennis当初设计C语言的初衷：  
 - 1）相信程序员，不阻止程序员做他们想做的事。  
 - 2）保持语言的简洁，以及概念上的简单。  
 - 3）保证性能，就算牺牲移植性  

12. 64位平台C/C++开发注意事项[http://coolshell.cn/articles/3512.html](http://coolshell.cn/articles/3512.html)

14. 全局变量得问题[http://coolshell.cn/articles/10115.html](http://coolshell.cn/articles/10115.html)
15. 空指针和空指针常量(NULL, '\0', 0) 
NULL is defined  as `#define NULL (void *)0`, An integer constant expression with the value 0, or such an expression cast to type void *, is called a null pointer constant.55) If a null pointer constant is converted to a pointer type, the resulting pointer, called a null pointer, is guaranteed to compare unequal to a pointer to any object or function.
16. C语言的歧义[http://coolshell.cn/articles/830.html](http://coolshell.cn/articles/830.html)
19. 进程组id和会话id[http://blog.kghost.info/2012/08/20/tty-multi-tasking/](http://blog.kghost.info/2012/08/20/tty-multi-tasking/)

