Title: 八皇后问题
Tags: algorithm, c/c++

1. 问题描述
>八皇后问题是一个古老而著名的问题，是回溯算法的典型例题。该问题是十九世纪著名的数学家高斯1850年提出：在8X8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。

2. 代码(递归)

        #include<stdlib.h>
        #include<stdio.h>

        #define N 8

        int queen[N], sum=0;

        int check(n) {//n: row number
            int i;
            for (i = 0; i < n; i++) {
                if ((queen[i] == queen[n]) || (abs(queen[i] - queen[n]) == (n - i)))
                ¦   return 0;
            }
            return 1;
        }

        void show() {
            int i;
            for (i = 0; i < N; i++) {
                printf("%d %d\n", i, queen[i]);
            }
            sum++;
        }

        void put(n) {//n: row number
            int i;
            for (i = 0; i < N; i++) {
                queen[n] = i;
                if (check(n)) {
                ¦   if (n == (N - 1))
                        show();
                ¦   else
                        put(n+1);
                }
            }
        }


        int main(void) {
            put(0);
            printf("solution num: %d", sum);
            return 0;
        } 

3. 代码(迭代)

        #include<stdlib.h>

        #define N 8

        int queen[N], sum=0;

        int check(int n) {//n: row number
            int i;
            for (i = 0; i < n; i++) {
                if ((queen[i] == queen[n]) || (abs(queen[i] - queen[n]) == (n - i)))
                   return 0;
            }
            return 1;
        }

        void show() {
            int i;
            for (i = 0; i < N; i++) {
                printf("%d %d\n", i, queen[i]);
            }
            sum++;
        }

        int queens() {
            int n = 0;//n: row num
            queen[n] = 0;
            while (n >= 0 && n < N) {
                while (queen[n] < N && !check(n)) queen[n]++;
                if (queen[n] < N) {
                   if (n == (N - 1)) {
                       show();
                       queen[n]++;
                   } else {
                        queen[++n] = 0;
                   }
                } else {
                    n--;
                    queen[n]++;
                }
            }
        }

        int main(void) {
            queens();
            printf("solution num: %d", sum);
            return 0;
        }

refer:

- [http://www.slyar.com/blog/eight-queen-c-program.html](http://www.slyar.com/blog/eight-queen-c-program.html)
