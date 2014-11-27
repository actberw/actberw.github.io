Title: 素因数分解
Date: 2014-06-15 19:00:00
Tags: algorithm, prime number


质因数分解：就是把一个合数分解成几个素数相乘的形式

### 试除法 
给定一个合数n（这里，n是待分解的正整数），试除法看成是用小于等于\sqrt{n}的每个素数去试除待分解的整数。如果找到一个数能够整除除尽，这个数就是待分解整数的因子。

    void trial_divisio_fac(int n) {
        int i;
        for (i = 2; i < sqrt(n); i++) {
            while(n%i == 0)
            {
                cout << i << ends;
                n = n / i;
            }
        }
        if(n>1) cout<<n;//n没有因数
    }

### 质因数分解法应用
>本题让我们输入一个正整数N，然后求出一最小的正整数M使得 N/M 是一个素数。

由此我们可以将N一直除以一个比它自己本身小的质数，按照质因数分解的方法，不停的进行分解，我们要找到一个分解出的最大的素数P,因为只有这样，我们才能使得M最小。


refer:

- [http://www.tuicool.com/articles/jQvqAzr](http://www.tuicool.com/articles/jQvqAzr)
