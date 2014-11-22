Title: 二分查找 
Tags: algorithm, binary search
Date: 2014-11-10

###二分查找元素key的下标

left <= right

### 元素的上下边界问题
left < right -1 (否则可能会死循环)

主要是array[mid] == v时处理情况不同:
如果是求下边界, 搜索l~mid, 如果是上边界则搜索mid~r, 如果是求相同值有多少个, 分别求出上下边界, 减即可。

扩展问题: 求已排序数组中相同字符出现的次数(求出上下边界, 减即可)

refer:

- [http://hedengcheng.com/?p=595](http://hedengcheng.com/?p=595)
- [http://segmentfault.com/blog/riodream/1190000000698553](http://segmentfault.com/blog/riodream/1190000000698553)
- [http://www.cnblogs.com/gaochundong/p/binary_search.html](http://www.cnblogs.com/gaochundong/p/binary_search.html)
- [http://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/](http://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/)
- [二分查找边界问题](http://www.ahathinking.com/archives/179.html)
