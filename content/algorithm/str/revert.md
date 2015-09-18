Title: 字符串反转
Tags: algorithm, c, str
Date: 2014-11-08

### 反转字符串

    void revert(char * str, unsigned int left, unsigned int right) {
        char tmp;
        if (str == NULL || left > right)
            return;
        while(left < right) {
            tmp = str[left];
            str[left] = str[right];
            str[right] = tmp;
            left++;right--;
        }
    }

### 反转句子中单词的顺序
>输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。

>例如输入“I am a student.”，则输出“student. a am I”。

由于本题需要翻转句子，我们先颠倒句子中的所有字符。这时，不但翻转了句子中单词的顺序，而且单词内字符也被翻转了。我们再颠倒每个单词内的字符。由于单词内的字符被翻转两次，因此顺序仍然和输入时的顺序保持一致。

    void revert_world(char * str) {
        int left, right, length = strlen(str);
        revert(str, 0, length - 1); // revert string
        left = right = 0;
        for (;right <= length; right++) {
            if (str[right] == ' ' || str[right] == '\0') {
                revert(str, left, right - 1);
                right++;
                left = right;
            }
        }
    }

### 数组循环移位
>设计一个算法把含有N个元素的数组循环右移K位, 要求时间复杂度为O(N), 且只允许使用两个附加变量.

可以先考虑简单的办法, 可以每次将数组的元素右移一位, 循环K次. 

    void right_shift(char* str, int n, int k) {
        int i;
        char tmp;
        k %= n;
        while(k--) {
            tmp = str[n-1]; 
            for(i=n-1; i > 0; i--) {
                str[i] = str[i-1];
            }
            str[0] = tmp;
        }
    } 

但是算法的复杂度位O(kn), 不符合O(n)要求.

假设原来的数组为ab1234, 要求转换成的数组序列为1234ab, 即循环右移了4位, 可以看出有两段是不变的: ab, 1234, 可以把这两段看成整体, 右移K位的过程看做是两部分的交换, 即后K位与前面部分的交换.

    void right_shift(char* str, int n, int k) {
        k %= n;
        revert(str, 0, strlen(str)-1);
        revert(str, 0, k-1);
        revert(str, k, n-1);
    }

