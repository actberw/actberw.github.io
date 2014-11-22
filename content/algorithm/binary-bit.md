Title: 整数位的操作
Tags: algorithm, bit, c
Date: 2014-09-04

### 二进制表示1的个数

    # 解法1
    int count(int v) {
        int num = 0;
        while (v) {
            if (v % 2 == 1) {
                num++;
            }
            v /=2;
        }
        return num;
    }

    # 解法2
    int count(int v) {
        int num = 0;
        while (v) {
            num += v & 0x1;
            v >>= 1;
        }
        return num;
    }

    # 解法 3
    int count(int v) {
        int num = 0;
        while (v) {
            v &= (v-1);
            num++;
        }
        return num;
    }



### 反转整数二进制表示

    # 解法1
    int bit_reverse(int v) {
        int size = sizeof(v) * 8, result=0, i;
        for (i = 0; i < size; v >>= 1) {
            result = (result << 1) | (v & 0x01);
        }
        return result;
    }

    # 解法2
    int bit_reverse(unsigned int )
    {
        v = ((v >> 1) & 0x55555555) | ((v << 1) & 0xaaaaaaaa);
        v = ((v >> 2) & 0x33333333) | ((v << 2) & 0xcccccccc);
        v = ((v >> 4) & 0x0f0f0f0f) | ((v << 4) & 0xf0f0f0f0);
        v = ((v >> 8) & 0x00ff00ff) | ((v << 8) & 0xff00ff00);
        v = ((v >> 16) & 0x0000ffff) | ((v << 16) & 0xffff0000);

        returv v;
    }    

### 整数a, b(二进制表示), 把a变为b需要改变多少位
解决这个问题转化为计算a^b有多少个1.

    int change(int x, int y) {
        return count(x^y);
    }

### 二分查找32位整数的前导0个数

Hacker's Delight上的代码, 程序思想是二分查找.

    int nlz(unsigned x) {
       int n;
       if (x == 0) return(32);
       n = 1;
       if ((x >> 16) == 0) {n = n +16; x = x <<16;}
       if ((x >> 24) == 0) {n = n + 8; x = x << 8;}
       if ((x >> 28) == 0) {n = n + 4; x = x << 4;}
       if ((x >> 30) == 0) {n = n + 2; x = x << 2;}
       n = n - (x >> 31);
       return n;
    }

### 判断二进制是否为回文数

参见[十进制数是否为回文数](/posts/algorithm/palindrome-number.html), 二进制比较不能直接反转比较，因为反转后可能是个负数.

    is_palindrome(int x) {
        int a = x>>1, mask = 1;
        while(a) {
            mask <<= 1;
            a >>= 1;
        }
        while (a) {     //能否用a判断?
            if ((x & mask) ^ (x & 0x1) != 0x0) return 0;
            x &=(~mask); //去高位
            x >>= 1;     //去低位
            mask >>= 2; 
        }
        return 1;
    }

refer:

- [http://en.wikipedia.org/wiki/Hamming_weight](http://en.wikipedia.org/wiki/Hamming_weight)
