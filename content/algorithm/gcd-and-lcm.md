Title: 最大公约数算法(Greatest Common Divisor) 和最小公倍数(Lowest common mulitiple)
Tags: algorithm, gcd
Date: 2014-09-06

公元前300年左右, 欧几里得(Euclid)就在他的著作<几何原本>中给出了--辗转相除法. 原理是:假设用f(x, y)表示x, y的最大公约数, 取$k=\frac{x/y}, x =ky + b$, 如果一个数能同时整除x,y, 则必能同时被b, y整除. 而能同时被b, y整除则能同时整除x,y, 即b, y的公约数与x, y的公约数相同, 最大公约数也相同, 则有f(x, y) = f(y, x%y) (x >= y >= 0), 如此便把愿问题转化为求两个更小的数的最大公约数, 直到其中一个为0, 剩下的一个就是两者的最大公约数.

## 最大公约数

### 1. 辗转相除法 Euclid

最简单的办法就是直接实现辗转相除法

    # O(log n)
    int gcd(x,y)
    {
        (!y)? x: gcd(y, x%y);
    }


### 2. 把方法1除法变减法

解法一中用到了取模运算, 对大整数, 取模是昂贵的操作. 如果一个数能同时整除x,y, 则必能同时被x-y, y整除. 而能同时被x-y, y整除则能同时整除x,y, 即x-y, y的公约数与x, y的公约数相同, 最大公约数也相同, 则有f(x, y) = f(x-y, y) (x >= y >= 0), 那么就可以不需要取模运算而转化成简单多的减法.

    int gcd(int x, int y) {
        if (x < y) 
            return gcd(y, x);

        if (y == 0) 
            return x;
        else {
            return gcd(x-y, y);
        }
    }

### 解法三 质因数分解法

## 最小公倍数

常用方法:

- 质因数分解
- 短除法
- 公式法, $lcm(a, b) = \frac{a * b}{gcd(a, b)}$

refer:

- [http://www.idomaths.com/zh-Hans/hcflcm.php](http://www.idomaths.com/zh-Hans/hcflcm.php)
- [http://en.wikipedia.org/wiki/Euclidean_algorithm](http://en.wikipedia.org/wiki/Euclidean_algorithm)
