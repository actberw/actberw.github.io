Title: 栈和队列 part 3
Tags: algorithm, data structure, stack, queue
Date: 2014-06-13 21:00:00

### 栈上实现min函数
>实现一个带Min函数的栈(Stack)，让其可以支持O(1)的Push，O(1)的Pop，O(1)的Top和O(1)的Min(返回整个Stack中的最小元素)。

用两个Stack，其中Stack1保存原始数据。Stack2保存最小值更新序列。如对于数据4 5 3 1 2(最后边是栈顶)，Stack1的数据为[4,5,3,1,2]，Stack2的数据为[4,3,1]，Stack2的Top()一直保存的是Stack1中的最小元素。


Min(): 返回Stack2.Top()


Push(x)：首先在Stack1中Push(x)，然后比较Stack2的Top与x的大小，如果x更小则Push到Stack2中


Top(): 返回Stack1.Top()


Pop(): 从Stack1中Pop()出栈顶元素，与这个Stack2的Top()进行比较，如果相同，则Stack2中也Pop()出栈顶元素。对于处理存在相同数值元素的问题，可以在Stack2的每个数加一个计数器，计数器减到0则Pop()

### 队列上实现min函数


refer:

- [http://www.ninechapter.com/problem/23/](http://www.ninechapter.com/problem/23/)
- [http://www.ninechapter.com/problem/50/](http://www.ninechapter.com/problem/50/)
