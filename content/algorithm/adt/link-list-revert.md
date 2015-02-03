Title: 链表反转
Tags: algorithm, data structure
Date: 2014-06-12 19:00:00

### 反整个链表

        link reverse(link head) {//递归实现
            if (head == NULL || head->next == NULL) {
                return head;
            }
            link rp = reverse(head->next);
            head->next->next = head;
            head->next = NULL;
            return rp;
        } 

        // 三个指针实现翻转

        link reverse(link head) {//非递归实现
            link prev=NULL, p, pn;
            for (p=head;p !=NULL; p=pn) {
                pn = p->next;
                p->next = prev;
                prev = p;
                p = pn;
            }
            return prev;
        }

### 反转链表部分
>Reverse a linked list from position m to n. Do it in-place and in one-pass.

>For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

>      return 1->4->3->2->5->NULL.

>      Note:
      Given m, n satisfy the following condition:
      1 ≤ m ≤ n ≤ length of list.


pre指向第m个节点前面节点, 3个指针实现翻转, p指向第m个节点，q指向m的下一个节点，因为q有可能是NULL，所以当q不是NULL的时候，r指向q的下一个节点。

    typedef struct link_node {
        int value;
        struct link_node *next;
    } *link;

    void revert_mn(link head, int m, int n) {
        int i;
        link prev, p = head, q, r;
        for (i = 1; i < m; i ++) {
            prev = p;
            p = p->next;
        }
        q = p->next;

        for (i = 0; i < (n - m) && q != NULL; i++) {
            r = q->next;
            q->next = p;
            p = q;
            q = r;
        }

        prev->next->next = q;
        prev->next = p;
    }

### 交换链表中的两个节点(Swap Nodes in Pairs)
>Given a linked list, swap every two adjacent nodes and return its head.
For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.
    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

添加一个亚元节点, 简化处理 

    link revert_two(link head) {
        link nhead = &(struct link_node) {-1, NULL}, p = head, prev=nhead, r;
        while (p != NULL && p->next != NULL) {
            r = p->next->next;
            prev->next = p->next;
            p->next->next = p;
            p->next = r;
            prev = p, p = r;
        }
        return nhead->next;
    }

### Reverse Nodes in k-Group 
>Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example,
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

上面的是两个, 这道题是每k个翻转, 最后不足k保留原顺序

    // 翻转l ~ r之间的
    void revert_l_r(link l, link r) {
        link p, q, n;
        p = l, q = p->next;
        while (p != r) {
            n = q->next;
            q->next = p;
            p = q;
            q = n;
        }
        l->next = q; // 跟后续节点连起来
    }

    link revert_k_group(link head, int k) {
        link nhead = &(struct link_node){-1, NULL}, prev = nhead;
        int i; link r = head, l;
        prev->next = head;
        for (i = 1; r != NULL; i++) {
            if (i % k == 0) {
            ¦   l = prev->next;
            ¦   revert_l_r(l, r);
            ¦   prev->next = r;
            ¦   prev = l;
            ¦   r = prev->next;
            } else
            r = r->next;
        }
        return nhead->next;
    }

refer:

- [http://www.cnblogs.com/4everlove/p/3651002.html](http://www.cnblogs.com/4everlove/p/3651002.html)
- [http://blog.csdn.net/kenden23/article/details/17004749](http://blog.csdn.net/kenden23/article/details/17004749)
- [http://www.cnblogs.com/lichen782/p/leetcode_Reverse_Nodes_in_kGroup.html](http://www.cnblogs.com/lichen782/p/leetcode_Reverse_Nodes_in_kGroup.html)
