Title: 奇偶检验
Tags: algorithm
Date: 2014-06-13 18:30:00

奇偶校验位是一个表示给定位数的二进制数中1的个数是奇数还是偶数的二进制数。奇偶校验位是最简单的错误检测码。

奇偶校验位有两种类型：偶校验位与奇校验位。如果一组给定数据位中1的个数是奇数，那么偶校验位就置为1反之则为0，从而使得总的1的个数是偶数。如果给定一组数据位中1的个数是偶数，那么奇校验位就置为1反之为0，使得总的1的个数是奇数。偶校验实际上是循环冗余校验的一个特例，通过多项式x + 1得到1位CRC。

如何判断给定位数的二进制数中1的个数是奇数还是偶数的二进制数(参见[整数位的操作](/posts/algorithm/binary-bit.html)), n为待检查得数字。
  
    /* Function to get parity of number n. It returns 1
     * if n has odd parity, and returns 0 if n has even
     * parity
     */

    //解法1
    bool get_parity(unsigned int n)
    {
        bool parity = 0;
        while (n) {
            parity = !parity;
            n      = n & (n - 1);
        }
        return parity;
    }

    //解法2
    unsigned int get_parity2(unsigned int n) {
        unsigned int parity = 0;
        unsigned int bit_length =  sizeof(unsigned int) * 8;
        while(n && bit_length > 0) {
            parity ^= (n & 1);
            n = n >> 1;
            bit_length--;
        }

        return parity;
    }

refer:

 - [http://blog.csdn.net/u010993034/article/details/9316043](http://blog.csdn.net/u010993034/article/details/9316043)
 - [http://www.geeksforgeeks.org/write-a-c-program-to-find-the-parity-of-an-unsigned-integer/](http://www.geeksforgeeks.org/write-a-c-program-to-find-the-parity-of-an-unsigned-integer/)
