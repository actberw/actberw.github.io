Title: enum枚举类型
tags: c, enum
Date: 2014-09-13

枚举的定义, 枚举变量的声明赋值

    enum tag { name1[=value1], ... };
    enum tag variab = name1;

需要注意的地方:

- 同一个程序中不能定义同名的枚举类型，不同的枚举类型中也不能存在同名的命名常量
- 如果不指定value默认从0开始顺序定义为0，1，2, ..., 如果某个元素指定了value, 后面的依次递增, 不同元素value值可以相同.
- 默认元素大小跟int一样(value representable as an int), 所以value 也可以是char, short int, unsigned int. gcc 可用 \_\_attribute\_\_ ((packed)) indicates that the smallest integral type should be used, 也可以用-fshort-enums 编译选项.


refer:

- [http://stackoverflow.com/questions/366017/what-is-the-size-of-an-enum-in-c](http://stackoverflow.com/questions/366017/what-is-the-size-of-an-enum-in-c)

