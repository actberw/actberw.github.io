Title: 矩阵
Tags: algorithm, matrix
Date: 2014-06-12 12:00:00

### Search in a row wise and column wise sorted matrix
> Given an n x n matrix, where every row and column is sorted in increasing order. Given a number x, how to decide whether this x is in the matrix. The designed algorithm should have linear time complexity.

Solution:
- Start with top right element
- Loop: compare this element e with x
    - if they are equal then return its position
    - e < x then move it to down (if out of bound of matrix then break return false)
    - e > x then move it to left (if out of bound of matrix then break return false)
    - repeat..

代码:

    int search(int mat[4][4], int n, int x)
    {
       int i = 0, j = n-1;  //set indexes for top right element
       while ( i < n && j >= 0 )
       {
          if ( mat[i][j] == x )
          {
             printf("\n Found at %d, %d", i, j);
             return 1;
          }
          if ( mat[i][j] > x )
            j--;
          else //  if mat[i][j] < x
            i++;
       }
     
       printf("\n Element not found");
       return 0;  // if ( i==n || j== -1 )
    }

### 子数组之和得最大值
可以转化为一维得求[最大值](/posts/adt/array-part-5.html), 把a,c 行之间相同列看成整体.

### 求一个矩阵中最大的二维矩阵(元素和最大)
> 如
1 2 0 3 4
2 3 4 5 1
1 1 5 3 0
中最大的是:
4 5
5 3
要求:(1)写出算法;(2)分析时间复杂度;(3)用C写出关键代码


    int max_submatrix(int **array, int n) {
        int i, j, sum, max_sum, last_sum=0;
        for (i=0; i < n; i++) {
            last_sum = array[i][0] + array[i+1][0];
            for (j = 0; j < n; j++) {
                sum = last_sum;    // sum = array[i][j] + array[i+1][j] + array[i][j+1] + array[i+1][j+1]; 
                                   // 用last_sum 减少一次加法多了两次赋值
                last_sum = array[i][j+1] + array[i+1][j+1];
                sum += last_sum;
                if (sum > max_sum)
                    max_sum = sum;
            } 
        }
        return max_sum;
    }

refer:

- [http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/](http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/)
- [http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html](http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html)
- [http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/](http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/)
- [http://zh.wikipedia.org/wiki/%E7%9F%A9%E9%98%B5%E6%8C%87%E6%95%B0](http://zh.wikipedia.org/wiki/%E7%9F%A9%E9%98%B5%E6%8C%87%E6%95%B0)
- [http://www.zhihu.com/question/19706331](http://www.zhihu.com/question/19706331)
- [http://www.ituring.com.cn/article/17978](http://www.ituring.com.cn/article/17978)
- [http://www.zhihu.com/question/22854639](http://www.zhihu.com/question/22854639)
