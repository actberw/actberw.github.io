#c数组与指针的区别
1. 指针是变量可以进行修改, 数组名不是变量不能进行修改

    # legal
    ptr = a;
    ptr++;

    # illegal
    a = ptr;
    a++;

2. 数组传递给函数被转换为指针

3. When the array is the operand of a unary “&” operator (so &arr yields the address of the array, not the address of its first element; same address, different type).
4. When the array is the operand of a unary “sizeof” operator (so sizeof arr yields the size of the array, not the size of a pointer).

####refer:
- http://eli.thegreenplace.net/2009/10/21/are-pointers-and-arrays-equivalent-in-c/
- http://www.360doc.com/content/11/1031/23/1317564_160688964.shtml
