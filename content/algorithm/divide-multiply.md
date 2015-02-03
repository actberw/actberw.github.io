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

### 加法
>写一个函数，求两个整数的之和，要求在函数体内不得使用＋、－、×、÷。

首先我们可以分析人们是如何做十进制的加法的，比如是如何得出5+17=22这个结果的。实际上，我们可以分成三步的：第一步只做各位相加不进位，此时相加的结果是12（个位数5和7相加不要进位是2，十位数0和1相加结果是1）；第二步做进位，5+7中有进位，进位的值是10；第三步把前面两个结果加起来，12+10的结果是22，刚好5+17=22。

求两数之和四则运算都不能用，那还能用什么啊？对呀，还能用什么呢？对数字做运算，除了四则运算之外，也就只剩下位运算了。位运算是针对二进制的，我们也就以二进制再来分析一下前面的三步走策略对二进制是不是也管用。

5的二进制是101，17的二进制10001。还是试着把计算分成三步：第一步各位相加但不计进位，得到的结果是10100（最后一位两个数都是1，相加的结果是二进制的10。这一步不计进位，因此结果仍然是0）；第二步记下进位。在这个例子中只在最后一位相加时产生一个进位，结果是二进制的10；第三步把前两步的结果相加，得到的结果是10110，正好是22。由此可见三步走的策略对二进制也是管用的。

接下来我们试着把二进制上的加法用位运算来替代。第一步不考虑进位，对每一位相加。0加0与 1加1的结果都0，0加1与1加0的结果都是1。我们可以注意到，这和异或的结果是一样的。对异或而言，0和0、1和1异或的结果是0，而0和1、1和0的异或结果是1。接着考虑第二步进位，对0加0、0加1、1加0而言，都不会产生进位，只有1加1时，会向前产生一个进位。此时我们可以想象成是两个数先做位与运算，然后再向左移动一位。只有两个数都是1的时候，位与得到的结果是1，其余都是0。第三步把前两个步骤的结果相加。如果我们定义一个函数AddWithoutArithmetic，第三步就相当于输入前两步骤的结果来递归调用自己。

    int AddWithoutArithmetic(int num1, int num2) {
        int sum, carry;
        if(num2 == 0)
            return num1;
        sum = num1 ^ num2;
        carry = (num1 & num2) << 1;
        return AddWithoutArithmetic(sum, carry);
    }

refer: 

- [http://www.cnblogs.com/TenosDoIt/p/3795342.html](http://www.cnblogs.com/TenosDoIt/p/3795342.html)
- [http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/](http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/)
- [http://www.acmerblog.com/interview-12-3180.html](http://www.acmerblog.com/interview-12-3180.html)
