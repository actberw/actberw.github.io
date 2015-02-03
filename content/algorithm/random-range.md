Title: 随机数范围
Tags: algorithm, random, c
Date: 2014-09-05

### 缩小范围

    unsigned int fac = (RAND_MAX + 1u) / N;
    unsigned int limit = fac * N;
    unsigned int r;
    do {
        r = rand();
    } while(r >= limit);
    return r / fac;


### 扩大范围
> rand7()产生1~7之间的随机数，如何用rand7()函数产生1~10之间的随机数

扩大范围的处理是先用类似(rand7()-1)*7+rand7()) 构造一个大范围，然后在缩小范围处理.

    // 循环实现 
    int rand10() {
        int fac = 49 / 10;
        int limit = fac * 10;
        int x = 0;
        do {
            x = (rand7()-1)*7+rand7();
        }while(x >= limit);                 //大于40的，即41~49区间的取值舍弃

        return x / fac;
    }

    // 递归实现 
    int rand10() {
        int fac = 49 / 10;
        int limit = fac * 10;
        int x = (rand7()-1)*7+rand7();
        if (x >= limit)
            return rand10()
        else
            return x / fac;
    }

### 概率问题 

refer:
>已知随机数生成函数f()，返回0的概率是60%，返回1的概率是40%。根据f()求随机数函数g()，使返回0和1的概率是50%，不能用已有的随机生成库函数。

分析: 调用f()两次即可，会出现4种结果(0,0), (0,1), (1,0), (1,1)，其中出现(0,1), (1,0)的概率是一样的，可以构造出等概率事件，比如出现(0,1)可返回0，出现(1,0)可返回1，如果出现其他两种情况则舍掉重新调用。

    int rand() {
    int a, b;
    while(1) {
        a = f();
        b = f();
        if (a == 0 && b == 1)
            return 0;
        if (a == 1 && b == 0)
            return 1;
        }
    } 

- [http://c-faq.com/lib/randrange.html](http://c-faq.com/lib/randrange.html)
- [http://www.dewen.io/q/15492?sort=newest](http://www.dewen.io/q/15492?sort=newest)
- [http://www.byywee.com/page/M0/S906/906096.html](http://www.byywee.com/page/M0/S906/906096.html)
- [http://www.verydemo.com/demo_c180_i34806.html](http://www.verydemo.com/demo_c180_i34806.html)
- [http://sumnous.github.io/blog/2014/05/13/random-pick-function/](http://sumnous.github.io/blog/2014/05/13/random-pick-function/)
