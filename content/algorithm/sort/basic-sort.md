Title:基本排序算法
Tags: algorithm, sort
Date: 2014-07-02 12:00:00

### 分类

- 选择排序: 直接选择排序，堆排序
- 插入排序: 直接插入排序，Shell排序
- 冒泡排序: 冒泡排序，快速排序
- 线性排序算法: 计数排序, 桶排序, 基数排序
- 归并排序

### 稳定性

A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, etc. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

### 选择排序

选择排序很简单，他的步骤如下:

- 从左至右遍历，找到最小(大)的元素，然后与第一个元素交换。
- 从剩余未排序元素中继续寻找最小（大）元素，然后与第二个元素进行交换。
- 以此类推，直到所有元素均排序完毕。

遍历过的元素都是排序好的.

    void selection_sort(int *a, int n) {
        int i, j, min, t;
        for(i = 0; i < n - 1; i ++) { // i 必须小于n-1
            min = i;
            for(j = i + 1; j < n; j ++)
                if(a[min] > a[j])
                    min = j;

            if(min != i)
            {
                t = a[min];
                a[min] = a[i];
                a[i] = t;
            }
        }
    }

特性:

- Not stable(例如:5 8 5 2 9)
- O(1) 空间复杂度
- 选择排序需要花费 (N – 1) + (N – 2) + … + 1 + 0 = $\frac{N(N- 1)}{2}$ ~ $\frac{N^2}{2}$次比较 和 N-1次交换操作。

### 插入排序
具体的步骤为:

- 从第一个元素开始，该元素可以认为已经被排序
- 取出下一个元素，在已经排序的元素序列中从后向前扫描
- 如果该元素小于前面的元素（已排序），则依次与前面元素进行比较如果小于则交换，直到找到大于该元素的就则停止；
- 如果该元素大于前面的元素（已排序），则重复步骤2
- 重复步骤2~4 直到所有元素都排好序 

遍历过的元素都不一定是排序好的.

    void insertion_sort(int *array, int n) {
       int i, j, temp;
       for (i = 1; i < n;i++) {
           temp = array[i];
           for (j = i - 1; j >= 0 && array[j] > temp) {
               array[j+1] = array[j]; // 后移
               j--;
           }
           array[j+1] = temp; 
       }
    }

特性:

- Stable
- O(1) 空间复杂度
- 插入排序平均需要$\frac{N^2}{4}$次比较和$\frac{N^2}{4}$ 次交换。在最坏的情况下需要$\frac{N^2}{2}$ 次比较和交换；在最好的情况下只需要N-1次比较和0次交换。

### 冒泡排序

    void bubble_sort(int *array, int n) {
        int i, j;
        for (i = 0; i < n - 1; i++) {
            for (j = n -1; j > i; j--) {
                if (array[j] < array[j - 1])
                    exch(array[j], array[j - 1]);
            }
        }
    }

可以增加是否交换的标识, 如果内循环没有交换, 表明可以排序, 直接break外循环就好了.

特性:

- Stable
- O(1) 空间复杂度
- O($n^2$) 比较和交换

冒泡排序和插入排序有差不多的性能, 但是对已经排序(nearly sorted)的冒泡排序 O($n^2$) 比较，而插入排序在这个例子只需要O(n). 改进的冒泡, 可以很好利用已经排序的减少比较.

    void bubble_sort(int *array, int n) {
        int flag = n-1, j, k;
        while (flag > 0) {
            k = flag;
            flag = 0;
            for (j = 1; j < k; j++) {
                if (array[j] < array[j - 1]) {
                    exch(array[j], array[j - 1]);
                    flag = j;
                }
            }
        }
    }

refer:


- [http://blog.jobbole.com/79288/](http://blog.jobbole.com/79288/)
- [http://www.acmerblog.com/article-sort-3969.html](http://www.acmerblog.com/article-sort-3969.html)
- [http://blog.csdn.net/morewindows/article/details/6657829](http://blog.csdn.net/morewindows/article/details/6657829)
- [http://www.cricode.com/3212.html](http://www.cricode.com/3212.html)
