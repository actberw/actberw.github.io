Title: 最长公共子串(子序列)
Tags: algorithm, c, str
Date: 2014-11-10

### 最长公共子串

暴力解法

以字符串中的每个字符作为子串的端点，判定以此为开始的子串的相同字符最长能达到的长度。其实从表层上想，这个算法的复杂度应该只有O(n2)因为该算法把每个字符都成对相互比较一遍，但关键问题在于比较两个字符串的效率并非是O(1)，这也导致了实际的时间复杂度应该是满足Ω(n2)和O(n3)。

    int lcs(char *str1, char *str2) {
        int max_len = 0, curr_len;
        int start_index1, start_index2;
        int i, j, x, y;
        for (i = 0; i < strlen(str1); i++) {
            for (j = 0; j < strlen(str2); j++) {
                curr_len = 0;
                x = i; y = j;
                while (x < strlen(str1) && j < strlen(str2) && str1[x++] == str2[y++]);
                curr_len = x - i;
                if (curr_len > max_len) {
                    start_index1 = i;
                    start_index2 = j;
                    max_len = curr_len
                }
            } 
        }

        return max_len;
    }



Dynamic Programming can be used to find the longest common substring in O(m*n) time. The idea is to find length of the longest common suffix for all substrings of both strings and store these lengths in a table.

>The longest common suffix has following optimal substructure property
   LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
                           0  Otherwise (if X[m-1] != Y[n-1])

>The maximum length Longest Common Suffix is the longest common substring.
   LCSubStr(X, Y, m, n)  = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m
                                                        and 1 <= j <= n

    int LCSubStr(char *X, char *Y, int m, int n) {
        int LCSuff[m+1][n+1];
        int result = 0;  // To store length of the longest common substring
     
        /* Following steps build LCSuff[m+1][n+1] in bottom up fashion. */
        for (int i=0; i<=m; i++) {
            for (int j=0; j<=n; j++) {
                if (i == 0 || j == 0)
                    LCSuff[i][j] = 0;
     
                else if (X[i-1] == Y[j-1]) {
                    LCSuff[i][j] = LCSuff[i-1][j-1] + 1;
                    result = max(result, LCSuff[i][j]);
                }
                else LCSuff[i][j] = 0;
            }
        }
        return result;
    }

`LCSuff[i][j] = LCSuff[i-1][j-1] + 1;` 空间可以优化下, 因只用到相邻得两行.

### 最长公共子序列

>Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.
refer:

    int lcs( char *X, char *Y, int m, int n ) {
       int L[m+1][n+1];
       int i, j;
     
       for (i=0; i<=m; i++) {
         for (j=0; j<=n; j++) {
           if (i == 0 || j == 0)
             L[i][j] = 0;
     
           else if (X[i-1] == Y[j-1])
             L[i][j] = L[i-1][j-1] + 1;
     
           else
             L[i][j] = max(L[i-1][j], L[i][j-1]);
         }
       }
       
       return L[m][n];
    }  

refer:

- [http://www.cnblogs.com/ider/p/longest-common-substring-problem-optimization.html](http://www.cnblogs.com/ider/p/longest-common-substring-problem-optimization.html)
- [http://www.geeksforgeeks.org/longest-common-substring/](http://www.geeksforgeeks.org/longest-common-substring/)
- [http://www.ahathinking.com/archives/115.html](http://www.ahathinking.com/archives/115.html)
