Title: 子数组
Tags: algorithm, data structure, array 
Date: 2014-06-11 19:00:00

### 子数组之和最大值

设最大的一段数组为(A[i], ..., A[j]), 跟A[0]的关系是:

- i=j=0 元素A[0]本身是最大和
- 0=i<j 从A[0]开始的最大和
- 0<i  跟A[0] 没有关系

通过动态规划来解决.

    int max(int x, int y) {
        return x > y ? x : y;
    }

    int find_max_sum(int *array, int n) {
        int max_curr, max_sum, i; //max_curr 就是上面的 前两个
        max_curr = max_sum = array[0];
        for (i = 1; i < n; i++) {
            max_curr = max(array[i], array[i] + max_curr);
            max_sum = max(max_curr, max_sum);
        }
        return max_sum;
    }

代码也可以简化为:

    int find_max_sum(int *array, int n) {
        int max_curr, max_sum, i;
        max_curr = max_sum = array[0];
        for (i = 1; i < n; i++) {
            if (max_curr < 0)
            ¦   max_curr = 0; // 不能处理全部是负数情况
            max_curr += array[i];

            if (max_curr > max_sum)
            ¦   max_sum = max_curr;
        }
        return max_sum;
    }

二维数组参见[子数组之和得最大值](/posts/algorithm/matrix.html)

### 子数组最大乘积
> Find the contiguous subarray within an array (containing at least one number) which has the largest product.

> For example, given the array [2,3,-2,4] ,

> the contiguous subarray  [2,3] has the largest product =  .

分析: 首先，任何一个数字和0相乘得到的都是0；另外，不考虑0的情况下，因为数字都是整数，所以乘积的绝对值是不会变小的；再次，负负得正。 思路跟最大和一样, 不过因为多了个负负得正所以需要保留前段最小值.

    int find_max_product(int *array, int n) {
        int max_curr, min_curr, max_product, i, tmp;
        max_curr = min_curr = 1;
        max_product = INT_MIN;
        for (i = 0; i < n; i++) {
            if (array[i] > 0) {
            ¦   max_curr *= array[i];
            ¦   min_curr = min(min_curr * array[i], 1);

            } else if (array[i] == 0) {
            ¦   max_curr = min_curr = 1;
            } else { // < 0
            ¦   tmp = max_curr;
            ¦   max_curr = max(min_curr * array[i], 1);
            ¦   min_curr = tmp * array[i];
            }

            if (max_curr > max_product)
            ¦   max_product = max_curr;
        }
        return max_product;
    }

### 最长递增子序列

可以用quicksort + LCS, ，因为LIS是单调递增的性质，所以任意一个LIS一定跟排序后的序列有LCS，并且就是LIS本身。
扩展:

- 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的


### Longest subarray with equal number of ones and zeros
>Given an array containing only 0s and 1s, find the largest subarray which contain equal no of 0s and 1s. Expected time complexity is O(n).

最简单得实现就是把0当-1, 计算从i 到j得sum, 如果sum ==0 , 比较size和max_size, 时间复杂度是$O(n^2)$.

    int find_sub_array(int arr[], int n) {
        int sum = 0;
        int max_size = -1, startindex;
     
        // Pick a starting point as i
        for (int i = 0; i < n-1; i++)
        {
            sum = (arr[i] == 0)? -1 : 1;
     
            // Consider all subarrays starting from i
            for (int j = i+1; j < n; j++)
            {
                (arr[j] == 0)? sum += -1: sum += 1;
     
                if(sum == 0 && max_size < j-i+1)
                {
                    max_size = j - i + 1;
                    startindex = i;
                }
            }
        }
        if ( max_size == -1 )
            printf("No such subarray");
        else
            printf("%d to %d", startindex, startindex+max_size-1);
     
        return max_size;
    }

### 最长公共子序列(Longest-Common-Subsequence)

refer:

- [http://blog.csdn.net/v_JULY_v/article/details/6419466](http://blog.csdn.net/v_JULY_v/article/details/6419466)
- [http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/](http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
- [http://www.geeksforgeeks.org/maximum-product-subarray/](http://www.geeksforgeeks.org/maximum-product-subarray/)
- [http://shepherdyuan.wordpress.com/2014/07/23/linkedin-maximum-sumproduct-subarray/](http://shepherdyuan.wordpress.com/2014/07/23/linkedin-maximum-sumproduct-subarray/)
- [http://www.ahathinking.com/archives/117.html](http://www.ahathinking.com/archives/117.html)
- [http://blog.csdn.net/zhanxinhang/article/details/6710285](http://blog.csdn.net/zhanxinhang/article/details/6710285)
