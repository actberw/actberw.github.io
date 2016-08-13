Title: 数组最大值和最小值
Tags: algorithm, data structure, array 
Date: 2014-06-11 18:00:00

### 数组最大值和最小值
分治法, 在N个数中求min和max, 需要分别求出前后N/2的min和max, 然后比较取较小的min, 较大的max, 时间复杂度依然是O(1.5N).

### 快速找出一个数组中的最大数、第二大数

思路: 如果当前元素大于最大数 max，则让第二大数等于原来的最大数 max，再把当前元素的值赋给 max。如果当前的元素大于等于第二大数secondMax的值而小于最大数max的值，则要把当前元素的值赋给 secondMax。

    void GetSecondMaxNumber(int *arr , int n)  
    {  
        int i , max , second_max;  
        max = arr[0];  
        second_max = 0x80000000;  
        for(i = 1 ; i < n ; ++i)  
        {  
            if(arr[i] > max)  
            {  
                second_max = max;  
                max = arr[i];  
            }  
            else  
            {  
                if(arr[i] > second_max)  
                    second_max = arr[i];  
            }  
        }  
        cout<<max<<"  "<<second_max<<endl;  
    }


### 一个int数组，里面数据无任何限制，要求求出所有这样的数a[i]，其左边的数都小于等于它，右边的数都大于等于它。

分析：最原始的方法是检查每一个数 array[i] ，看是否左边的数都小于等于它，右边的数都大于等于它。这样做的话，要找出所有这样的数，时间复杂度为O(N^2)。
其实可以有更简单的方法，我们使用额外数组，比如rightMin[]，来帮我们记录原始数组array[i]右边（包括自己）的最小值。假如原始数组为： array[] = {7, 10, 2, 6, 19, 22, 32}， 那么rightMin[] = {2, 2, 2, 6, 19, 22, 32}. 也就是说，7右边的最小值为2, 2右边的最小值也是2。
有了这样一个额外数组，当我们从头开始遍历原始数组时，我们保存一个当前最大值 max， 如果当前最大值刚好等于rightMin[i]， 那么这个最大值一定满足条件，还是刚才的例子。
第一个值是7，最大值也是7，因为7 不等于 2， 继续，
第二个值是10，最大值变成了10，但是10也不等于2，继续，
第三个值是2，最大值是10，但是10也不等于2，继续，
第四个值是6，最大值是10，但是10不等于6，继续，
第五个值是19，最大值变成了19，而且19也等于当前rightMin[4] = 19, 所以，满足条件。如此继续下去，后面的几个都满足。

    int arr[100] , rightMin[100];
    void smallLarge(int *arr , int *rightMin , int n)  {  
        int i , leftMax;  
        rightMin[n - 1] = arr[n - 1];  
        for(i = n - 2 ; i >= 0 ; --i)  
        {  
            if(arr[i] < rightMin[i+1])  
                rightMin[i] = arr[i];  
            else  
                rightMin[i] = rightMin[i + 1];  
        }  
        leftMax = 0x80000000;  
        for(i = 0 ; i < n ; ++i)  
        {  
            if(arr[i] >= leftMax)  
            {  
                leftMax = arr[i];  
                if(leftMax == rightMin[i])  
                    printf("%d\n",leftMax);  
            }  
        }  
    }

refer:

- [http://blog.csdn.net/zxzxy1988/article/details/8587244](http://blog.csdn.net/zxzxy1988/article/details/8587244)
- [http://blog.csdn.net/cklsoft/article/details/40841637](http://blog.csdn.net/cklsoft/article/details/40841637)
