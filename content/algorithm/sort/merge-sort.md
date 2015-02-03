Title:归并排序
Tags: algorithm, sort
Date: 2014-07-02 18:00:00

归并排序就是通过将两个有序的序列合并为一个大的有序的序列的方式来实现排序。合并排序是一种典型的分治算法：首先将序列分为两部分，然后对每一部分进行循环递归的排序，然后逐个将结果进行合并。

### 合并

合并排序依赖于合并操作，即将两个已经排序的序列合并成一个序列，具体的过程如下：

- 建立辅助数组, 使其大小为两个已经排序序列之和，然后将待排序数组复制到该数组中。
- 设定两个指针，最初位置分别为两个已经排序序列的起始位置
- 比较复制数组中两个指针所指向的元素，选择相对小的元素放入到原始待排序数组中，并移动指针到下一位置
- 重复步骤3直到某一指针达到序列尾
- 将另一序列剩下的所有元素直接复制到原始数组末尾

代码:

    int aux[max_size];
    merge(int *arr, int l, int mid, int r) {
        int i = l, j = mid + 1, k;

        // 复制数组, 也可以m~r中的元素倒叙复制到aux中, 避免下面归并的if判断.
        for (k = l; i <= r; k++) { 
            axu[k] = arr[k];
        }

        for (k = l; i <= r; k++) {
            if (i > mid) arr[k] = aux[j++];
            else if (j > hi) arr[k] = aux[i++];
            else
                arr[k] = (arry[i] < arry[j]) ? arr[i++]: arry[j++]; 
        }
    }

### 数组归并排序

归并可以自顶向下或自底向上, 自顶而下的归并是一种典型的分治算法(Divide-and-Conquer)，如果两个序列已经排好序了，那么采用归并算法将这两个序列合并为一个大的序列也就是对大的序列进行了排序。

    // 自顶向下
    void merge_sort(int *arr, int l, int r) {
        int mid = l + (r - l) >> 2;
        if (r <= l) return;
        merge_sort(arr, l, mid);
        merge_sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }

    //自底向上的归并 
    void merge_sort(int *arr, int l, int r) {
        int m, i;
        for (m = 1; m < (r - l); m *= 2) {
            for (i = l; i < (r - m); i += 2m) {
                merge(arr, i, i + m -1, min(i + 2m -1, r));
            }
        }
    }

### 链表的归并排序

    // 自顶向下
    link merge_sort(link c) {
        link b, slow, fast;
        slow = fast = c;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }

        b = slow->next;
        slow->next = NULL;
        merge(merge_sort(c), merge_sort(b))
    } 

    // 自底向上
    link merge_sort(link t) {
        link p, q, tmp;
        if (t == NULL || t->next == NULL) return t;
        p = t;

        queue_init();
        while (p != NULL) {
            q = p->next;
            p->next = NULL;
            queue_put(p);
            p = q;
        }
        while (!queue_empty()) {
            tmp = merge(queue_get(), queue_get());
            queue_put(tmp);
        }

        return t;
    }

特性:

- 稳定排序
- O(n)空间复杂度(链表是O(lgn)),  O(n·lg(n))时间复杂度($C_N = 2C_\frac{N}{2} + N$)
- Does not require random access to data


归并排序的改进, 当带排序的分段很小的时候用插入排序. 

    void Insert_MergeSort(int arr[], int beg, int end, int temp_arr[]) {
        if(end - beg + 1 <= INSERT_BOUND) {
            InsertSort(arr,beg,end);
        }else {
            int mid = (beg + end) / 2;
            Insert_MergeSort(arr, beg, mid, temp_arr);
            Insert_MergeSort(arr, mid+1, end, temp_arr);
            Merge(arr, beg, mid, end, temp_arr);
        }
    }

### 原位归并

参见refer[1]

### 多路归并

1、外部排序指待排序文件较大，内存一次存放不下，尚需存放在外部介质的文件的排序。
2、为减少平衡归并中外存读写次数所采取的方法：增大归并路数和减少归并段个数。
3、利用败者树增大归并路数。
4、利用置换—选择排序增大归并段长度来减少归并段个数。
5、由长度不等的归并段，进行多路平衡归并，需要构造最佳归并树。

置换选择排序

设内存最多能够存i条记录, 在平均情况下合并段的平均长度为是2i。

胜者和败者树

设从 k 个元素中挑选一个最小的元素需 ( k-1) 次比较。 那么在对 n 个对象进行k路归并时， 总的比较次数应为： $log_{k}m * (k - 1) * (n - 1)$

采用胜者树或者败者树，从 k 个元素中挑选一个最小的元素仅需 $log_{2}k$ 次比较，这时总的比较次数将下降为: $log_{k}m * log_{2}k * (n - 1) = log_{2}m * (n - 1)$

胜者树和败者树的用处都是用lgk的时间从k个数里选出最大或者最小的一个, 败者树的优点重构时修改结点较少, 败者树的重构只需要与其父结点比较，而胜者树则需要和兄弟节点比较。

需要访问 $1 + log_{k}m$ 遍.

### 最佳归并树

由于初始归并段通常不等长, 减少读写外存的次数。 按照 HUFFMAN 树的思想，记录少的段最先合并, 不够时增加虚段。

k叉huffman 树 内部几点个数为: (m - 1) / (k - 1), 因为结果必须为整数, 所以虚段: k - 1 - (m - 1) % (k - 1)

refer:

- [0][http://blog.jobbole.com/79293/](http://blog.jobbole.com/79293/)
- [1][http://www.ahathinking.com/archives/103.html](http://www.ahathinking.com/archives/103.html)
- [http://jpkc.seiee.sjtu.edu.cn/ds/ds2/jiaoxueziyuan/kejian/92.pdf](http://jpkc.seiee.sjtu.edu.cn/ds/ds2/jiaoxueziyuan/kejian/92.pdf)
- [http://ds.ytu.edu.cn/document/gangyao/11.htm](http://ds.ytu.edu.cn/document/gangyao/11.htm)
