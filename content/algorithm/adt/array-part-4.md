Title: 数组 part-4
Tags: algorithm, data structure, array 
Date: 2014-06-11 18:00:00

### 数组最大值和最小值
分治法, 在N个数中求min和max, 需要分别求出前后N/2的min和max, 然后比较取较小的min, 较大的max, 时间复杂度依然是O(1.5N).

### 第K大数
K次冒泡就可以找到第K大的数，时间复杂度为O(kn)。快排是对冒泡的改进，这里我们也可以使用快排进行算法改进。步骤如下:

- 随机选择一个支点
- 将比支点大的数，放到数组左边；将比支点小的数放到数组右边；将支点放到中间(属于左部分)
- 设左部分的长度为L

        当K < L时，递归地在左部分找第K大的数
        当K > L时，递归地在有部分中找第(K - L)大的数
        当K = L时，返回左右两部分的分割点（即原来的支点），就是要求的第K大的数


代码:

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
            return findk(array, pivot + 1, r, k - llen);
        else if (k < llen)
            return findk(array, l, pivot, k);
        else
            return array[pivot];
    }


refer:

- [http://coolshell.cn/articles/8138.html](http://coolshell.cn/articles/8138.html)
- [http://xfhnever.github.io/blog/2014/10/21/algorithm-findk/](http://xfhnever.github.io/blog/2014/10/21/algorithm-findk/)
### 最大的K个数
最简单的就是冒泡O(N * K), 也可以直接转化为求第K大数, 然后遍历数组打印所有比第K个数大的元素, 或者用求第K大数的快排方式.
或者用最小堆.

### median of two sorted array
利用类似merge(合并两个有序数组)的操作找到中位数，利用两个分别指向A和B数组头的指针去遍历数组，然后统计元素个数，直到找到中位数，此时算法复杂度为O(n). 或者参照第K大数

refer:

- [http://blog.csdn.net/zxzxy1988/article/details/8587244](http://blog.csdn.net/zxzxy1988/article/details/8587244)

