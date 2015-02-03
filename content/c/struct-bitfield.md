Title: struct 位域
tags: c, struct
Date: 2014-09-12

所谓“位域”是把一个字节中的二进位划分为几个不同的区域，并说明每个区域的位数。每个域有一个域名，允许在程序中按域名进行操作。位域在本质上就是一种结构类型，不过其成员是按二进位分配的.

### 声明

    struct
    {
          type [member_name] : width ;
    };

    // 示例
    struct bs{
        int a:8;
        int b:2;
        int c:6;
        int :2;
    };

type 表示类型, member_name 表示struct成员, width指定宽度(The number of bits in the bit-field).

位域的定义尚有以下几点说明:

- 一个位域必须存储在同一个字节中，不能跨两个字节(如一个字节所剩空间不够存放另一位域时，应从下一单元起存放该位域)(貌似gcc是连续分配的)
- 位域的长度不能大于一个字节的长度，也就是说不能超过8位二进位 
- 位域可以无位域名，这时它只用来作填充或调整位置, 但无名的位域是不能使用的
- 相邻的位域字段的类型不同，则各编译器的具体实现有差异
     
### 位域的使用 
位域的使用和结构成员的使用相同, `variable.field` 或者 `pointer->field`.

赋值时不能超过该位域的允许范围, 否则编译的时候会提示 *warning: large integer implicitly truncated to unsigned type*.


位域是不可移植的。因为位域不能跨越机器字，而且不同计算机中的机器字长也不同，所以一个使用了位域的程序在另一种计算机上很可能无法编译, 通常应该避免使用位域.
refer:

- [http://see.xidian.edu.cn/cpp/html/102.html](http://see.xidian.edu.cn/cpp/html/102.html)
