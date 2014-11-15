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

### Maximum subarray with all 1’s.
可以利用求直方图最大长方形(largest rectangle in histogram)得问题求解.

### Maximum size square sub-matrix with all 1s
用动态规划解决:

Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j] represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost and bottommost entry in sub-matrix.

- Construct a sum matrix S[R][C] for the given M[R][C].
     a) Copy first row and first columns as it is from M[][] to S[][]
     b) For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1 //understand
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
- Find the maximum entry in S[R][C]
- Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]

### four borders
>Imagine you have a square matrix, where each cell is filled with either black or white. Design an algorithm to find the maximum subsquare such that all four borders are filled with black pixels. 

暴力法，从左到右，从上到下遍历格子，将它作为子正方形左上角的点。 固定了子正方形左上角的点，我们只需要知道边长，就能把子正方形确定下来。 我们按边长从大到小开始，去检查每一个子正方形的四条边是否都为黑色格子。 如果是，则记下当前最大的边长值。将子正方形左上角的点移动到下一行(即向下移动一格)， 进入下一轮循环。

    SubSquare FindSubSquare(int n){
        int max_size = 0; //最大边长
        int col = 0;
        SubSquare sq;
        while(n-col > max_size){
            for(int row=0; row<n; ++row){
                int size = n - max(row, col);
                while(size > max_size){
                    if(IsSquare(row, col, size)){
                        max_size = size;
                        sq.row = row;
                        sq.col = col;
                        sq.size = size;
                        break;
                    }
                    --size;
                }
            }
            ++col;
        }
        return sq;
    }


### 打印螺旋矩阵

我们可以直接根据螺旋的过程来实现打印，从第一个元素开始，向右走N步，然后转向下，需要走的步数则为N-1，然后转向右，需要走的步数依然为N-1,最后往上走，需要走N-2步。这样就螺旋的打印完了最外围一圈，接着是往里的一圈，又重复这样的过程。

    void printMatrix(int **matrix, int dimension){
        if(matrix == NULL || dimension <= 0)
            return;
        int i = 0, j = 0, steps = dimension;
        int circle = steps >> 1;
        int num = 1, k = 0;
        while(k < circle){
            i = j = k;
            while(j < steps){ // fisrt print steps-j elements
                matrix[i][j++] = num++;
            }
            --j;

            while(i < steps - 1){ // 0,1,2,3
                matrix[++i][j] = num++;
            }

            while(j > k){
                matrix[i][--j] = num++;
            }

            while(i > k+1){
                matrix[--i][j] = num++;
            }
            ++k;
            --steps;
        }
        if(dimension & 0x1 == 1)
            matrix[circle][circle] = num;
    }

### 按顺序打印已排序得矩阵 
>Given an n x n matrix, where every row and column is sorted in non-decreasing order. Print all elements of matrix in sorted order.


refer:

- [http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/](http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/)
- [http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html](http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html)
- [http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/](http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/)
- [最大矩阵问题的一些变种](http://wansishuang.appspot.com/?p=38002)
- [http://zh.wikipedia.org/wiki/%E7%9F%A9%E9%98%B5%E6%8C%87%E6%95%B0](http://zh.wikipedia.org/wiki/%E7%9F%A9%E9%98%B5%E6%8C%87%E6%95%B0)
- [http://www.zhihu.com/question/19706331](http://www.zhihu.com/question/19706331)
- [http://www.ituring.com.cn/article/17978](http://www.ituring.com.cn/article/17978)
- [http://www.zhihu.com/question/22854639](http://www.zhihu.com/question/22854639)
- [http://www.hawstein.com/posts/20.11.html](http://www.hawstein.com/posts/20.11.html)
- [http://www.geeksforgeeks.org/print-elements-sorted-order-row-column-wise-sorted-matrix/](http://www.geeksforgeeks.org/print-elements-sorted-order-row-column-wise-sorted-matrix/)
- [http://www.ituring.com.cn/article/51520](http://www.ituring.com.cn/article/51520)
