Title: 堆排序
Tags: algorithm, sort
Date: 2014-07-02 15:00:00

利用最大堆就地(in-place)排序, 排序过程为:

- 用序列的所有元素创建一个最大堆
- 然后重复删除最大元素(循环移除顶部元素到数组末尾，然后利用Sink重建堆的操作)

实现:

    #define SWAP(x, y) do {x = x^y; y = x^y; x=x^y;} while (0)

    void heap_sort(int *array, int size) {
            int i;
            //build heap
            for (i = (size/2 - 1); i >= 0; i--) {
                    siftdown(array, i, size);
            }

            //sort
            for (i = size - 1; i > 0; i--) {
                    SWAP(array[0], array[i]);
                    siftdown(array, 0, i);
            }
    }

特点:

- 不稳定排序
- O(1) 空间复杂度, O($nlgn$)时间复杂度

缺点: 其内部循环要比快速排序要长, 并且其操作在N和N/2之间进行比较和交换，当数组长度比较大的时候，对CPU缓存利用效率比较低, 非稳定性排序


refer:

- [http://blog.jobbole.com/79300/](http://blog.jobbole.com/79300/)
