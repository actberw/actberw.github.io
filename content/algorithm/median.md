Title: 中位数
Tags: algorithm, median, heap
Date: 2014-06-12 18:00:00

对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的平均数作为中位数。

求数组中位数的方法:

- 排序
- find k-th
- 双堆

前两种方法不太适合于数据动态变更中位数.

### 双堆方法
算法如下:

- 初始化的时候设置两个变量分别记录两个堆【左堆和右堆】的元素的个数。

- 取第一个元素【d[0]】作为初始中位数m。

- 循环后面的每一个元素，如果比m大，则插入到右堆(小堆)，如果比m小，则插入到左堆(大堆)。

- 如果此时最小堆和最大堆的元素个数的差值>=2 ，则将m加入到元素个数少的堆中，然后从元素个数多的堆将根节点赋值到m，最后重建两个最大堆和最小堆，返回到第三步。

此时，如果想要知道当前的中位数，输出m即可。

### median of two sorted array
>There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

利用类似merge(合并两个有序数组)的操作找到中位数，利用两个分别指向A和B数组头的指针去遍历数组，然后统计元素个数，直到找到中位数，此时算法复杂度为O(m + n). 或者参照[k-th Smallest Element in the Union of Two Sorted Arrays](/posts/adt/find-kth.html). 

    // 只适合m == n 的情况 
    double getMedian(int arr1[],int arr2[], int n){
        int i=0,j=0; //分别是 arr1， arr2的当前下标
        int m1=-1,m2=-1; //保存两个中位数. 由于是2n个，肯定有两个中位数
        for(int cnt=0; cnt<=n; cnt++){
            if( (i<n && (arr1[i] < arr2[j]) || j >= n ){
                m1 = m2;
                m2 = arr1[i++];
            }else{
                m1 = m2;
                m2 = arr2[j++];
            }
        }
        return (m1+m2)/2.0;
    }

分治法: By comparing the medians of two arrays (也是假设m == n)
算法如下:

    1) Calculate the medians m1 and m2 of the input arrays ar1[] 
       and ar2[] respectively.
    2) If m1 and m2 both are equal then we are done.
         return m1 (or m2)
    3) If m1 is greater than m2, then median is present in one 
       of the below two subarrays.
        a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
        b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
    4) If m2 is greater than m1, then median is present in one    
       of the below two subarrays.
       a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
       b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
    5) Repeat the above process until size of both the subarrays 
       becomes 2.
    6) If size of the two arrays is 2 then use below formula to get 
      the median.
        Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2

代码:

    int getMedian(int ar1[], int ar2[], int n) {
        int m1; /* For median of ar1 */
        int m2; /* For median of ar2 */
     
        /* return -1  for invalid input */
        if (n <= 0)
            return -1;
     
        if (n == 1)
            return (ar1[0] + ar2[0])/2;
     
        if (n == 2)
            return (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1])) / 2;
     
        m1 = median(ar1, n); /* get the median of the first array */
        m2 = median(ar2, n); /* get the median of the second array */
     
        /* If medians are equal then return either m1 or m2 */
        if (m1 == m2)
            return m1;
     
         /* if m1 < m2 then median must exist in ar1[m1....] and ar2[....m2] */
        if (m1 < m2) {
            if (n % 2 == 0)
                return getMedian(ar1 + n/2 - 1, ar2, n - n/2 +1);
            else
                return getMedian(ar1 + n/2, ar2, n - n/2);
        }
     
        /* if m1 > m2 then median must exist in ar1[....m1] and ar2[m2...] */
        else {
            if (n % 2 == 0)
                return getMedian(ar2 + n/2 - 1, ar1, n - n/2 + 1);
            else
                return getMedian(ar2 + n/2, ar1, n - n/2);
        }
    }

当 m != n 时

About this problem, I think maybe we could still use the MIT solution with a small modification. When n+m is odd, then it’s fine; otherwise, it actually returns the greater one of the two middle numbers and the smaller one will be max(B[j], A[i-1]). My code is here. Looking forward for your comments.

    double findMedian(int A[], int B[], int l, int r, int nA, int nB) {
        if (l > r) return findMedian(B, A, max(0, (nA+nB)/2-nA), min(nB, (nA+nB)/2), nB, nA);
        int i = (l+r)/2;
        int j = (nA+nB)/2 – i – 1;
        if (j ≥ 0 && A[i] < B[j]) 
            return findMedian(A, B, i+1, r, nA, nB);
        else if (j < nB-1 && A[i] > B[j+1]) 
            return findMedian(A, B, l, i-1, nA, nB);
        else { // B[j] <= A[i] <= B[j+1]
            if ( (nA+nB)%2 == 1 ) 
                return A[i];
            else if (i > 0) 
                return (A[i]+max(B[j], A[i-1]))/2.0;
            else 
                return (A[i]+B[j])/2.0;
        }
    }

也可以用[find-Kth](/posts/adt/top-k.html)来解决如果总数是奇数个调一次find-Kth($\frac{m + n}{2}$), 偶数的话$\frac{find-Kth(\frac{m + n}{2}) + find-Kth(\frac{m + n}{2} + 1}{2}$ , 参见refer[4]

refer:

- [0][http://www.cnphp6.com/archives/41479](http://www.cnphp6.com/archives/41479)
- [1][http://www.acmerblog.com/median-of-two-sorted-arrays-5967.html](http://www.acmerblog.com/median-of-two-sorted-arrays-5967.html)
- [2][http://www2.myoops.org/course_material/mit/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/30C68118-E436-4FE3-8C79-6BAFBB07D935/0/ps9sol.pdf](http://www2.myoops.org/course_material/mit/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/30C68118-E436-4FE3-8C79-6BAFBB07D935/0/ps9sol.pdf)
- [3][http://leetcode.com/2011/03/median-of-two-sorted-arrays.html](http://leetcode.com/2011/03/median-of-two-sorted-arrays.html)
- [4][http://blog.csdn.net/yutianzuijin/article/details/11499917](http://blog.csdn.net/yutianzuijin/article/details/11499917)
