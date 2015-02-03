Title: C预处理
Tags: c, preprocessor 
Date: 2014-09-16

C 预处理包含两部分功能, 在编译前做文本替换(宏展开)和条件编译. 所有的预处理命令都以#开头(It must be the first nonblank character). 下表是主要的预处理命令列表.

Directive    | Description
-------------|------------
#define      | Substitutes a preprocessor macro
#include     | Inserts a particular header from another file
#undef       | Undefines a preprocessor macro
#ifdef       | Returns true if this macro is defined
#ifndef      | Returns true if this macro is not defined
#if          | Tests if a compile time condition is true
#else        | The alternative for #if
#elif        | #else an #if in one statement
#endif       | Ends preprocessor conditional
#error       | Prints error message on stderr
#pragma      | Issues special commands to the compiler, using a standardized method


### 条件编译

条件编译指令包括if/ifdef/else等等,  以#if开头的语句块必须以#endif结尾.

    #ifdef DEBUG
       /* Your debugging statements here */
    #endif

上面这条预处理在调试时候非常有用, 编译的时候加上 `-DDEBUG` flag 就会处理if/endif之间的内容 就会处理if/endif之间的代码.

### 宏和带参数的宏(Parameterized Macros)

简单的宏就是做文本替换, 定义了下面的宏在预编译的时候代码中所有 `MAX_ARRAY_LENGTH` , 都会被替换成20.

    #define MAX_ARRAY_LENGTH 20

有很多内置的宏 `gcc -E -dM - < /dev/null` 可以打印出gcc中宏, 还有一些内置的预处理符号不会被打印出来，比如__DATE__, __FUNCTION__...，因为它们是由编译器展开的，而不是预处理器。

带参数的宏用来模仿函数(simulate function), 跟inline 函数的有点像, 但是它不会对参数进行类型检查.

    int square(int x) {
       return x * x;
    }

    // same as

    #define square(x) ((x) * (x))

宏参数用圆括号括起来, 必须紧跟宏后面, 不能有空格.


### 预处理操作符

1\. Macro Continuation '\'

一般宏定义必须包含在一行内, 但用 '\' 符号可以拆分成多行. 

    #define  message_for(a, b)  \
    printf(#a " and " #b ": We love you!\n")

2\. 字符串化 '#' (Stringize)

在宏定义的时候可以把传递个宏的参数转换成字符串常量.

    #include <stdio.h>

    #define  message_for(a, b)  \
        printf(#a " and " #b ": We love you!\n")

    int main(void) {
       message_for(Carole, Debra);
       return 0;
    }

预处理后会替换成

    printf("Carole" " and " "Debra" ": We love you!\n")

3\. 拼接符号 '##' (Token Pasting)

拼接符号在宏定义是可以把两个参数连接起来成一个token(It permits two separate tokens in the macro definition to be joined into a single token)

    #include <stdio.h>

    #define tokenpaster(n) printf ("token" #n " = %d", token##n)

    int main(void) {
       int token34 = 40;
       
       tokenpaster(34);
       return 0;
    }

预处理后会替换成

    printf ("token34 = %d", token34);

### 宏定义中常见的问题

1\. 语法问题

由于是纯文本替换，C预处理器不对宏体做任何语法检查，像缺个括号、少个分号神马的预处理器是不管的。这里要格外小心，由此可能引出各种奇葩的问题，一下还很难找到根源。

2\. 运算符优先级问题

下一段简单的宏实现乘法：

    #define MULTIPLY(x, y) x * y

MULTIPLY(1, 2)没问题，会正常展开成1 * 2。有问题的是这种表达式MULTIPLY(1+2, 3)，展开后成了1+2 * 3，显然优先级错了. 在宏体中，给引用的参数加个括号就能避免这问题。

    #define MULTIPLY(x, y) (x) * (y)

3\. 对自身的递归引用

    #define foo (4 + foo)

按前面的理解，(4 + foo)会展开成(4 + (4 + foo)，然后一直展开下去，直至内存耗尽。但是，预处理器采取的策略是只展开一次。也就是说，foo只会展开成(4 + foo)，而展开之后foo的含义就要根据上下文来确定了。

交叉引用宏体也只会展开一次

    #define x (4 + y)
    #define y (2 * x)

x展开成 `(4 + y) -> (4 + (2 * x))` , y展开成 `(2 * x) -> (2 * (4 + y))`

4\. 宏参数预处理

参数中若包含另外的宏，那么宏参数在被代入到宏体之前会做一次完全的展开，除非宏体中含有#或##.

    #define AFTERX(x) X_ ## x
    #define XAFTERX(x) AFTERX(x)
    #define TABLESIZE 1024
    #define BUFSIZE TABLESIZE

AFTERX(BUFSIZE)会被展开成X_BUFSIZE。因为宏体中含有##，宏参数直接代入宏体。

XAFTERX(BUFSIZE)会被展开成X_1024。因为XAFTERX(x)的宏体是AFTERX(x)，并没有#或##，所以BUFSIZE在代入前会被完全展开成1024，然后才代入宏体，变成X_1024。

refer:

- [http://www.tutorialspoint.com/cprogramming/c_preprocessors.htm](http://www.tutorialspoint.com/cprogramming/c_preprocessors.htm)
- [http://hbprotoss.github.io/posts/cyu-yan-hong-de-te-shu-yong-fa-he-ji-ge-keng.html](http://hbprotoss.github.io/posts/cyu-yan-hong-de-te-shu-yong-fa-he-ji-ge-keng.html)
