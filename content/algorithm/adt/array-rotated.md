Title: 旋转数组
Tags: algorithm, data structure, array 
Date: 2014-06-11 16:00:00

### 旋转排序数组(Rotated array)
>Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

思路:我们将数组中需要选择的部分分为A和B，我们要做的就是先将A倒置，再将B导致。最后将整个数组倒置，就能得到我们想要的结果。 交换连续内存思想. 参见refer[2]

### 旋转数组查找
>Suppose a sorted array is rotated at some pivot unknown to you beforehand (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).You are given a target value to search. If found in the array return its index, otherwise return -1.
Search in Rotated Sorted Array, 

这道题目就是用二分查找的思路来解决, 中间用到了旋转数组的一些特性。以题目中的旋转数组为例, {3,4,5,1,2}, 我们可以有序数组经过旋转以后被分割为两段有序的数组, 比如此处被分为{3,4,5}{1,2}这样两个数组, 并且前半段数组中的数字肯定大于等于后半段的数组。我们找中间元素, 让其跟首尾元素素比较, 确定范围.

    int search(int *array, int len, int target) {
        int middle = 0;
        int left = 0, right = len - 1;
        if (len == 0) return -1;

        while(left <= right) {
            middle = left + (right - left) / 2;
            if (array[middle] == target) return middle;
            if (array[right] == target) return right;
            if (array[left] == target) return left;

            if (array[middle] < array[right]) {
                if (array[middle] < target && target < array[right]) {
                    left = middle + 1;
                } else { 
                    right = middle - 1;
                }
            } else {
                if (array[middle] > target && target > array[right]) {
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
            }
        }

        return -1;
    }

扩展: 求最小值(如果有重复当array[mid] == array[r]时left++), 同样也是用二分查找, 参见refer[1].

refer:

- [http://blog.leanote.com/post/qqxufo/Rotate-Array-Leetcode-No.189%EF%BC%88%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%EF%BC%89](http://blog.leanote.com/post/qqxufo/Rotate-Array-Leetcode-No.189%EF%BC%88%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%EF%BC%89)
- [0][http://segmentfault.com/blog/code/1190000000457723](http://segmentfault.com/blog/code/1190000000457723)
- [1][http://www.cnblogs.com/xwdreamer/archive/2012/05/07/2487520.html](http://www.cnblogs.com/xwdreamer/archive/2012/05/07/2487520.html)

- [2][http://www.ahathinking.com/archives/16.html](http://www.ahathinking.com/archives/16.html)
