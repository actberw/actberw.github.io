Title: python 多重继承方法解析顺序
Tags: python, mro, c3
Date: 2014-11-02 13:00:00

pyhton 支持多重继承, 方法(or attribute)查找顺序称为mro, 目前有三种mro: 

- classic
- python 2.2 new-style
- c3

其中只有c3算法是2.3+广泛使用的.

### classic mro  
classic mro 采用的是简单的广度有限算法(DFS), 中序遍历. 查找过程中第一个匹配的返回. 这种算法简单情况下没问题，但是diamond 继承时就出现问题了, 例如:

    class A:
      def save(self): pass

    class B(A): pass

    class C(A):
      def save(self): pass

    class D(B, C): pass

对于D classic mro查找方法的顺序为: D, B, A, C, A, 调用save方法时A的save方法会被调用, 正确情况应该是C的save方法

### python 2.2 new-style  
针对上面的问题2.2中查找算法做了下改进,依然是中序遍历, 不过对于mro中多次出现的类, 只保留最后出现的那个，其他的删除,  上面的用新的mro算法就是: D, B, C, A. 但是这种算法依然有不适用的情况, 参见refer[0].

### c3  
在复杂的继承中满足所有情况的mro规则就是monotonic, 简单的标记介绍: 

C1 C2 ... CN
表示类列表(list of classes)[C1, C2, ... , CN], 其中表头是第一个项C1(head=C1), 表尾是除了表头的其他项(tail=C2 ... CN.)

C + (C1 C2 ... CN) = C C1 C2 ... CN

表示列表相加 [C] + [C1, C2, ... ,CN].

如果要计算L\[C\](the linearization L[C] of the class C). 规则如下:
>the linearization of C is the sum of C plus the merge of the linearizations of the parents and the list of the parents.

符号表示为:

    L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)

merge的计算遵循下面的规则:
>take the head of the first list; if this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head of the next list and take it, if it is a good head. Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class C and will raise an exception

### bad mro  
A MRO is bad when it breaks such fundamental properties as local precedence ordering and monotonicity. 

refer:

- [0][http://python-history.blogspot.com/2010/06/method-resolution-order.html](http://python-history.blogspot.com/2010/06/method-resolution-order.html)
- [1][https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/)

