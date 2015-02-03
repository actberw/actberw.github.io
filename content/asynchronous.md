
多线程单进程
多线程的设计之处就是为了在共享的程序空间中，实现并行处理任务，从而达到充分利用CPU的效果。多线程的缺点在于执行时上下文交换的开销较大，和状态同步（锁）的问题。同样它也使得程序的编写和调用复杂化。

单线程多进程
为了避免多线程造成的使用不便问题，有的语言选择了单线程保持调用简单化，采用启动多进程的方式来达到充分利用CPU和提升总体的并行处理能力。 它的缺点在于业务逻辑复杂时（涉及多个I/O调用），因为业务逻辑不能分布到多个进程之间，事务处理时长要远远大于多线程模式


I/O的阻塞与非阻塞
阻塞模式的I/O会造成应用程序等待，直到I/O完成。同时操作系统也支持将I/O操作设置为非阻塞模式，这时应用程序的调用将可能在没有拿到真正数据时就立即返回了，为此应用程序需要多次调用才能确认I/O操作完全完成。
I/O的同步与异步
I/O的同步与异步出现在应用程序中。如果做阻塞I/O调用，应用程序等待调用的完成的过程就是一种同步状况。相反，I/O为非阻塞模式时，应用程序则是异步的。

异步I/O与轮询技术
当进行非阻塞I/O调用时，要读到完整的数据，应用程序需要进行多次轮询，才能确保读取数据完成，以进行下一步的操作。
轮询技术的缺点在于应用程序要主动调用，会造成占用较多CPU时间片，性能较为低下。现存的轮询技术有以下这些：

select
poll
epoll
pselect
kqueue
read是性能最低的一种，它通过重复调用来检查I/O的状态来完成完整数据读取。select是一种改进方案，通过对文件描述符上的事件状态来进行判断。操作系统还提供了poll、epoll等多路复用技术来提高性能。
轮询技术满足了异步I/O确保获取完整数据的保证。但是对于应用程序而言，它仍然只能算时一种同步，因为应用程序仍然需要主动去判断I/O的状态，依旧花费了很多CPU时间来等待。

上一种方法重复调用read进行轮询直到最终成功，用户程序会占用较多CPU，性能较为低下。而实际上操作系统提供了select方法来代替这种重复read轮询进行状态判断。select内部通过检查文件描述符上的事件状态来进行判断数据是否完全读取。但是对于应用程序而言它仍然只能算是一种同步，因为应用程序仍然需要主动去判断I/O的状态，依旧花费了很多CPU时间等待，select也是一种轮询。

![io-model](/img/io-model.gif)

refer:

- [io model](http://english.tebyan.net/newindex.aspx?pid=31159&BookID=23760&PageIndex=92&Language=3)
- [http://www.infoq.com/cn/articles/nodejs-asynchronous-io](http://www.infoq.com/cn/articles/nodejs-asynchronous-io)
- [http://cs.brown.edu/courses/cs168/f12/handouts/async.pdf](http://cs.brown.edu/courses/cs168/f12/handouts/async.pdf)
- [http://www.zhihu.com/question/19585576](http://www.zhihu.com/question/19585576)
- [http://en.wikipedia.org/wiki/Futures_and_promises](http://en.wikipedia.org/wiki/Futures_and_promises)
- [http://www.xiaoyatou.net/archives/tag/half-synchalf-async](http://www.xiaoyatou.net/archives/tag/half-synchalf-async)
- [http://www.ruanyifeng.com/blog/2014/10/event-loop.html](http://www.ruanyifeng.com/blog/2014/10/event-loop.html)
- [http://www.oschina.net/translate/the-future-of-asynchronous-io-in-python](http://www.oschina.net/translate/the-future-of-asynchronous-io-in-python)
