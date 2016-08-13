Title: 实现pow(x, n)和sqrt
Tags: algorithm, pown, sqrt
Date: 2014-09-03

### pow(x, n)
>implement pow(x, n)

用二分法先求出n/2次方, 然后求n次方, 嵌套一次函数调用避免复杂的指数正负判断.

    double power(double x, int n) {
        double v;
        if (n == 0) return 1;
        v = power(x, n/2);

        if (n % 2 == 0)
            return v * v;
        else
            return v * v * x;
    }

    double _pow(double x, int n) {
        if (x == 0) return 0;
        return n > 0 ? power(x, n): 1/power(x, -n);
    }


    int pow(double x, int n) { // TODO: check exp negative or positive
         double base = x;
         unsigned int exp = n > 0 ? n: -n; // unsigned
         double result = 1;
         while (exp) {
             if (exp & 0x01)
                result *= base;
             base *= base;
             exp >>= 2;
         }
         return n > 0? result : 1 / result;
    }


### sqrt(x) 

这里给出两种实现方法：一是二分搜索，二是牛顿迭代法。

二分搜索: 对于一个非负数n，它的平方根不会小于大于(n/2+1). 在[0, n/2+1]这个范围内可以进行二分搜索，求出n的平方根。

    int sqrt(int x) {
        long long i = 0;
        long long j = x / 2 + 1;
        while (i <= j)
        {
            long long mid = (i + j) / 2;
            long long sq = mid * mid;
            if (sq == x) return mid;
            else if (sq < x) i = mid + 1;
            else j = mid - 1;
        }
        return j;
    }

牛顿迭代法, 参见 refer[2]

refer:

- [0][http://www.programcreek.com/2012/12/leetcode-powx-n/](http://www.programcreek.com/2012/12/leetcode-powx-n/)
- [1][http://blog.jobbole.com/74468/](http://blog.jobbole.com/74468/)
- [2][http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html](http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html)
