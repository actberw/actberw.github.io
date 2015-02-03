Title: 希尓排序
Tags: algorithm, sort
Date: 2014-07-02 13:00:00

### 希尓排序
希尔排序也称之为递减增量排序，他是对插入排序的改进。在第二部插入排序中，我们知道，插入排序对于近似已排好序的序列来说，效率很高，可以达到线性排序的效率。但是插入排序效率也是比较低的，他一次只能将数据向前移一位.

希尔排序的关键在于步长递减序列的确定，任何递减至1步长的序列都可以，目前已知的:

- Shell’s 序列: N/2 , N/4 , …, 1 (重复除以2);
- Hibbard’s 序列: 1, 3, 7, …, 2k - 1 ;
- Knuth’s 序列: 1, 4, 13, …, (3k - 1) / 2 ;该序列是本文代码中使用的序列。

下面是代码以Knuth’s 序列

    void shell_sort(int *array, int n){
        int gap = 1, i, j, tmp;
        while (gap < n / 3) gap = 3gap + 1 ;
        for (;gap >= 1; gap /= 3) {

            for (i = gap; i < n; i += 1) {
                temp = a[i]
                for (j = i - gap; j >= 0 && a[j] > temp; j -= gap) {
                    a[j + gap] = a[j];
                }
                a[j + gap] = temp;
            }
        }
    }

希尓排序的时间复杂度依赖于增量递减序列, 目前最好的是 $O(n\lg^{2}n)$, 使用Hibbard’s 递减步长序列的时间复杂度为$O(N^\frac{3}{2})$.

特点:

- 不稳定排序
- O(1) 空间复杂度, O($n^{\frac{3}{2}}$)时间复杂度

refer:

- [http://blog.jobbole.com/79288/](http://blog.jobbole.com/79288/)
