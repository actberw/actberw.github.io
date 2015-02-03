### wild pointer and dangling pointer
http://en.wikipedia.org/wiki/Dangling_pointer
read pointer declarations backwards, and pronouce the * as "pointer to"
http://www.cplusplus.com/forum/unices/51539/


### 函数指针

    void (*fptr)();


把函数的地址赋值给函数指针，可以采用下面两种形式(a function name is turned into an address when it's used in an expression.):

    fptr=&Function;
    fptr=Function;

可以采用如下两种方式来通过指针调用函数:

    x=(*fptr)();
    x=fptr();


函数指针类型:

    typedef void (*SignalHandler)(int signum);

定义了一个函数类型 `SignalHandler`


refer:

- [http://stackoverflow.com/questions/840501/how-do-function-pointers-in-c-work](http://stackoverflow.com/questions/840501/how-do-function-pointers-in-c-work)
- [http://stackoverflow.com/questions/1591361/understanding-typedefs-for-function-pointers-in-c-examples-hints-and-tips-ple](http://stackoverflow.com/questions/1591361/understanding-typedefs-for-function-pointers-in-c-examples-hints-and-tips-ple)
