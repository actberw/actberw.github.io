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

    void ExpPop(stack *S,int a,int *flag) {
        int temp;
        if(IsEmpty(S)) *flag=0;
        if(GetTop(S)!=a) *flag=0;
        Pop(S,&temp);
    }

    void Exp(stack *S) {
        char buffer[100];
        int flag=1,i=0;
        puts("please input the exp:");
        memset(buffer,0,sizeof(buffer));
        gets(buffer);
        while(buffer[i]&&flag) {
            switch (buffer[i]) {
            case '(':Push(S,1);break;
            case '[':Push(S,2);break;
            case '{':Push(S,3);break;
            case ')':ExpPop(S,1,&flag);break;
            case ']':ExpPop(S,2,&flag);break;
            case '}':ExpPop(S,3,&flag);break;
            default : break;
            }
            i++;
        }
        if(!flag||!IsEmpty(S)) puts("error!");
        else puts("right!");
        puts("--------------------");
    }

### 最长正确的括号 (Longest Valid Parentheses)
>Given a string containing just the characters  '('  and  ')' , find the length of the longest valid (well-formed) parentheses substring.

>For  "(()" , the longest valid parentheses substring is  "()" , which has length = 2.

>Another example is  ")()())" , where the longest valid parentheses substring is  "()()" , which has length = 4.

求最长合法匹配的长度，这道题可以用一维动态规划逆向求解。假设输入括号表达式为String s，维护一个长度为s.length的一维数组dp[]，数组元素初始化为0。 dp[i]表示从s[i]到s[s.length - 1] 包含s[i] 的最长的有效匹配括号子串长度。则存在如下关系：

dp[s.length - 1] = 0;
i从n - 2 -> 0逆向求dp[]，并记录其最大值。若s[i] == '('，则在s中从i开始到s.length - 1计算dp[i]的值。这个计算分为两步，通过dp[i + 1]进行的（注意dp[i + 1]已经在上一步求解）:
- 在s中寻找从i + 1开始的有效括号匹配子串长度，即dp[i + 1]，跳过这段有效的括号子串，查看下一个字符，其下标为j = i + 1 + dp[i + 1]。若j没有越界，并且s[j] == ‘)’，则s[i ... j]为有效括号匹配，dp[i] =dp[i + 1] + 2。
- 在求得了s[i ... j]的有效匹配长度之后，若j + 1没有越界，则dp[i]的值还要加上从j + 1开始的最长有效匹配，即dp[j + 1]。

代码实现:

    int longestValidParentheses(string s) {
        int len = s.length();
        if(len<2)
          return 0;
        int max = 0;
        int *dp = new int[len];
        for(int k = 0;k<len;k++)//把辅助数组清空，存储为0
         dp[k] = 0;
        for(int i = len-2;i>=0;i--) {

          if(s[i] == '(') {           //只对左括号处理，右括号在数组中存储为0
            int j = i+1+dp[i+1];      //计算与当前左括号匹配的右括号的位置, 可能存在也可能不存在
            if(j<len && s[j] == ')') { //确保位置不能越界
              dp[i] = dp[i+1] + 2;   //找到了相匹配的右括号，当前数组中存储的最长长度是它后一个位置加2

              if(j+1<len)            //这是连接两个子匹配的关键步骤
                dp[i] += dp[j+1];    //在j的后面可能已经存在连续的匹配，要记得加上。dp[j+1]存储了以j+1开始的匹配
            }
            if(dp[i]>max)
              max = dp[i];//更新最长长度
          }
        }
        return max;
    }

refer:

- [http://www.ahathinking.com/archives/186.html](http://www.ahathinking.com/archives/186.html)
- [http://www.chenhd.com/stack/](http://www.chenhd.com/stack/)
- [http://www.tuicool.com/articles/vUnEbi](http://www.tuicool.com/articles/vUnEbi)
