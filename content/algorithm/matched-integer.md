Title: 整数相关题目
Tags: algorithm
Date: 2014-09-02

### 符合条件的整数
>任意给定的正整数N, 求一个最小的正整数M, 使得N*M的十进制表示形式只含有1和0.

### 满足条件的两个数
>输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。如果有多对数字的和等于输入的数字，输出任意一对即可.

    void find(int *array, int n, int sum, int *i, int *j) {
        int left = 0, right=n - 1;
        while (left < right) {
            if (array[left] + array[right] == sum) {
                *i = left, *j = right;
                return;
            } else if (array[left] + arry[right] > sum) {
                right--;
            } else {
                left ++;
            }

        }
        *i = -1, *j = -1;
    }

扩展:

- 如果将“两个数字”改为“三个数字”或“任意个数字”时，如何求解？ 参见refer[0].

refer:

- [0][http://www.cnblogs.com/youxin/p/3367398.html](http://www.cnblogs.com/youxin/p/3367398.html)

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

### 反转整数

    int reverse(int x) {
        // c除法是向0方向取最接近精确值的整数, 不需要管正负, 这里没有考虑溢出情况.
        int ret=0;
        while(x) {
            ret = ret * 10 + x % 10;
            x /= 10;
        }

        return ret;
    }

### valid number
>Validate if a given string is numeric.

>Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

refer:

- [http://blog.csdn.net/kenden23/article/details/18696083](http://blog.csdn.net/kenden23/article/details/18696083)


refer:

- [http://segmentfault.com/blog/code/1190000000452052](http://segmentfault.com/blog/code/1190000000452052)
