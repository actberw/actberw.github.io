Title: 堆(heap)
Tags: algorithm, heap
Date: 2014-09-03

a heap is a specialized tree-based data structure, Either the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node (this kind of heap is called max heap) or the keys of parent nodes are less than or equal to those of the children and the lowest key is in the root node (min heap).  

In a heap the highest (or lowest) priority element is always stored at the root, hence the name heap. A heap is not a sorted structure and can be regarded as partially ordered. As visible from the Heap-diagram, there is no particular relationship among nodes on any given level, even among the siblings. When a heap is a *complete binary tree*, it has a smallest possible height—a heap with N nodes always has O(log N) height, 这样实现的堆成为二叉堆(binary heap)

Heaps are crucial in several efficient graph algorithms such as Dijkstra's algorithm, and in the sorting algorithm heapsort. 

Heaps are usually implemented in an array, and do not require pointers between elements. children of the node at position i would be at positions 2i+1 and 2i+2 in a zero-based array.

### 基本操作

插入: 新节点总是插在已建立的堆的最后, 然后调用sift_up 调整.
删除: 删除堆顶元素, 将堆最后一个节点填补堆顶, 然后调用sift_down 调整.

    # define MAX_SIZE 20
    # define item_t int
    typedef struct heap {
        item_t data[MAX_SIZE];
        int current_size;
    } heap ;

    //创建堆, 复杂度为O(n), n为堆的大小
    void build_heap(heap &heap, item_t *data, int n) {
        int i, j;
        // copy data
        for (i = 0; i < n; i++) {
            heap->data[i] = data[i];
        }
        heap->current_size = n;
        j = (heap-> current_size - 2) / 2; 

        while (j) {
            sift_down(heap, j, h.current_size);
            j--;
        }
    }

    // 自上向下筛选法, 基于最小堆
    void sift_down(heap &heap, int start, int n) {
        item_t tmp = heap->data[start], i = start, j;
        for (j = 2 * i + 1; j < n ; j = 2 * i + 1) {
            if (j < n && heap->data[j] > heap->data[j + 1]) j++; //j指向子节点最小的一个

            if (tmp < heap->data[j]) break;
            else {
                heap->data[i] = heap->data[j];
                i = j;
            }
        }

        heap->data[i] = tmp;
    }

    // 自下向上筛选法, 基于最小堆
    void sift_up(heap &heap, int start) {
        item_t tmp = heap->data[start], i = start,  j = (i - 1) / 2;
        while (j) {
            if (heap->data[j] < heap->data[start]) break;
            else {
                heap->data[start] = heap->data[j];
                i = j;
                j = (i - 1) / 2;
            }
        }
        heap->data[i] = tmp;
    }

    // 插入
    void insert(heap &heap, item_t x) {
        heap->data[heap->current_size] = x; // 插在末尾
        sift_up(heap, heap->current_size);
        h.current_size++;
    }

    // extract min
    void delete(heap &heap, item_t &x) {
        x = heap->data[0];
        heap->current_size--;
        heap->data[0] = heap->data[heap->current_size]; // 把最末尾的元素放入堆顶
        sift_down(heap, 0, heap->current_size);
    }

### heap的变种

- Binary heap
- [Binomial heap](http://en.wikipedia.org/wiki/Binomial_heap)
- Fibonacci heap

refer:

- [http://www.acmerblog.com/article-heap-3974.html](http://www.acmerblog.com/article-heap-3974.html)
