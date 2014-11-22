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
如果根本就不允许你再开一个数组，只能用额外的一到两个变量。那么，你可以依次访问 这个数组的每个元素，每访问一个，就将该元素到字符串结尾的元素中相同的元素去掉( 比如置为’\0′ 或 0).时间复杂度为O(n2 )

解法2

如果可以开一个固定大小，与问题规模(即字符串长度)无关的数组，那么可以用一个数组来 表征每个字符的出现(假设是ASCII字符，则数组大小为256)，这样的话只需要遍历一遍字符 串即可，时间复杂度O(n)。

解法3

如果字符集更小一些，比如只是a-z，即字符串里只包含小写字母，那么使用一个int变量中 的每一位来表征每个字符的出现，一样可以在O(n)的时间里移除重复字符，而且还不需要额 外开一个数组。

参见refer[3]

refer:

- [0][http://zhedahht.blog.163.com/blog/static/25411174200722191722430/](http://zhedahht.blog.163.com/blog/static/25411174200722191722430/)
- [1][http://m.blog.csdn.net/blog/sangni007/8155041](http://m.blog.csdn.net/blog/sangni007/8155041)
- [2][http://zhedahht.blog.163.com/blog/static/25411174200801931426484/](http://zhedahht.blog.163.com/blog/static/25411174200801931426484/)
- [3][http://www.acmerblog.com/remove-duplicate-character-5906.html](http://www.acmerblog.com/remove-duplicate-character-5906.html)
