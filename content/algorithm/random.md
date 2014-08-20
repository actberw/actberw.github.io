Title:随机数及检验
Tags:algorithm, random
Date: 2014-06-12
1. 随机数算法
    - 取中法
    - 线性同余法(Linear congruential generator)(参见参考[7])  
    $N_{i+1} = aN_{i} + C$ (mod m), 其中其中a为乘子，C为增量，m为模. 产生的随机序列$R_n = N_i / m$.
    - 移位法
    - 梅森旋转算法

2. 检验
    - 参数检验
    - 均匀性检验
    - 独立性检验

refer:

- [1][http://blog.csdn.net/zmazon/article/details/17383521](http://blog.csdn.net/zmazon/article/details/17383521)
- [2][http://wenku.baidu.com/view/0295fdd7b14e852458fb574e.html](http://wenku.baidu.com/view/0295fdd7b14e852458fb574e.html)
- [3][http://wenku.baidu.com/view/bec3a060ddccda38376bafe4.html?from=related](http://wenku.baidu.com/view/bec3a060ddccda38376bafe4.html?from=related)
- [4][http://carlnerv.com/2014/c%E6%A0%87%E5%87%86%E5%BA%93%E9%87%8C%E7%9A%84rand.html](http://carlnerv.com/2014/c%E6%A0%87%E5%87%86%E5%BA%93%E9%87%8C%E7%9A%84rand.html)
- [5][http://www.dewen.org/q/15492](http://www.dewen.org/q/15492)
- [6][http://club.alibabatech.org/article_detail.htm?articleId=2](http://club.alibabatech.org/article_detail.htm?articleId=2)
- [7][http://stackoverflow.com/questions/3932978/gcc-implementation-of-rand](http://stackoverflow.com/questions/3932978/gcc-implementation-of-rand)
