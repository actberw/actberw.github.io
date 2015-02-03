Title: 素数算法
Date: 2014-06-15 19:00:00
Tags: algorithm, prime number

素数的定义: 除了能被1和它本身整除而不能被其他任何数整除的数。根据素数定义 只需要用2到n-1去除n，如果都除不尽，则n是素数，否则，只要其中有一个数能整除则n不是素数。

两种办法: 试除法和筛法

### 原始算法  

    bool is_primer(int num) {
        for(int i = 2; i < num; i++) {
            if(num % i == 0) { /*若整除则为假，否则为真*/
                return false;
            }
        }
        return true;
    }

### 从2到sqrt(N)的整数是否整除N

    bool is_primer(int num) {
        for(int i = 2; i * i < num; i++) {
            if(num % i == 0) { /*若整除则为假，否则为真*/
               return false;
            }
        }
        return true;
    }

### 改进去掉偶数得判断(i+=2)

    bool is_primer(int num) {
        if (num == 2) 
            return true;
        else if (num % 2 == 0)
            return false;
        else {
            for(int i = 3; i * i < num; i+=2) {
                if(num % i == 0) /*若整除则为假，否则为真*/
                   return false;
            }
            return true;
        }
    }

### 筛选算法
更高效地素数判断方法应该是将素数预先保存到一个素数表中，当判断一个数是否为素数时，直接查表即可。这种方法需要解决两个问题:

- 怎样快速得到素数表 (埃拉托斯特尼筛法)
- 怎样减少素数表的大小 (采用位图数据结构或者2~max_int的所有素数顺序存在内存里面用二分查找或者用hashtable)

埃拉托斯特尼筛法(参见[1]).
>对于1到n全部整数, 逐个判断它们是否是素数, 找出一个非素数, 就把它挖掉, 最后剩下的就是素数。具体方法是： <1> 定义primer[i] = true (primer也可以用bitmap存储); <2> 从2开始, 依次遍历整个primer(直到sqrt(N)), 如果primer[i]=true,则primer[j]=false j ∈ {n², n²+n, n²+2n, ..., limit}

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

### 随机算法(参见[3])


refer:

- [1][http://dongxicheng.org/structure/prime/](http://dongxicheng.org/structure/prime/)
- [2][http://www.zhihu.com/question/19668324](http://coolshell.cn/articles/3738.html)
- [3][http://www.zhihu.com/question/19668324](http://www.zhihu.com/question/19668324)
- [4][http://program-think.blogspot.com/2011/12/prime-algorithm-1.html](http://program-think.blogspot.com/2011/12/prime-algorithm-1.html)
