Title: 字符串相关题目
Tags: algorithm, c, str
Date: 2014-11-07

### 第一个只出现一次的字符
创建一个长度为256的数组，每个字母根据其ASCII码值作为数组的下标对应数组的对应项，而数组中存储的是每个字符对应的次数。这样我们就创建了一个大小为256，以字符ASCII码为键值的哈希表。 我们第一遍扫描这个数组时，每碰到一个字符，在哈希表中找到对应的项并把出现的次数增加一次。这样在进行第二次扫描时，就能直接从哈希表中得到每个字符出现的次数了。 参见refer[0]

### 在字符串中删除特定的字符
>输入They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”。o

分两部分操作: 删除一个字符和查找一个字符

如何在字符串中删除一个字符: 由于字符串的内存分配方式是连续分配的。我们从字符串当中删除一个字符，需要把后面所有的字符往前移动一个字节的位置。但如果每次删除都需要移动字符串后面的字符的话，对于一个长度为n的字符串而言，删除一个字符的时间复杂度为O(n), 事实上，我们并不需要在每次删除一个字符的时候都去移动后面所有的字符。我们可以设想，当一个字符需要被删除的时候，我们把它所占的位置让它后面的字符来填补，也就相当于这个字符被删除了。在具体实现中，我们可以定义两个指针(pFast和pSlow)，初始的时候都指向第一字符的起始位置。当pFast指向的字符是需要删除的字符，则pFast直接跳过，指向下一个字符。如果pFast指向的字符是不需要删除的字符，那么把pFast指向的字符赋值给pSlow指向的字符，并且pFast和pStart同时向后移动指向下一个字符。这样，前面被pFast跳过的字符相当于被删除了。用这种方法，整个删除在O(n)时间内就可以完成。

如何在一个字符串中查找一个字符: 对待删除得字符建一个hashtable

### 删除重复的字符
>Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.

解法1
如果根本就不允许你再开一个数组，只能用额外的一到两个变量。那么，你可以依次访问 这个数组的每个元素，每访问一个，就将该元素到字符串结尾的元素中相同的元素去掉( 比如置为’\0′ 或 0).时间复杂度为O($n^2$)

解法2

如果可以开一个固定大小，与问题规模(即字符串长度)无关的数组，那么可以用一个数组来 表征每个字符的出现(假设是ASCII字符，则数组大小为256)，这样的话只需要遍历一遍字符 串即可，时间复杂度O(n)。

解法3

如果字符集更小一些，比如只是a-z，即字符串里只包含小写字母，那么使用一个int变量中 的每一位来表征每个字符的出现，一样可以在O(n)的时间里移除重复字符，而且还不需要额 外开一个数组。

参见refer[3]
### 最长不重复子串 (Longest Substring Without Repeating Characters)
- 基本算法 使用Hash
- DP方案
- DP + Hash 方案
- DP + Hash 优化方案

基本解法使用Hash

要求子串中的字符不能重复，判重问题首先想到的就是hash，寻找满足要求的子串，最直接的方法就是遍历每个字符起始的子串，辅助hash，寻求最长的不重复子串，由于要遍历每个子串故复杂度为O(n^2)，n为字符串的长度，辅助的空间为常数hash[256]。代码如下

    int maxlen;
    int maxindex;
    void output(char * arr);
     
    /* LNRS 基本算法 hash */
    char visit[256];
     
    void LNRS_hash(char * arr, int size)
    {
        int i, j;
        for(i = 0; i < size; ++i)
        {
            memset(visit,0,sizeof visit); // visit存储字符是否出现过
            visit[arr[i]] = 1;
            for(j = i+1; j < size; ++j)
            {
                if(visit[arr[j]] == 0)
                {
                    visit[arr[j]] = 1;
                }else
                {
                    if(j-i > maxlen)
                    {
                        maxlen = j - i;
                        maxindex = i;
                    }
                    break;
                }
            }
            if((j == size) && (j-i > maxlen))
            {
                maxlen = j - i;
                maxindex = i;
            }
        }
        output(arr);
    }

DP方案

类似最长递增子序列.

用数组dp, dp[i] 表示以字符串索引i字符结尾的最长不重复子串长度

    int dp[30];
     
    void LNRS_dp(char * arr, int size) {
        int i, j;
        int last_start = 0;     // 上一次最长子串的起始位置
        maxlen = maxindex = 0;
     
        dp[0] = 1;
        for(i = 1; i < size; ++i)
        {
            for(j = i-1; j >= last_start; --j) // 遍历到上一次最长子串起始位置
            {
                if(arr[j] == arr[i])
                {
                    dp[i] = i - j;
                    last_start = j+1; // 更新last_start
                    break;
                }else if(j == last_start) // 无重复
                {
                    dp[i] = dp[i-1] + 1;
                }
            }
            if(dp[i] > maxlen)
            {
                maxlen = dp[i];
                maxindex = i + 1 - maxlen;
            }
        }
        output(arr);
    }

DP + Hash 方案

上面的DP方案是O(n^2)的，之所以是n^2，是因为“回头”去寻找重复元素的位置了，受启发于最初的Hash思路，我们可以用hash记录元素是否出现过，我们当然也可以用hash记录元素出现过的下标，既然这样，在DP方案中，我们何不hash记录重复元素的位置，这样就不必“回头”了，而时间复杂度必然降为O(N)，只不过需要一个辅助的常数空间visit[256]，典型的空间换时间。


    void LNRS_dp_hash(char * arr, int size) {
        memset(visit, -1, sizeof visit);
        memset(dp, 0, sizeof dp);
        maxlen = maxindex = 0;
        dp[0] = 1;
        visit[arr[0]] = 0; // 这里的visit 存储最近重复的位置(索引)
        int last_start = 0;
     
        for(int i = 1; i < size; ++i)
        {
            if(visit[arr[i]] == -1)
            {
                dp[i] = dp[i-1] + 1;
                visit[arr[i]] = i; /* 记录字符下标 */
            }else
            {
                if(last_start <= visit[arr[i]])
                {
                    dp[i] = i - visit[arr[i]];
                    last_start = visit[arr[i]] + 1;
                    visit[arr[i]] = i; /* 更新最近重复位置 */
                }else
                {
                    dp[i] = dp[i-1] + 1;
                    visit[arr[i]] = i; /* 更新最近重复位置 */
                }
     
            }
            if(dp[i] > maxlen)
            {
                maxlen = dp[i];
                maxindex = i + 1 - maxlen;
            }
        }
        output(arr);
    }


DP + Hash 优化方案

>dp[i] = dp[i-1] + 1;

dp[i-1]不就是更新dp[i]当前的最优解么？这与最大子数组和问题的优化几乎同出一辙，我们不需要O(n)的辅助空间去存储子问题的最优解，而只需O(1)的空间就可以了.

    /* LNRS dp + hash 优化 */
    void LNRS_dp_hash_impro(char * arr, int size) {
        memset(visit, -1, sizeof visit);
        maxlen = maxindex = 0;
        visit[arr[0]] = 0;
        int curlen = 1;
        int last_start = 0;
     
        for(int i = 1; i < size; ++i) {
            if(visit[arr[i]] == -1) {
                ++curlen;
                visit[arr[i]] = i; /* 记录字符下标 */
            }else {
                if(last_start <= visit[arr[i]]) {
                    curlen = i - visit[arr[i]];
                    last_start = visit[arr[i]] + 1;
                    visit[arr[i]] = i; /* 更新最近重复位置 */
                }else {
                    ++curlen;
                    visit[arr[i]] = i; /* 更新最近重复位置 */
                }
            }
            if(curlen > maxlen) {
                maxlen = curlen;
                maxindex = i + 1 - maxlen;
            }
        }
        output(arr);
    }

### 把字符串转换成数字

>题目要求：
如果前面有空格开头，忽略掉开头的所有空格
如果发现没意义的字符，忽略之，并结束转换。即123ttyw -> 123
考虑负数额
如果溢出，则返回相应的最大正数和最大负数。

    int atoi(char *str) {
        int i = 0, flag = 0, ret, dig;
        if (str == NULL || strlen(str) < 1)
            return 0;
        while(i < strlen(str) && str[i] == ' ') i++;
        // 判断符号
        if (str[i] == '-') {
            flag = 1;
            i++;
        } else if (str[i] == '+')
            i++;

        while (i < strlen(str) && '0' <= str[i] <= '9') {
            if (INT_MAX/10 > ret)
            ¦   ret = ret * 10 
            else
                // overflow
                return flag ? INT_MIN: INT_MAX;
            dig = str[i] - '0';
            if ((INT_MAX - ret) > dig)
                ret += dig;
            else
                // overflow
                return flag ? INT_MIN: INT_MAX;
        }

        return flag ? -ret: ret;
    }

### 判断一个字符串中的字符是否都只出现一次
－排序然后看charArray[i] 是否与charArray[i+1]相等
- 用bitmap, 一个int表示所有字符(26个)

        public static boolean isUniqueChars(String str) {
            int checker = 0;
            for (int i = 0; i < str.length(); ++i) {
              int val = str.charAt(i) - 'a';
              if ((checker & (1 << val)) > 0)
                return false;
              checker |= (1 << val);
            }
            return true;
        }

refer:

- [0][http://zhedahht.blog.163.com/blog/static/25411174200722191722430/](http://zhedahht.blog.163.com/blog/static/25411174200722191722430/)
- [1][http://m.blog.csdn.net/blog/sangni007/8155041](http://m.blog.csdn.net/blog/sangni007/8155041)
- [2][http://zhedahht.blog.163.com/blog/static/25411174200801931426484/](http://zhedahht.blog.163.com/blog/static/25411174200801931426484/)
- [3][http://www.acmerblog.com/remove-duplicate-character-5906.html](http://www.acmerblog.com/remove-duplicate-character-5906.html)
- [4][Longest Substring Without Repeating Characters](http://www.ahathinking.com/archives/123.html)
