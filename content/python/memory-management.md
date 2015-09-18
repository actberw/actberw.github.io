Title: Python 内存管理
Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching

### 引用计数
在CPython中，大多数对象的生命周期都是通过对象的引用计数来管理的。引用计数是一种最直观、最简单的垃圾收集计数，与其他主流GC算法比较，它的最大优点是实时性，即任何内存，一旦没有指向它的引用，就会立即被回收。
然而引用计数存在两个比较麻烦的缺陷：
- 当程序中出现循环引用时，引用计数无法检测出来，被循环引用的内存对象就成了无法回收的内存，引起内存泄露。比如：

    list1 = []
    list1.append(list1)
    del list1

list1循环引用了自身，第二行执行完后，list1的GC变成了2，执行完del操作后，list1的引用计数变为1，并没有归零，list1的内存空间并没有被释放，造成内存泄露。

- 维护引用计数需要额外的操作, 在每次内存对象呗引用或者引用被销毁时都需要修改引用计数，这类操作被称为footprint。引用计数的footprint是很高的，使得程序的整体性能受到很大的影响 (内存池)

### 申请内存机制 

PyObject_Malloc 

SMALL_REQUEST_THRESHOLD(512B)
usedpools
arena: ARENA_SIZE(256K) 

free_list

### 垃圾回收机制(gc)

gc.get_threshold()

    update_refs(young)
    subtract_refs(young)
    gc_init_list(&unreachable)
    move_unreachable(young, &unreachable)

The reason that objects with a reference count of 0 are tentatively unreachable is as follows. Suppose object A has been marked as tentatively unreachable and is referenced by some object B. Suppose that B is in the same generation as A and is actually reachable from outside the generation, but that B comes later in the `young` list than A. Then A would be sent to the `unreachable` list when `move_unreachable` scans over it. However, when `move_unreachable` scans over B, it will notice that it’s reference count is non-zero, mark it as `GC_REACHABLE`, and traverse B’s references and mark them as reachable. Now, A has become `GC_REACHABLE` as well and has been moved to the end of the `young` list so that it’s references can also be marked as `GC_REACHABLE`. Thus, we only know that an object is unreachable after `move_unreachable` has scanned over the entire `young` list.

`Objects/obmalloc.c`

Sequential fit
Segregated free lists
Buddy system

refer:

- http://karlma8812.github.io/python/2014/06/21/python-memory-management.html
- https://docs.python.org/2/c-api/memory.html
- http://wiki.luajit.org/New-Garbage-Collector#GC-Algorithms
- http://www.slideshare.net/delimitry/python-gc
- http://patshaughnessy.net/2013/10/30/generational-gc-in-python-and-ruby
- http://hbprotoss.github.io/posts/pythonla-ji-hui-shou-ji-zhi.html
- http://yqhui.com/post/3/
- http://www.cs.nmsu.edu/~ekerriga/presentation/index2.html
