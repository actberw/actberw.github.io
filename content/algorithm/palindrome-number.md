Title: 回文数
Tags: algorithm, c
Date: 2014-09-05
>Determine whether an integer is a palindrome. Do this without extra space

可以直接将数字反转判断两个数是否相等,  但是可能带来一个问题就是反转的时候整数溢出.
对于任意n位的数字，取n=5，数字95349为例

    95349 % 10 => 9
    95349 / 10000 => 95349 / 10^4 => 9
可以看出我们可以通过模10来取其最低位，除10^(n-1)来取其最高位，将其最高位和最低位进行比较，便可以得出当前是否符合回文要求了, 比较完最高位和最低位后，如何除掉这两位呢？

    95349 % 1000 => 95349 % 10^4 = 5349
    95349 / 10 = 9534

如此便能完成掐头去尾了.

    int is_palindrome(int x) {
        int a = x, h = 1;

        if (a < 0) return 0;

        while (a / h >= 10) {
            h = h * 10;
        }

        while (a > 0) {
            if (a / h != a % 10) return 0;
            a = a % h;  // 去高位
            a = a / 10; // 去低位
            h = h / 100;
        }

        return 1;
    }

二进制的判断参见[二进制是否为回文数](/posts/algorithm/binary-bit.html)

refer:

- [http://segmentfault.com/blog/code/1190000000453441](http://segmentfault.com/blog/code/1190000000453441)
- [http://blog.csdn.net/cklsoft/article/details/40862037](http://blog.csdn.net/cklsoft/article/details/40862037)
