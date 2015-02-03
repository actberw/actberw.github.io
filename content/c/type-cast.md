Title: 类型转换(type cast)
tags: c
Date: 2014-09-15

类型转换是把一种类型的变量转换成另一种类型的变量, 可以显式用下面的语法的进行类型转换操作.

    (type_name) expression

编译器也会需要的时候进行隐式类型转换, 把 "比较窄的" 转换成 "比较宽的" 并且不丢失信息, 正对可能发生信息丢失的编译器会发出警告. 一个好的编程实践是在需要的类型转换的时候显式进行转换. 

### 整形提升(Integer Promotion)

Integer promotion is the process by which values of integer type "smaller" than int or unsigned int are converted either to int or unsigned int

常见的算数类行转换是隐式进行的, 当操作数类型不同时会按照如下顺序转换成相同类型.

> int -> unsigned int -> long -> unsigned long -> long long -> unsigned long long -> float -> double -> long double

### 位宽不发生变化的类型转换

对于符号数和无符号数之间的转换，C语言的转换原则是底层的位表示保持不变。表达式内有符号数也有无符号数且位宽相同, 那么C语言会隐式地将有符号数参数强制类型转换为无符号数，

### 扩展位宽的类型转换

将一个无符号数转换为一个更大的数据类型采用零扩展(zero extension)；将一个补码数字转换为一个更大的类型执行的是符号扩展(sign extension), 添补最高有效位.

### 截断位宽的类型变换

直接在位域上进行截断，然后进行解释.

refer:

- [http://dawnight.diandian.com/post/2013-04-18/40050538739](http://dawnight.diandian.com/post/2013-04-18/40050538739)
- [http://stackoverflow.com/questions/8060170/printing-hexadecimal-characters-in-c](http://stackoverflow.com/questions/8060170/printing-hexadecimal-characters-in-c)
