Title: 算法: c语言实现读书笔记
Tags: note
Date: 2014-08-07 19:00:00
3.1  基本组件  
基本数据类型(char, int, float, double), arrry, struct, point

3.2 数组(array)  
埃拉托斯特尼筛法(参见[1])
>对于1到n全部整数，逐个判断它们是否是素数，找出一个非素数，就把它挖掉，最后剩下的就是素数。具体方法是： <1> 定义is_primer[i] = true; <2> 从2开始，依次遍历整个is_primer(直到sqrt(N))，如果is_primer[i]=true,则is_primer[i]=false i ∈ {n², n²+n, n²+2n, ..., limit}

    #define N 1000
    int main() {
        int i, j, a[N];
        //init
        for (i = 2; i < N; i++) a[i] = 1;

        for (i = 2; i < sqrt(N); i++) {
            if(a[i]) {
                for ( j = i; i * j < N; j++)
                    a[i*j] = 0;
            }
        }
    }

refer:
- [1][http://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95](http://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95)
