Title: 内存对齐
Tags: extern, static, register, auto
Date: 2014-09-14

cpu是按照two-, four-, eight- 16- or even 32-byte chunks 的方式访问内存的, 为了尽可能少的内存周期来访问数据提高速度，一般需要数据的内存地址必须是对齐 (align) 的. 默认要求任何K字节基本对象的地址都必须是K的倍数(K = 2, 4, 8), linux一般最高要求8字节的数据按4字节的边界对齐.

对齐规则如下:

- 在结构体内部，有效对齐值取决于自身对齐值和指定对齐值中的较小值。
- 在计算结构体自身长度时，取 用的对齐值中最大值 的整数倍；

        struct alig {
            char s;
            short n;
            int y;
            long long m;
            double z;
        };

上面代码在linux下(4字节对齐)各成员占用内存空间如下:

- s第一个成员，偏移为0，占用1字节[0]
- n 大小为2字节, 则对齐值取2, 偏移为2，占用2字节 [2-3]
- y 大小为4字节, 则对齐值取4, 偏移为4, 占用4字节[4-7]
- m 大小为8字节, 则对齐值取4, 偏移为8, 占用4字节[7-15]
- z 大小为8字节, 则对齐值取4, 偏移为8, 占用4字节[16-23]

最终计算该结构体长度，用到过的对齐值最大为4，则补齐整数倍到24即该结构体长度。


对gcc来说，可以使用预编译指令 `#pragma pack` 或者gcc特有的关键字`__attribute__` 两种方式控制对齐方式设置。

### pragma pack

声明#pragma可以设置对齐参数的数值，缺省是8字节, `#pragma pack()` sets the alignment to the one that was in effect when compilation started(可能通过 -fpack-struct[=n]指定过), n 必须是$2^x$, 表示要对齐的字节数, 遵循前面讲的对齐规则. 

    #pragma pack( [show] | [push | pop] [, identifier], n )

n 取值为1,2,4,8.

### \_\_attribute\_\_

`__attribute__` 优先级高于#pragma预编译指令, 可以放在struct/enum/union 后类型明前, 也可以放在关闭的大括号后, 推荐前一种方式.

    struct __attribute__ ((aligned(16))) test_s { short f[3]; char s;};
    // or 
    struct test_s { short f[3]; char s;} __attribute__ ((aligned(16)));


`__attribute__` 参数:

`aligned (alignment)` 定义类型最小的对齐字节数, 如果用于 struct 则是结构体间的对齐字节(也就是结构体的大小, 把struct当成一个整体了), 但是结构体成员仍按默认的方式对齐. 

另外只能用来增大对齐值, 如果小于类型默认的对齐值则忽略. alignment值必须是$2^x$, 否则会报错 "requested alignment is not a power of 2". 

当不指定aligment (`__attribute__ ((aligned))`) 时编译器会自动设定aligment 前面用到aligment的最大值(to the largest alignment which is ever used for any data type on the target machine you are compiling for)

`packed` specified that the minimum required memory be used to represent the type, 紧凑存储, 不填充(padding), 有点类似于 `#progma pack (1)` .

### Stack Boundary Alignment

函数所使用的栈空间必须是16byte的整数倍. stack growth can be changed by using the following GCC option `-mpreferred-stack-boundary=num` , the default is 4 (16 bytes or 128 bits).

### malloc 的对齐

refer:

- [http://www.ibm.com/developerworks/library/pa-dalign/](http://www.ibm.com/developerworks/library/pa-dalign/)
- [http://blog.jqian.net/post/alignment.html](http://blog.jqian.net/post/alignment.html)
- [http://www.tenouk.com/Bufferoverflowc/Bufferoverflow3.html](http://www.tenouk.com/Bufferoverflowc/Bufferoverflow3.html)
- [http://wr.informatik.uni-hamburg.de/_media/teaching/wintersemester_2013_2014/epc-14-haase-svenhendrik-alignmentinc-paper.pdf](http://wr.informatik.uni-hamburg.de/_media/teaching/wintersemester_2013_2014/epc-14-haase-svenhendrik-alignmentinc-paper.pdf)
