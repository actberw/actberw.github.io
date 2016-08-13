Title: 求第K大数(或者前K大)
Tags: algorithm, data structure, array 
Date: 2014-06-11 18:00:00

常用方法:

- 排序, K次冒泡就可以找到第K大的数, 时间复杂度为O(kn), 最快的排序是快排和mergesort, 然后返回已排序数组的第k个数, 算法时间复杂度为O（nlogn）, 空间复杂度为O(1)。

- 一个更好的方法是利用大/小根堆的性质：建立一个包含K个元素的最大堆, 将后续的N-K每个数与堆顶元素比较, 如果小于堆顶元素, 则将其替换堆顶元素并调整堆得结构维护最大堆的性质, 最后堆中包含有最小的K个元素, 从而堆顶元素就是第K小的数。建堆的时间为O(K), 每次调整最大堆结构时间为O(lgK), 从而总的时间复杂度为O(K + (N-K)lgK)。 注意：求第k小建大根堆, 求第k大建小根堆。

- 类快速排序方法(双层桶划分), 时间复杂度为O(N).

    - 随机选择一个支点
    - 将比支点大的数, 放到数组左边；将比支点小的数放到数组右边；将支点放到中间(属于左部分)
    - 设左部分的长度为L

        当K < L时, 递归地在左部分找第K大的数
        当K > L时, 递归地在有部分中找第(K - L)大的数
        当K = L时, 返回左右两部分的分割点（即原来的支点）, 就是要求的第K大的数

### 求第K大数

    int partion(int *array, int l, int r) {
        int tmp=array[l], i=l, j=r+1;
        while (1) {
            while (array[++i] > tmp);
            while (array[--j] < tmp) if (j==i) break;
            if (i >= j) break;
            swap(array+i, array+j);
        }
        i--;
        swap(array + l, array + i);
        return i;
    }

    int findk(int *array, int l, int r, int k) {
        int llen; // 左部分的长度为L
        int pivot = partion(array, l, r);
        llen = (pivot - l) + 1; // !!
        if (k > llen)
            return findk(array, pivot + 1, r, k - llen); // 直接是k也行 
        else if (k < llen)
            return findk(array, l, pivot, k);
        else
            return array[pivot];
    }


### 最大的K个数(top K)
最简单的就是冒泡O(N * K), 也可以直接转化为求第K大数, 然后遍历数组打印所有比第K个数大的元素, 或者用求第K大数的快排方式.
或者用最小堆.


### n个元素中的第2小元素 
>证明：在最坏情况下，利用n+ceil(lg n)-2次比较，即可得到n个元素中的第2小元素。（提示：同时找最小元素）。ceil表示向上取整


### k-th Smallest Element in the Union of Two Sorted Arrays
三种方法:

- 排序, Merge both arrays and the k-th smallest element could be accessed directly.
- 跟合并数组一样两个指针, 时间复杂度为O(k)
- 二分查找类似于find, 时间复杂度为O(lg m + lg n)

二分查找分析:
We try to approach this tricky problem by comparing middle elements of A and B, which we identify as Ai and Bj. If Ai is between Bj and Bj-1, we have just found the i+j+1 smallest element. Why? Therefore, if we choose i and j such that i+j = k-1, we are able to find the k-th smallest element. This is an important invariant that we must maintain for the correctness of this algorithm.

Summarizing the above:

    Maintaining the invariant
    i + j = k – 1,

compare the k/2-th smallest element in A(i.e. A[k/2-1]) and the k/2-th smallest element in B, 参照[中位数](/posts/algorithm/median.html)

    double findKth(int a[], int m, int b[], int n, int k) {
        //always assume that m is equal or smaller than n
        if (m > n)
            return findKth(b, n, a, m, k);
        if (m == 0)
            return b[k - 1];
        if (k == 1)
            return min(a[0], b[0]);
        //divide k into two parts
        int pa = min(k / 2, m), pb = k - pa;
        if (a[pa - 1] < b[pb - 1])
            return findKth(a + pa, m - pa, b, n, k - pa);
        else if (a[pa - 1] > b[pb - 1])
            return findKth(a, m, b + pb, n - pb, k - pb);
        else
            return a[pa - 1];
    }

### Kth smallest element in a row-wise and column-wise sorted 2D array

> Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the given 2D array.

>For example, consider the following 2D array.

        10, 20, 30, 40  
        15, 25, 35, 45  
        24, 29, 37, 48  
        32, 33, 39, 50  
>The 3rd smallest element is 20 and 7th smallest element is 30

方法跟[合并K个链表](/posts/adt/link-list-merge.html)一样, 用最小堆.  detailed step:

- Build a min heap of elements from first row. A heap entry also stores row number and column number.
- Do following k - 1 times.
    - Get minimum element (or root) from min heap.
    - Find row number and column number of the minimum element.
    - Replace root with the next element from same column and min-heapify the root.
- Return the top of min heap.

代码实现:

    struct HeapNode {
        int val;  // value to be stored
        int r;    // Row number of value in 2D array
        int c;    // Column number of value in 2D array
    };
     
    void swap(HeapNode *x, HeapNode *y) {
        HeapNode z = *x;
        *x = *y;
        *y = z;
    }
     
    void minHeapify(HeapNode harr[], int i, int heap_size) {
        int l = i*2 + 1;
        int r = i*2 + 2;
        int smallest = i;
        if (l < heap_size && harr[l].val < harr[i].val)
            smallest = l;
        if (r < heap_size && harr[r].val < harr[smallest].val)
            smallest = r;
        if (smallest != i)
        {
            swap(&harr[i], &harr[smallest]);
            minHeapify(harr, smallest, heap_size);
        }
    }
     
    void buildHeap(HeapNode harr[], int n) {
        int i = (n - 1)/2;
        while (i >= 0)
        {
            minHeapify(harr, i, n);
            i--;
        }
    }
     
    // This function returns kth smallest element in a 2D array mat[][]
    int kthSmallest(int mat[4][4], int n, int k) {
        // k must be greater than 0 and smaller than n*n
        if (k <= 0 || k > n*n)
           return INT_MAX;
     
        HeapNode harr[n];
        for (int i = 0; i < n; i++)
            harr[i] =  {mat[0][i], 0, i};
        buildHeap(harr, n);
     
        HeapNode hr;
        for (int i = 0; i < (k - 1); i++) {
           // Get current heap root
           hr = harr[0];
     
           int nextval = (hr.r < (n-1))? mat[hr.r + 1][hr.c]: INT_MAX;
     
           // Update heap root with next value
           harr[0] =  {nextval, (hr.r) + 1, hr.c};
           minHeapify(harr, 0, n);
        }
     
        return harr[0].val;
    }
     
    int main() {
      int mat[4][4] = { {10, 20, 30, 40},
                        {15, 25, 35, 45},
                        {25, 29, 37, 48},
                        {32, 33, 39, 50},
                      };
      cout << "7th smallest element is " << kthSmallest(mat, 4, 7);
      return 0;
    }


refer:

- [http://www.elvisyu.com/%E5%9C%A8%E6%95%B0%E7%BB%84%E4%B8%AD%E6%89%BE%E5%88%B0%E7%AC%ACk%E5%B0%8F%E5%A4%A7%E7%9A%84%E5%85%83%E7%B4%A0/](http://www.elvisyu.com/%E5%9C%A8%E6%95%B0%E7%BB%84%E4%B8%AD%E6%89%BE%E5%88%B0%E7%AC%ACk%E5%B0%8F%E5%A4%A7%E7%9A%84%E5%85%83%E7%B4%A0/)
- [http://coolshell.cn/articles/8138.html](http://coolshell.cn/articles/8138.html)
- [http://www.acmerblog.com/second-smallest-5768.html](http://www.acmerblog.com/second-smallest-5768.html)
- [http://xfhnever.github.io/blog/2014/10/21/algorithm-findk/](http://xfhnever.github.io/blog/2014/10/21/algorithm-findk/)
- [http://segmentfault.com/blog/cleverutd/1190000000510258](http://segmentfault.com/blog/cleverutd/1190000000510258)
- [http://leetcode.com/2011/01/find-k-th-smallest-element-in-union-of.html](http://leetcode.com/2011/01/find-k-th-smallest-element-in-union-of.html)
- [http://stackoverflow.com/questions/4607945/how-to-find-the-kth-smallest-element-in-the-union-of-two-sorted-arrays](http://stackoverflow.com/questions/4607945/how-to-find-the-kth-smallest-element-in-the-union-of-two-sorted-arrays)
- [http://www.cnblogs.com/CathyGao/archive/2013/05/03/3055302.html](http://www.cnblogs.com/CathyGao/archive/2013/05/03/3055302.html)
- [http://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/](http://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/)
- [http://ask.julyedu.com/question/197](http://ask.julyedu.com/question/197)
