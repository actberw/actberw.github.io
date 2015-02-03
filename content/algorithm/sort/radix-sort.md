Title:基数排序
Tags: algorithm, sort
Date: 2014-07-02 16:00:00

在计算机科学中，排序是一门基础的算法技术，许多算法都要以此作为基础，不同的排序算法有着不同的时间开销和空间开销。排序算法有非常多种，如我们最常用的快速排序和堆排序等算法，这些算法需要对序列中的数据进行比较，因为被称为基于比较的排序。

基于比较的排序算法是不能突破O(NlogN)的。简单证明如下：

N个数有N!个可能的排列情况，也就是说基于比较的排序算法的判定树有N!个叶子结点，比较次数至少为log(N!)=O(NlogN)(斯特林公式)。

本文着重介绍三种线性的非基于比较的排序算法：计数排序、桶排序与基数排序。

### 计数排序 

数排序(Counting Sort)基本思想时: 对于每一个输入元素x, 确定小于x的元素个数. 假设我们有一个待排序的整数序列A，$x\in{[0, K]}$。建立一个长度为K的线性表C，用来记录不大于每个值的元素的个数。

算法步骤:

- 扫描序列A，以A中的每个元素的值为索引，把出现的个数填入C中。此时C[i]可以表示A中值为i的元素的个数。
- 对于C从头开始累加，使C[i]<-C[i]+C[i-1]。这样，C[i]就表示A中值不大于i的元素的个数。

        int ctsort(int *data, int size, int k)  {  // k: 数组中元素数组最大值+1 （这个需要+1） 
            int * counts = NULL,/*计数数组*/  
                * temp = NULL; /*保存排序后的数组*/  
            int i = 0;  
          
            if ((counts = (int *) malloc( k * sizeof(int))) == NULL)  
                return -1;  
            if ((temp = (int *) malloc( size * sizeof(int))) == NULL)  
                return -1;  
          
            for (i = 0; i < k; i ++)  // or memset
                counts[i] = 0; 

            for(i = 0; i < size; i++)  
                counts[data[i]] += 1;  

            for (i = 1; i < k; i++)  
                counts[i] += counts[i - 1];  

            for (i = size -1; i >= 0; i --){  
                temp[counts[data[i]] - 1] = data[i];  
                counts[data[i]] -= 1;  
            }  
              
          
            memcpy(data,temp,size * sizeof(int));  
            free(counts);  
            free(temp);  
          
            return 0;  
        }

计数排序的时间复杂度为O(N+K)，空间复杂度为O(N+K) (K 为最大数)

### 桶排序

算法步骤:
- 创建一个桶数组 
- 将待排序的一组数，分档规入这些子桶
- 将桶中的数据进行排序
- 将各个桶中的数据有序的合并起来

        void bucketSort(float arr[], int n) {
            vector<float> b[n];
            
            for (int i=0; i<n; i++)
            {
               int bi = n*arr[i]; // Index in bucket
               b[bi].push_back(arr[i]);
            }
         
            for (int i=0; i<n; i++)
               sort(b[i].begin(), b[i].end());
         
            int index = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < b[i].size(); j++)
                  arr[index++] = b[i][j];
        }

### 基数排序

从整体上来说，计数排序，桶排序都是非基于比较的排序算法，而其时间复杂度依赖于数据的范围，桶排序还依赖于空间的开销和数据的分布。而基数排序是一种对多元组排序的有效方法，具体实现要用到计数排序或桶排序。

相对于快速排序、堆排序等基于比较的排序算法，计数排序、桶排序和基数排序限制较多，不如快速排序、堆排序等算法灵活性好。但反过来讲，这三种线性排序算法之所以能够达到线性时间，是因为充分利用了待排序数据的特性，如果生硬得使用快速排序、堆排序等算法，就相当于浪费了这些特性，因而达不到更高的效率。

基本思想: 将整数按位数切割成不同的数字，然后按每个位数分别比较, 可以LSD(Least sgnificant digital)或MSD(Most sgnificant digital), 按位比较可以借助计数或桶排序.

    void radix_sort(int *arr, int len) {
        int max_val, tmp[len], count[BASE], exp = 1, i;
        max_val = max_arr(arr, len);  // 数组最大元素
        while (max_val / exp) {
            memset(count, 0, BASE * sizeof(int));
            for (i = 0 ; i < len; i++) {
            ¦   count[(arr[i] / exp) % BASE] += 1;
            }

            for (i = 1; i < BASE; i++) {
            ¦   count[i] += count[i-1];
            }

            for (i = len - 1; i >= 0; i--) {
            ¦   tmp[--count[(arr[i] / exp) % BASE]] = arr[i];
            }
            memcpy(arr, tmp, len * sizeof(int));
            exp *= BASE;
        }
    }

时间复杂度为O(nk), k为数字的位数, 空间复杂度为O(n).

refer:

- [https://www.byvoid.com/blog/sort-radix](https://www.byvoid.com/blog/sort-radix)
- [http://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F](http://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F)
- [http://www.geeksforgeeks.org/bucket-sort-2/](http://www.geeksforgeeks.org/bucket-sort-2/)
- [http://bubkoo.com/2014/01/15/sort-algorithm/bucket-sort/](http://bubkoo.com/2014/01/15/sort-algorithm/bucket-sort/)
