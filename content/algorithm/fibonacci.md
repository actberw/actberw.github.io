Title: 斐波纳契数列
Tags: algorithm
Date: 2014-06-11 19:00:00

>问题描述：Fibonacci数（Fibonacci Number）的定义是：$F_n = F_{n - 1} + F_{n - 2}$，并且$F_0$ = 0，$F_1$ = 1。对于任意指定的整数n（n ≥ 0），计算$F_n$的精确值，并分析算法的时间、空间复杂度。

有下面几种解法.

### 递归法   

根据Fibonacci的递推公式，对于输入的n，直接递归地调用相同的函数分别求出$F_{n - 1}$和$F_{n - 2}$，二者相加就是结果。递归的终止点就是递推方程的初值，即n取0或1的时候。

    int fibonacii(int n) {
        if (n <= 1) return n;
        return fibonacii(n - 1) + fibonacii(n - 2);
    }
时间复杂度是O($2^n$)(实际上是黄金分割$\frac{1+\sqrt{5}}{2}$)，空间复杂度是O(n)。  
这个算法的时间复杂度有着跟Fibonacci类似的递推方程：$T_n = T_{n - 1} + T_{n - 2} + O(1)$, 具体解法见下图:

 - 先用特征方程求出Fibonacci通项
![Fibonacci-recursion-complexity](/img/fibonacci-complexity.png)
 - 设 $K_n$为计算Fn所需要的加法次数, $K_n$ = $K_{n-1}$ + $K_{n-2}$ + 1, $K_0$ = 0, $K_1$ = 0, $K_2$ = 1, 则有$K_n$ + 1 = $K_{n-1}$ + 1 + $K_{n-2}$ + 1, $K_n$ + 1 是斐波那契数列, $K_n$ = fibonacci(n+1) - 1, 所以O(fibonacci(n+1) - 1) = O(fibonacci(n+1))

### 递推法  
虽然只是一字之差，但递推法的复杂度要小的多。这个方法就是按照递推方程，从n = 0和n = 1开始，逐个求出所有小于n的Fibonacci数，最后就可以算出F(n)。由于每次计算值需要用到前两个Fibonacci数，更小的数就可以丢弃了，可以将空间复杂度降到最低。算法如下：

    int fibonacii2(int n) {
        int x = 0, y = 1, t;
        if (n <= 1) return n;
        for(; n >= 2; n--) {
            t = y;
            y = y + x;
            x = t;
        }
        return y;
    }
显然时间复杂度是O(n)，空间复杂度是O(1)。  

比较一下递归法和递推法，二者都用了分治的思想——把目标问题拆为若干个小问题，利用小问题的解得到目标问题的解。二者的区别实际上就是普通分治算法和动态规划的区别。

### 矩阵法  

我们把Fibonacci数列中相邻的两项：$F_n$和$F_{n - 1}$写成一个2 * 1的矩阵，然后对其进行变形


### 有关Fibonacci问题

1. 在递归计算$F_n$的时候，需要对较小的$F_{n-1}$，$F_{n-2}$，…, $F_l$, $F_0$精确计算多少次?  
\begin{eqnarray\*} 
F_n = F_{n-1} + F_{n-2}  
   = (F_{n-2} + F_{n-3}) + (F_{n-3} + F_{n-4})
\end{eqnarray\*}

设$K_{n.m}$ 表示计算$F_n$时用到$F_m$的次数, 则有$K_{n.n-3} = K_{n.n-2} + K_{n.n-1}$ 是Fibonacci数列, 其中$K_{n.n-1}$ = 1 = fibonacci(2), $K_{n.n-2}$ = 2 = fibonacci(3),  $K_{n.0}$ = fibonacci(n+1)

refer:

- [http://www.gocalf.com/blog/calc-fibonacci.html](http://www.gocalf.com/blog/calc-fibonacci.html)
- [http://061251008.blog.163.com/blog/static/240841720123157186395/](http://061251008.blog.163.com/blog/static/240841720123157186395/)
