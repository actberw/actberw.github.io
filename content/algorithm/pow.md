Title: 实现pow(x, n)函数
Tags: algorithm
Date: 2014-09-03
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

refer:

- [http://www.programcreek.com/2012/12/leetcode-powx-n/](http://www.programcreek.com/2012/12/leetcode-powx-n/)
