Title: 最长回文子串
Tags: algorithm, c, str, manacher
Date: 2014-11-09

### 暴力解法

枚举出所有的可能字符串判断是否是回文串, 找出最大的, 时间复杂度为$O(n^3)$

### 中心扩展法
中心扩展就是把给定的字符串的每一个字母当做中心，向两边扩展，中心点左侧如果对应的和右侧都一致，则该字符串是回文串, 时间复杂度为$O(n^2)$
### 动态规划
Stated more formally below:

    Define P[ i, j ] ← true iff the substring Si … Sj is a palindrome, otherwise false.
Therefore,

    P[ i, j ] ← ( P[ i+1, j-1 ] and Si = Sj )
    The base cases are:

    P[ i, i ] ← true
    P[ i, i+1 ] ← ( Si = Si+1 )

This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on… 

### 转化为求lcs

### Manacher算法

    int mx = 0;
    int id = 0;
    int[] p =new int[s2.length()];
    p[0] = 0;
    for(int i = 1; i < s2.length() - 1; i++){
        p[i] = mx > i ? Math.min(p[2 * id - i], mx - i) : 1;
 
        while(s2.charAt(i + p[i]) == s2.charAt(i - p[i])){
            p[i] ++;
        }
        if(i + p[i] > mx){
            mx = i + p[i];
            id = i;
        }
    }

refer:

- [http://vicdory.com/longest_palindromic_substring.html](http://vicdory.com/longest_palindromic_substring.html)
- [http://m.blog.csdn.net/blog/sangni007/8155041](http://m.blog.csdn.net/blog/sangni007/8155041)
- [http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html](http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html)
- [http://www.felix021.com/blog/read.php?2040](http://www.felix021.com/blog/read.php?2040)
