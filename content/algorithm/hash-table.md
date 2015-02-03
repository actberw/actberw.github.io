Title: 散列表(hashtable)
Tags: algorithm, hash

表中元素的存储位置与表元素的关键值之间建立了对应函数:
address = hash(rec.key)
按照此种方式构造出来的表或者结构叫做散列表.

### 常见的散列函数

hash算法的两个问题:

- 对于给定关键词集合, 计算简单且地址分布比较均匀, 避免或尽量减少冲突 
- 解决冲痛方式

1. 直接定址法
2. 除留余数法
3. 数字分析法
4. 平方取中法

### 解决冲突的方法
分两种:开地址法和关地址法

1. 线性探测法
2. 二次探测法
3. 双散列法
4. 链接地址法

refer:

- [http://blog.csdn.net/v_july_v/article/details/6256463](http://blog.csdn.net/v_july_v/article/details/6256463)
- [http://www.zhihu.com/question/20820286](http://www.zhihu.com/question/20820286)
