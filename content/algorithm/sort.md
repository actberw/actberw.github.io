Title:基本排序算法
Tags: algorithm, sort

1. 分类
    - 插入排序: 直接插入排序，Shell排序
    - 选择排序: 直接选择排序，堆排序
    - 冒泡排序: 冒泡排序，快速排序
    - 归并排序，基数排序，桶排序

A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, etc. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

计数排序
插入排序
void Insertsort(int a[], int n)
{
    int i, j;
    for (i = 1; i < n; i++)
        int temp = a[i];
        for (j = i - 1; j >= 0 && a[j] > temp; j--)
            a[j + 1] = a[j];
        a[j + 1] = temp;
}

refer:

http://www.cnblogs.com/kkun/archive/2011/11/23/2260299.html

- [http://www.acmerblog.com/article-sort-3969.html](http://www.acmerblog.com/article-sort-3969.html)
- [http://www.acmerblog.com/sort-algorithm1-3374.html](http://www.acmerblog.com/sort-algorithm1-3374.html)
- [http://www.acmerblog.com/quick-sort-5789.html](http://www.acmerblog.com/quick-sort-5789.html)
