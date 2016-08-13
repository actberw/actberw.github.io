Title: 整数相关题目
Tags: algorithm
Date: 2014-09-02

### 符合条件的整数
>任意给定的正整数N, 求一个最小的正整数M, 使得N*M的十进制表示形式只含有1和0.

### 整数集合中找出3的最大倍数-数学
>给一个包含非负整数的数组(长度为n)，找出由这些数字组成的最大的3的倍数，没有的话则输出impossible。

refer:

- [http://www.acmerblog.com/find-the-largest-number-multiple-of-3-5820.html](http://www.acmerblog.com/find-the-largest-number-multiple-of-3-5820.html)

### 整数拆分
>输入两个整数 n 和 m，从数列1，2，3.......n 中 随意取几个数, 使其和等于 m ,要求将其中所有的可能组合列出来

这道题就是一道典型的动态规划问题了，思路和背包问题差不多，m就相当于背包能容纳的重量了，就是从右往左校验，通过m，以及m-n进行下一次, 也就是当前是f(m,n)那接下来就是进行f(m,n-1)和f(m-n,n-1)进行递归.  而终止条件是n<=0, 以及sum<0, sum=0时候说明正好找到.

    #include <stdio.h>
    #define N 10
    /*
        f(sum,n)= f(sum-n,n-1) + f(sum,n-1);
    */

    typedef struct stack{
        int array[N];
        int index;
    } Stack;

    int is_empty(Stack *q) {
        return q->index <= 0;
    }

    void push(Stack *q, int value) {
        q->array[q->index] = value;
        q->index++;
    }

    int pop(Stack *q) {
        if (is_empty(q))
            return -1;

        q->index--;
        return q->array[q->index];
    }

    int print_stack(Stack *q) {
        int i;
        for (i = 0; i < q->index; i++) {
            printf("%d ", q->array[i]);
        }
        printf("\n");
    }

    void find_factor(int sum, int n, Stack *q) {
        int i;
        if (sum == 0) {
            print_stack(q);
            return;
        }

        if (n <=0 || sum < 0)
            return;
        push(q, n);
        find_factor(sum - n , n - 1, q);
        pop(q);
        find_factor(sum, n - 1, q);
    }

    int main(void) {
        int m = 15, n = N;
        Stack q = {.index = 0};
        find_factor(15, N, &q);
        return 0;
    }

扩展:

- 将N拆分成多个整数相加和的形式，求出所有的形式, 参见refer[1].

refer:

- [0][http://blog.csdn.net/v_JULY_v/article/details/6419466](http://blog.csdn.net/v_JULY_v/article/details/6419466)
- [1][http://m.blog.csdn.net/blog/sangni007/8521005](http://m.blog.csdn.net/blog/sangni007/8521005)

### 整数的拆分问题(个数)
>如，对于正整数n=6，可以拆分为：
6
5+1
4+2, 4+1+1
3+3, 3+2+1, 3+1+1+1
2+2+2, 2+2+1+1, 2+1+1+1+1
1+1+1+1+1+1+1
现在的问题是，对于给定的正整数n，程序输出该整数的拆分种类数

状态表示: 将n划分为k个数相加的组合方案数记为 q(n,k)。（相当于将n个苹果放入k个盘子）
状态转移:

- 若k>n，则盘子数大于苹果数，至少有k-n个空盘子，可以将其拿掉，对组合方案数无影响。
q(n,k) = q(n,n)
- 若k<=n，则盘子数小于等于苹果数，则分为两种情况
    - 至少有一个盘子空着：q(n,k) = q(n,k-1)
    - 所有盘子都不空：q(n,k) = q(n-k,k)

所以: q(n,k) = q(n,k-1) + q(n-k,k)

    int q(int n , int m)  {  
        if(n < 1 || m < 1)  
            return 0;  
        if(n == 1 || m == 1)  
            return 1;  
        if(n < m)  
            return q(n , n);  
        if(n == m)  
            return q(n , m - 1) + 1;  
        return q(n , m - 1) + q(n - m , m);  
    }  
      
    int main(void)  
    {  
        int n;  
        while(scanf("%d",&n)!=EOF)  
        {  
            cout<<q(n,n)<<endl;  
        }  
        return 0;  
    } 


### 反转整数

    int reverse(int x) {
        // c除法是向0方向取最接近精确值的整数, 不需要管正负, 这里没有考虑溢出情况. 可以用int64_t表示.
        int ret=0;
        while(x) {
            ret = ret * 10 + x % 10;
            x /= 10;
        }

        return ret;
    }

refer:

- [http://blog.csdn.net/kenden23/article/details/18696083](http://blog.csdn.net/kenden23/article/details/18696083)
- [http://segmentfault.com/blog/code/1190000000452052](http://segmentfault.com/blog/code/1190000000452052)
