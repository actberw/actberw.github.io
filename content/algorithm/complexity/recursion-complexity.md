Title: 递归算法的复杂度分析
Tags: algorithm analysis
Date: 2014-06-07 17:00:00

在算法分析中，当一个算法中包含递归调用时，其时间复杂度的分析会转化为一个递归方程求解。实际上，这个问题是数学上求解渐近阶的问题，而递归方程的形式多种多样，其求解方法也是不一而足，比较常用的有以下四种方法:

### 代入法(Substitution Method)  

代入法的基本步骤是先推测递归方程的显式解，然后用数学归纳法来验证该解是否合理。

### Recurrence Tree Method

For example consider the recurrence relation 
$T(n) = T(\frac{n}{4}) + T(\frac{n}{2}) + cn^2$

           cn2
         /      \
     T(n/4)     T(n/2)

If we further break down the expression $T(\frac{n}{4})$ and $T(\frac{n}{2})$, 
we get following recursion tree.

                  cn2
              /         \      
           c(n2)/16       c(n2)/4
          /      \          /     \
      T(n/16)     T(n/8)  T(n/8)    T(n/4) 
Breaking down further gives us following

                     cn2
                /            \      
           c(n2)/16          c(n2)/4
           /      \            /      \
    c(n2)/256   c(n2)/64  c(n2)/64    c(n2)/16
     /    \      /    \    /    \       /    \  

To know the value of T(n), we need to calculate sum of tree 
nodes level by level. If we sum the above tree level by level, 
we get the following series
$T(n)  = c(n^2 + \frac{5}{16}(n^2) + \frac{25}{256}(n^2)) + ....$
The above series is geometrical progression with ratio $\frac{5}{16}$.

To get an upper bound, we can sum the infinite series. 

We get the sum as $(n^2)/(1 - \frac{5}{16})$ which is $O(n^2)$

### 公式法(Master Method)  

设常数a >= 1，b > 1，f(n)为函数，T(n)为非负整数，T(n) = a T(n / b) + f(n)，则有:  

- 若f(n)=O($n^{log_{b}a−ε}$),ε>0 ，那么T(n)=Θ($nlog_{b}a$) 。  
- 若f(n)=Θ($n^{log_{b}a}$) ，那么T(n)=Θ($n^{log_{b}a}logn$) 。  
- 若f(n)=Ω($n^{log_{b}a+ε}$),ε>0 ，并且对于某个常数c < 1和充分大的n有af(n/b)≤cf(n) ，那么T(n)=Θ(f(n)) 。  

比如常见的二分查找算法，时间复杂度的递推方程为T(n) = T(n / 2) + θ(1)，显然有nlogba=n0=Θ(1) ，满足Master定理第二条，可以得到其时间复杂度为T(n) = θ(log n)  

### 迭代法(Iteration Method)  

  迭代法的基本步骤是迭代地展开递归方程的右端，使之成为一个非递归的和式，然后通过对和式的估计来达到对方程左端即方程的解的估计。适用于: Tn = T(n-1 +N , Tn = Tn/2 + 1,   T(n) = 3T(n/4) + O(n), 对于Tn = 2Tn/2 +1, Tn = 2Tn/2 + n, 直接令n = $2^k$ 迭代

### 母函数法  

参见参考[2],[4]和[母函数介绍](/mu-han-shu-generating-function.html)

### 差分方程法(Difference Formula Method)  
  参见参考[4]

refer:

- [0][http://www.geeksforgeeks.org/analysis-algorithm-set-4-master-method-solving-recurrences/](http://www.geeksforgeeks.org/analysis-algorithm-set-4-master-method-solving-recurrences/)
- [1][http://www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html](http://www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html)
- [2][http://www.cnblogs.com/python27/archive/2011/12/09/2282486.html](http://www.cnblogs.com/python27/archive/2011/12/09/2282486.html)
- [3][http://blog.csdn.net/metasearch/article/details/4428865](http://blog.csdn.net/metasearch/article/details/4428865)
- [4][http://wenku.baidu.com/view/92d328ea551810a6f52486db.html](http://wenku.baidu.com/view/92d328ea551810a6f52486db.html)
- [5][http://www.acmerblog.com/analysis-recurrences-5084.html](http://www.acmerblog.com/analysis-recurrences-5084.html)
