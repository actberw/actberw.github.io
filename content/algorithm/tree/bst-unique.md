Title: Unique Binary Search Trees

### Unique Binary Search Trees
>Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

>For example,
Given n = 3, there are a total of 5 unique BST's.

>   1         3     3      2      1  
    \       /     /      / \      \  
     3     2     1      1   3      2  
    /     /       \                 \  
   2     1         2                 3  

>Solution:

>　　See the definition for Catalan Number here, and that's the answer for this problem.

>　　So, this problem is just to test if you know the term Catalan Number. If you do know the math formula, you won't use recurrence relation to calculate it, but use combinatorial number as a faster solution.

>　　Time complexity is O(n), as calculating C(n, k) requires O(k) complexity, and F(n) = C(2n, n) / (n + 1).
　　Space complexity is O(1)

从处理子问题的角度来看，选取一个结点为根，就把结点切成左右子树，以这个结点为根的可行二叉树数量就是左右子树可行二叉树数量的乘积，所以总的数量是将以所有结点为根的可行结果累加起来。写成表达式如下：

$C_0 = C_1 = 1\ and\ C_{n+1} = \sum_{i=0}^{i=n} C_{i}C_{n-i}$

复合卡特兰数的一种定义方式.

    public int numTrees(int n) {  
        if(n<=0)  
            return 0;  
        int[] res = new int[n+1];  
        res[0] = 1;  
        res[1] = 1;  
        for(int i=2;i<=n;i++)  
        {  
            for(int j=0;j<i;j++)  
            {  
                res[i] += res[j]*res[i-j-1];  
            }  
        }  
        return res[n];  
    }  

当然这道题还可以用卡特兰数的通项公式来求解，这样时间复杂度就可以降低到O(n), 参见refer[2].

### Unique Binary Search Trees II

refer:

- [0][http://blog.csdn.net/linhuanmars/article/details/24761459](http://blog.csdn.net/linhuanmars/article/details/24761459)
- [1][http://blog.csdn.net/linhuanmars/article/details/24761437](http://blog.csdn.net/linhuanmars/article/details/24761437)
- [2][http://www.cnblogs.com/zhuli19901106/p/3499924.html](http://www.cnblogs.com/zhuli19901106/p/3499924.html)
