Title: 有关括号的问题
Tags: algorithm, data structure, stack
Date: 2014-06-13 22:00:00


### N对括号所有的合法状态 (Generate Parentheses)
>给定N对括号，输出其所有的合法的组合状态，例如，N=3，所有的合法状态为："((()))”, “(()())”, “(())()”, “()(())”, “()()()”

思路：还是深搜DFS的思路，深搜的过程关键在于记录已经用掉的左括号个数和右括号的个数，当用过的左括号个数小于右括号则非法；当二者个数和大于2N则非法；当二者个数相等且数目等于2N则为合法。

    #include<stdio.h>
 
    #define PAIR 50
 
    char str[PAIR * 2 + 1]; // 设括号对数不超过50, str记录括号组合状态
 
    void DFS_bracket(int n, int left_used, int right_used) {
        if(left_used == right_used && left_used + right_used == 2*n) {
            printf("%s\n",str);
            return;
        }
        if(left_used < right_used || left_used + right_used >= 2*n) {
            return ;
        }
        int index = left_used + right_used;
        str[index] = '(';
        DFS_bracket(n, left_used + 1, right_used);
     
        str[index] = ')';
        DFS_bracket(n, left_used, right_used + 1);
    }
     
    int main(void)
    {
        int N;
        scanf("%d", &N);
        DFS_bracket(N,0,0);
        return 0;
    }

### 括号匹配合法性检测 (Valid Parentheses)
>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

>The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

### 最长正确的括号 (Longest Valid Parentheses)


refer:

- [http://www.chenhd.com/stack/](http://www.chenhd.com/stack/)
- [http://www.ahathinking.com/archives/186.html](http://www.ahathinking.com/archives/186.html)
