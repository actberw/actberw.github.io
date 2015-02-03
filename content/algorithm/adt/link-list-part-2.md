Title: 单链表常见问题
Tags: algorithm, data structure
Date: 2014-06-12 20:00:00
### 访问
> 1. 找出单链表的倒数第K个元素(仅允许遍历一遍链表)
2. 找出单链表的中间元素

对于#1 龟兔算法(快慢指针). fast, slow两个指针, fast先前进到第K个位置, 然后两个指针同步向后移, 知道fast到达末尾(fast->next == NULL).

对于#2 同样是龟兔算法(快慢指针), fast, slow两个指针, fast移动速度是slow 的两倍.

### 有环
>1. 判断单链表是否有环(Floyd 环查找算法)
2. 如何知道环的长度
3. 如何找到环入口
4. 求带环链表的长度
5. 如何将有环的链表变成单链表

![有环链表](/img/link-cycle.jpg)

对于#1 定义fast, slow两个指针, fast移动速度是slow 得两倍, 如果fast == low 则有环, 否则无环.

    int has_cycle(link *a) {
        link fast, slow;
        fast = slow = a;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (fast == slow)
                return 1 // 有环
        }
        return 0;
    }

第一次相遇时slow走过的距离：a + b + p(b + c)，fast走过的距离：a + b + q(b + c)。 因为fast的速度是slow的两倍，所以fast走的距离是slow的两倍，有 2(a + b + p(b + c)) = a+ b + q(c+b)，可以得到a + b = (q - 2p)(b + c)。

对于#2 : 第一次相遇后，让fast停着不走了，slow继续走，记录到下次相遇时循环了几次; 

对于#3 根据上面的结论结论，那么让两个指针分别从X和Z开始走，每次走一步，那么正好会在Y相遇！也就是环的第一个节点。

对于#4 知道了环长度和环入口, 两段长度加起来就是.

对于#5 将Y之前得next = NULL

### 相交
>1. 如何知道两个单链表（无环）是否相交?
2. 如果两个单链表（无环）相交,如何知道它们相交的第一个节点是什么?
3. 如何知道两个单链表（有环）是否相交？
4. 如果两个单链表（有环）相交，如何知道它们相交的第一个节点是什么？

对于#1 判断两链表最后一个节点是否相同，如果相交，则尾节点肯定是同一节点. 或者将链表A的尾节点指向链表B(人为构环)，如果B链表有环，则两个链表相交，此时从链表B的头指针往下遍历，如果能够回到B，则说明相交.

对于#2 依然是快慢指针, 首先先取得两个链表A和B的长度len(A)和len(B), 沿着A和B链表中较长的链表遍历，使用指针追赶的方法, 设定两个指针fast、slow。fast先出发前进(lengthMax-lengthMin)步（即是二者的长度之差）使fast和slow指针到相交点的距离相等,之后两个链表同时前进，每次一步，相遇的第一点即为两个链表相交的第一个点

对于#3 求出A的环入口，判断其是否在B链表上，如果在，则相交。
对于#4 两个有环链表相交是指这个环属于两个链表共有, 所以跟无环相交处理方式相同.


### 复制
>You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link list. The second pointer however CAN point to any node in the list and not just the previous node. Now write a program in O(n) time to duplicate this list. That is, write a program which will create a copy of this list.

![链表复制](/img/link-list-copy.jpg)

第一次遍历将要复制的链表A’ B’ C’ D’插入员链表中，然后再一次遍历复制random指针：A'->next->random = A->random->next;
恢复很简单：A->next=A->next->next;A’-next=A’->next->next;

### 删除
>删除排序链表中重复的元素

    public class Solution {
        public ListNode deleteDuplicates(ListNode head) {
            if(head == null || head.next == null)
                return head;
     
            ListNode p = head;
     
            while( p!= null && p.next != null){
                if(p.val == p.next.val)
                    p.next = p.next.next;
                p = p.next; 
            }
     
            return head;
        }
    }

### 相加(add two numbers)
>You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

>Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

This is a simple problem. It can be solved by doing the following:

- Use a flag to mark if previous sum is >= 10
- Handle the situation that one list is longer than the other
- Correctly move the 3 pointers p1, p2 and p3 which pointer to two input lists and one output list

        link add_two_number(link a, link b) {
            int carry = 0; //进位标示
            link c;
            link p1 = a, p2 = b, p3;
            c = new_node(0);
            p3 = c;
            while (p1 != NULL || p2 != NULL) { // 对比合并
                 if(p1 != NULL) {
                     carry += p1->value;
                     p1 = p1->next;
                 } 
                 if(p2 != NULL) {
                     carry += p2->value;
                     p2 = p2->next;
                 } 
                 p3->next = new_node(carry%10);
                 p3 = p3->next;
                 carry /= 10;
            }

            if (carry == 1)  // 因为都是单个数字所以和不可能大于10, 所以carry不可能大于1
                p3->next = new_node(1);

            return c->next;
        }

### 有序单链表转化为bst
http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
http://www.acmerblog.com/convert-sorted-list-to-binary-search-tree-6124.html

refer:

- [0][http://vitrivs.blogspot.sg/2013/08/floydcycle-detection.html](http://vitrivs.blogspot.sg/2013/08/floydcycle-detection.html)
- [1][http://m.blog.csdn.net/blog/sangni007/8218552](http://m.blog.csdn.net/blog/sangni007/8218552)
- [2][http://www.cppblog.com/yuech/archive/2011/04/02/143318.html](http://www.cppblog.com/yuech/archive/2011/04/02/143318.html)
- [3][http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/](http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/)
- [4][http://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work](http://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work)
