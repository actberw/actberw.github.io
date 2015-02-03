Title:快速排序
Tags: algorithm, sort
Date: 2014-07-02 14:00:00

快速排序也是一种采用分治法解决问题的一个典型应用。在很多编程语言中，对数组，列表进行的非稳定排序在内部实现中都使用的是快速排序。


快速排序的基本思想如下:

- 从数列中取出一个数作为中轴数(pivot), 以中轴数进行划分, 将比这个数大的数放到它的右边，小于或等于它的数放到它的左边。
- 再对左右区间重复上面两步，直到各区间只有一个数

划分操作可以分为以下5个步骤:

- 获取中轴元素
- i从左至右扫描，如果小于基准元素，则i自增，否则记下a[i]
- j从右至左扫描，如果大于基准元素，则i自减，否则记下a[j]
- 交换a[i]和a[j]
- 重复这一步骤直至i和j交错，然后和基准元素比较，然后交换。


实现:

    int partition(int *arr, int l, int r) {
        int tmp = arr[r], i = l - 1, j = r;
        while (1) {
            while (arr[++i] < tmp);
            while (arr[--j] > tmp) if (j == r) break;
            if (i >= j) break;
            swap(arr, i, j);
        }
        swap(arr, i, r);

        return i;
    }

    // 递归实现
    void qsort(int *arr, int l, int r) {
        int i;
        if (l <= r) return;
        i = partition(arr, l, r);
        qsort(arr, l, i - 1);
        qsort(arr, i + 1, r);
    }

    // 非递归实现
    void qsort(int *arr, int l, int r) {
        int pivot;
        stack_init(); 
        stack_push(r); 
        stack_push(l)
        while (!stack_empty()) {
            l = stack_pop(), r = stack_pop();
            if (l >= r) continue;
            pivot = partition(arr, l, r);
            if (pivot - l > r - pivot) {
                stack_push(pivot - 1); stack_push(l);
                stack_push(r); stack_push(pivot + 1);
            } else {
                stack_push(r); stack_push(pivot + 1);
                stack_push(pivot - 1); stack_push(l);
            }
        }
    }

特性:

- 非稳定排序
- 空间复杂度(O(lgn), 最坏O(n)), 时间复杂度(O(nlgn), 最坏O($n^2$))


### 改进1: 当划分到较小的子序列时，通常可以使用插入排序替代快速排序

把`if (l <= r) return;` 用 `if (r - l <= M) insert_sort(arr, l , r);`

### 改进2: 三者取中划分(Median of three partitioning)

选取l, mid, r的中值作为划分元素

    int MedianOf3(int *arr, int l, int r) {
        int mid = l + (h - l) >> 2;
        return (Less(arr[l], arr[mid]) ?
               (Less(arr[mid], arr[r]) ? mid : Less(arr[l], arr[r]) ? r : l) :
               (Less(arr[r], arr[mid]) ? mid : Less(arr[r], arr[l]) ? r : l));
    }


    void qsort(int *arr, int l, int r) {
        int i, median;

        if (r - l <= M) {insert_sort(arr, l , r); return;}

        median = MedianOf3(arr, l, r); 
        swap(array, r, median);
        i = partition(arr, l, r);
        qsort(arr, l, i - 1);
        qsort(arr, i + 1, r);
    }


### 改进3: 三路中划分(three way partitioning)

将文件分成三部分: 一部分比划分元素小, 一部分比划分元素大, 一部分等于划分元素.

Dijkstra的方法如下图：

![dijkstra-quick-sort](/img/dijkstra-quick-sort.jpg)

从左至右扫描数组，维护一个指针lt使得[l…lt-1]中的元素都比v小，一个指针gt使得所有[gt+1….r]的元素都大于v，以及一个指针i，使得所有[lt…i-1]的元素都和v相等。i从lo开始，从左至右开始扫描:

- 如果a[i]<v: 交换a[lt]和a[i],lt和i自增
- 如果a[i]>v:交换a[i]和a[gt], gt自减
- 如果a[i]=v: i自增

代码实现:

    void qsort(int arr, int l, int r) {
        if (r - l <= CUTTOFF - 1) {
            insert_sort(arr, l, r);
            return;
        }
        //三分区
        int lt = l, i = l, gt = r;
        int v = arr[r];
        while (i <= gt) {
            int cmp = arr[i] - v;
            if (cmp < 0) Swap(arr, lt++, i++);
            else if (cmp > 0) Swap(arr, i, gt--);
            else i++;
        }
     
        qsort(arr, l, lt - 1);
        qsort(arr, gt + 1, hi);
    }

Dijkstra的三分区快速排序虽然在快速排序发现不久后就提出来了，但是对于序列中重复值不多的情况下，它比传统的2分区快速排序需要更多的交换次数。

Bentley 和D. McIlroy在普通的三分区快速排序的基础上，对一般的快速排序进行了改进。在划分过程中，i遇到的与v相等的元素交换到最左边，j遇到的与v相等的元素交换到最右边，i与j相遇后再把数组两端与v相等的元素交换到中间


    void qsort(int *arr, int l, int r) {
        int i = l, j = r + 1;
        int p = l - 1, q = r;
        int v = arr[r];

        if (r - l <= CUTTOFF - 1) {
            insert_sort(arr, l, r);
            return;
        }

        // Bentley-McIlroy 3-way partitioning
        while (1) {
            while (Less(arr[++i], v))
                if (i == r) break;
            while (Less(v, arr[--j]))
                if (j == l) break;
     
            // pointers cross
            if (i == j && Equal(arr[i], v))
                swap(arr, ++p, i);
            if (i >= j) break;
     
            swap(arr, i, j);
            if (Equal(arr[i], v)) swap(arr, ++p, i);
            if (Equal(arr[j], v)) swap(arr, --q, j);
        }
     
        i = j + 1;
        for (int k = l; k <= p; k++) Swap(arr, k, j--);
        for (int k = r; k >= q; k--) Swap(arr, k, i++);
     
        sort(arr, l, j);
        sort(arr, i, r);
    }

refer:

- [http://blog.jobbole.com/79298/](http://blog.jobbole.com/79298/)
- [http://www.acmerblog.com/quick-sort-5789.html](http://www.acmerblog.com/quick-sort-5789.html)
- [http://geeksquiz.com/quick-sort/](http://geeksquiz.com/quick-sort/)
