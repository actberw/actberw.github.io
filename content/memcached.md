memcached


memcached 中用一个数组存储所有的slab class(元素是slab_class_t类型), 每个slab class 由很多slab page 组成, slab page划分成固定大小的chuck . 申请内存是按照slab page进行的, 默认是1M.


Memcached的高性能源于两阶段哈希（two-stage hash）结构。

http://blog.csdn.net/zsh_comeon/article/details/16924289
http://www.tuicool.com/articles/7J3mmev
