Title: 数组重排问题
Tags: algorithm, data structure, array
Date: 2014-06-12 24:00:00

>给定含有n个元素的整型数组a，其中包括0元素和非0元素，对数组进行排序，要求：
1、排序后所有0元素在前，所有非零元素在后，且非零元素排序前后相对位置不变
2、不能使用额外存储空间

>例子如下
输入 0、3、0、2、1、0、0
输出 0、0、0、0、3、2、1

此排序非传统意义上的排序，因为它要求排序前后非0元素的相对位置不变，或许叫做整理会更恰当一些。我们可以两个指针从后向前遍历整个数组，i找到第一个非0元素时，如果k找到第一个为0元素，则将arr[i]和arr[k]交换, 重复上面的步骤。

    void Arrange(int *arr , int n) {
        int i , k;
        i = k = n - ;
        for(i = n-1 ; i >=0 ; --i)  {
            if(arr[i] != 0)
            {
                if (arr[k] == 0) {
                    arr[k] = arr[i];
                    arr[i] = 0;
                }
            k--;
            }
        }
    }


>一个未排序整数数组，有正负数，重新排列使负数排在正数前面，并且要求不改变原来的正负数之间相对顺序。
比如： input: 1,7,-5,9,-12,15 ，ans: -5,-12,1,7,9,15 。且要求时间复杂度O(N),空间O(1) 。


refer:

- [http://blog.csdn.net/v_july_v/article/details/7329314](http://blog.csdn.net/v_july_v/article/details/7329314)
