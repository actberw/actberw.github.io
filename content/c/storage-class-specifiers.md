Title:  storage class specifiers 
Tags: extern, static, register, auto
Date: 2014-09-13

A storage class defines the scope (visibility) and life-time of variables and/or functions within a C Program. These specifiers precede the type that they modify. There are the following storage classes, which can be used in a C Program:

- auto 
- register 
- static 
- extern

### auto

这个这个关键字用于声明变量的生存期为自动, 内部定义的变量默认就是auto.

### register

寄存器的速度比访问内存快很多, 对访问频繁的变量可以用register关键字请求编译器尽可能的将变量存在CPU 内部寄存器中而不是通过内存寻址访问以提高效率. register 变量可能不存放在内存中，所以不能用取址运算符 `&` 来获取register 变量的地址,  否则可能会报错。register 变量必须是一个单个的值，并且其长度应小于或等于整型的长度。

### extern 

对于函数声时加extern/static, 定义时不用加. 变量加extern是声明(不分配空间)，其他都是定义. `extern int a = 5;` 会报警. 

extern 对变量不分配存储空间, 对函数默认可以不加.

### static

static 作用有两方面:

- 隐藏作用, static的函数或变量只对模块内部可见
- static 存储在.data或.bss(未出始化时), 未出始化时默认值为0, static 局部变量在每次函数调用时保留上次调用的值.

注: 全局变量变量未初始化时值也为0,  局部变量未初始化时值随机

refer:

- [http://publications.gbdirect.co.uk/c_book/chapter8/declarations_and_definitions.html](http://publications.gbdirect.co.uk/c_book/chapter8/declarations_and_definitions.html)
