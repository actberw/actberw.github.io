Title: 线程局部存储(thread local storage)
Tags: tls, thread, linux
Date: 2014-09-22

现在使用多线程开发越来越普遍, 为了提高性能,性能局部变量使用也非常普遍.如线程私有的成员变量,buffer等. 本文首先介绍线程局部变量的2 种使用方法:

- 常规的使用方式: 相对复杂
- __thread 修饰符(c++ 11 thread_local)

## 原理

elf 新的section .tdata, .tbss 和 新的flags SHF_TLS

dynamic thread vector.

pthread_t实际是个pthread对象的地址。

refer:

- http://www.akkadia.org/drepper/tls.pdf
- http://stackoverflow.com/questions/6611346/amd64-fs-gs-registers-in-linux
- [http://www.searchtb.com/2012/09/tls.html](http://www.searchtb.com/2012/09/tls.html)
- [https://docs.oracle.com/cd/E19683-01/817-3677/chapter8-10/index.html](https://docs.oracle.com/cd/E19683-01/817-3677/chapter8-10/index.html)
- [http://codemacro.com/2014/10/07/pthread-tls-bug/](http://codemacro.com/2014/10/07/pthread-tls-bug/)
