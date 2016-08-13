Title: 内存分配函数malloc

一般有两种方式：

- 非入侵式，内存分配器自行先申请内存（和栈配合使用），用作记录用户层的申请记录（地址，大小）。 用户释放空间时会查找该表，除了知道释放空间大小外还能判断该指针是合法。
- 入侵式，例如用户要申请1byte的内存，而内存分配器会分配5byte的空间（32位），前面4byte用于申请的大小。释放内存时会先向前偏移4个byte找到申请大小，再进行释放。

两种方法各有优缺点，第一种安全，但慢。第二种快但对程序员的指针控制能力要求更高，稍有不慎越界了会对空间信息做成破坏。

glibc实现的是入侵式的相关代码见malloc.c:__libc_free, 测试代码.

    #include <stdlib.h>
    #include <stdio.h>
    #include <stddef.h>

    int main() {
            int size;
            void *ptr = malloc(1024);
            size = *((size_t *)ptr - 1);
            printf("size of alloc: %d\n", size);
            free(ptr);
            return 0;
    }

查看到的数值总是比申请的略大，其中一部分是用来存储分配大小的cookie信息(`set_head`), 还有一部分是因为内存对齐原因. 当申请的内存小于 DEFAULT_MMAP_THRESHOLD 时大小用 `request2size`计算:

    #define SIZE_SZ 8
    #define MALLOC_ALIGN_MASK (2 * SIZE_SZ - 1)
    #define request2size(req)                                         
      (((req) + SIZE_SZ + MALLOC_ALIGN_MASK < MINSIZE)  ?             
       MINSIZE :                                                      
       ((req) + SIZE_SZ + MALLOC_ALIGN_MASK) & ~MALLOC_ALIGN_MASK)


大于DEFAULT_MMAP_THRESHOLD 时还要进行page对齐.

refer:

- http://windmissing.github.io/linux/2016-01/memory-leak-in-linux-4.html
- http://stackoverflow.com/questions/9866145/whatre-the-differences-between-tcmalloc-jemalloc-and-memory-pool
- https://techtalk.intersec.com/2013/10/memory-part-4-intersecs-custom-allocators/#Other_custom_allocators


http://drops.wooyun.org/tips/6595
http://mqzhuang.iteye.com/blog/1014260
