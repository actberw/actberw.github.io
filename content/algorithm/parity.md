Title: 奇偶检验
Tags: algorithm
Date: 2014-06-13 18:30:00

如何判断给定位数的二进制数中1的个数是奇数还是偶数的二进制数, 算法得复杂度为O(lgn), n为待检查得数字。
  
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
