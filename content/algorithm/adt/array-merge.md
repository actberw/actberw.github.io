Title: 数组合并问题
Tags: algorithm, data structure, array 
Date: 2014-06-12 23:00:00

### 合并两个有序数组
类似归并排序, 参见[合并链表](/posts/adt/link-list.html)

### 合并两个有序的子序列
>数组al[0,mid-1]和al[mid,num-1]是各自有序的，对数组al[0,num-1]的两个子有序段进行merge，得到al[0,num-1]整体有序。要求空间复杂度为O(1)。注：al[i]元素是支持'<'运算符的。

思路, 设两个有序段位A和B，A在前，B紧接在A后面:

- 找到A的第一个大于B[0]的数A[i]， A[0...i-1]相当于merge后的有效段，在B中找到第一个大于A[i]的数B[j]，
- 对数组A[i...j-1]循环右移j-k位，使A[i...j-1]数组的前面部分有序
- 如此循环merge

实现代码:

    void Reverse(int *a , int begin , int end ) {   //反转
        for(; begin < end; begin++ , end--)
            swap(a[begin] , a[end]);
    }
    void RotateRight(int *a , int begin , int end , int k) {
        int len = end - begin + 1;  //数组的长度
        k %= len;
        Reverse(a , begin , end - k);
        Reverse(a , end - k + 1 , end);
        Reverse(a , begin , end);
    }

    // 将有序数组a[begin...mid] 和 a[mid+1...end] 进行归并排序
    void Merge(int *a , int begin , int end ) {
        int i , j , k;
        i = begin;
        j = 1 + ((begin + end)>>1);    //位运算的优先级比较低，外面需要加一个括号，刚开始忘记添加括号，导致错了很多次
        while(i <= end && j <= end && i<j)
        {
            while(i <= end && a[i] < a[j])
                i++;
            k = j;   //暂时保存指针j的位置
            while(j <= end && a[j] < a[i])
                j++;
            if(j > k)
                RotateRight(a , i , j-1 , j-k);   //数组a[i...j-1]循环右移j-k次
            i += (j-k+1);  //第一个指针往后移动，因为循环右移后，数组a[i....i+j-k]是有序的
        }
    }

    void MergeSort(int *a , int begin , int end ) {
        if(begin == end)
            return ;
        int mid = (begin + end)>>1;
        MergeSort(a , begin , mid);   //递归地将a[begin...mid] 归并为有序的数组
        MergeSort(a , mid+1 , end);   //递归地将a[mid+1...end] 归并为有序的数组
        Merge(a , begin , end);       //将有序数组a[begin...mid] 和 a[mid+1...end] 进行归并排序
    }


refer:

- [http://www.cnblogs.com/legendmaner/archive/2013/04/04/2999769.html](http://www.cnblogs.com/legendmaner/archive/2013/04/04/2999769.html)

