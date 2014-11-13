Title: divide 和  multiply
Tags: algorithm, c
Date: 2014-09-04

### divide
>Divide two integers without using multiplication, division and mod operator.

最直观的方法是，用被除数逐个的减去除数，直到被除数小于0。这样做会超时。那么如果每次不仅仅减去1个除数，计算速度就会增加，但是题目不能使用乘法，因此不能减去k*除数，我们可以对除数进行左移位操作，这样每次相当于减去2^k个除数，如何确定k呢，只要使 $2^k$*除数 <=  当前被除数 < $2^{k+1}$*除数.


    int divide(int x, int y) {
        int i, ret;
        unsigned int a, b; //用unsigned 因为-INT_MIN 溢出问题(结果还是INT_MIN)
        unsigned long div; //防止溢出
        a = x > 0 ? x : -x;
        b = y > 0 ? y : -y;
        while (a > b) {
            for(i = 0, div=b; div < a; i++) {
            ¦   div <<= 1;
            }
            ret += (1<<(i - 1)); // i 从零开始最后多加了一次所以减去, div左移的次数
            a -= b << (i - 1);
        }
        return (x > 0) ^ (y > 0) ? -ret : ret;
    }

### multiply
>Multiply two integers without using multiplication, division and bitwise operators, and no loops

To multiply x and y, recursively add x y times.

    int multiply(int x, int y) {
       if(y == 0)
         return 0;
     
       /* Add x one by one */
       if(y > 0 )
         return (x + multiply(x, y-1));
      
      /* the case where y is negative */
       if(y < 0 )
         return -multiply(x, -y);
    }

refer: 

- [http://www.cnblogs.com/TenosDoIt/p/3795342.html](http://www.cnblogs.com/TenosDoIt/p/3795342.html)
- [http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/](http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/)
