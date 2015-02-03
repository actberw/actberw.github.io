Title: huffman 树与 huffman 编码
Tags: algorithm, huffman
Date: 2014-09-04

### 带权路径长度和huffman树

从树的一个节点到另一个节点之间的分支构成两节点之间的路径, 而路径长度(path length)则是指路径上的分支数. 树的路径长度是从树的根节点到每个一节点的路径长度之和.

设一颗二叉树有n个叶节点, 它们各自带有权值$w_1, w_2, ..., w_n$, 则带权路径长度(WPL, weight path length)定义为:   

>$WPL = \sum_{i=1}^{i=n}w_{i}l_{i}$

其中$l_i$为叶子节点到根节点的路径长度.

称WPL最小的二叉树为最优二叉树, 直观的看就是WPL最小的二叉树就是权值大的叶子节点离根节点最近, 这样树称为huffman树.

赫夫曼树具有如下特性:

- 对于同一组权值，所能得到的赫夫曼树不一定是唯一的。
- 赫夫曼树的左右子树可以互换，因为这并不影响树的带权路径长度。
- 带权值的节点都是叶子节点，不带权值的节点都是某棵子二叉树的根节点。
- 权值越大的节点越靠近赫夫曼树的根节点，权值越小的节点越远离赫夫曼树的根节点。
- 赫夫曼树中只有叶子节点和度为2的节点，没有度为1的节点。
- 一棵有n个叶子节点的赫夫曼树共有2n-1个节点。

### huffman树的构造

赫夫曼树的构建步骤如下:

- 将给定的n个权值看做n棵只有根节点（无左右孩子）的二叉树，组成一个集合HT，每棵树的权值为该节点的权值。
- 从集合HT中选出2棵权值最小的二叉树，组成一棵新的二叉树，其权值为这2棵二叉树的权值之和。
- 将步骤2中选出的2棵二叉树从集合HT中删去，同时将步骤2中新得到的二叉树加入到集合HT中。
- 重复步骤2和步骤3，直到集合HT中只含一棵树，这棵树便是赫夫曼树。

利用优先队列实现见refer[0]

### huffman编码

霍夫曼编码是一种无损数据压缩算法。在计算机数据处理中，霍夫曼编码使用变长编码表对源符号（如文件中的一个字母）进行编码，其中变长编码表是通过一种评估来源符号出现机率的方法得到的，出现机率高的字母使用较短的编码，反之出现机率低的则使用较长的编码，这便使编码之后的字符串的平均长度、期望值降低，从而达到无损压缩数据的目的。

构建霍夫曼编码主要包括两个部分(参见refer[1]):

- 根据输入的字符串构建霍夫曼树。
- 遍历huffman树并给每个字符分配编码(左支编码为0，右支编码为1)

### Fence Repair
>有一个农夫要把一个木板钜成几块给定长度的小木板，每次锯都要收取一定费用，这个费用就是当前锯的这个木版的长度
给定各个要求的小木板的长度，及小木板的个数n，求最小费用

长度较长应该经过较少的切割次数后得到, 类比哈夫曼树出现频度较高的字符编码较短, 这题用哈夫曼编码的思路即可解决. 要使总费用最小, 那么每次只选取最小长度的两块木板相加, 再把这些“和”累加到总费用中即可. 本题虽然利用了Huffman思想，但是直接用HuffmanTree做会超时，可以用优先队列做.

    using namespace std;  
      
    //比较规则，最小优先  
    class cmp  
    {  
    public:  
        bool operator()(const __int64 a,const __int64 b)const  
        {  
            return a>b;  
        }  
    };  
      
    int main(void)  
    {  
        int n;  //需要切割的木板个数  
        while(cin>>n)  
        {  
            priority_queue<__int64,vector<__int64>,cmp>Queue;  //定义优先队列  
      
            for(int i=1;i<=n;i++)  
            {  
                __int64 temp;  
                scanf("%I64d",&temp);  
                Queue.push(temp);       //输入要求的木板长度（费用）并入队  
            }  
      
            __int64 mincost=0;   //最小费用  
            while(Queue.size()>1)  //当队列中小于等于一个元素时跳出  
            {  
                __int64 a=Queue.top();  //得到队首元素的值，并使其出队  
                Queue.pop();  
                __int64 b=Queue.top();  //两次取队首，即得到最小的两个值  
                Queue.pop();  
      
                Queue.push(a+b);  //入队  
                mincost+=a+b;  
            }  
      
            printf("%I64d\n",mincost);  
      
            while(!Queue.empty())  //清空队列  
                Queue.pop();  
        }  
        return 0;  
    } 

refer:

- [0][http://imakechoice.com/?p=224](http://imakechoice.com/?p=224)
- [1][http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/](http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/)
- [2][http://www.acmerblog.com/jiudu-1172-2331.html](http://www.acmerblog.com/jiudu-1172-2331.html)
- [3][http://coolshell.cn/articles/7459.html](http://coolshell.cn/articles/7459.html)
- [4][http://poj.org/problem?id=3253](http://poj.org/problem?id=3253)
- [5][http://blog.csdn.net/lyy289065406/article/details/6647423](http://blog.csdn.net/lyy289065406/article/details/6647423)
