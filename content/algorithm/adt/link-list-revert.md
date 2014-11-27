Title: 链表反转
Tags: algorithm, data structure
Date: 2014-06-12 19:00:00

### 反整个链表

        link reverse(link head) {//递归实现
            if (head->next == NULL || head == NULL) {
                return head;
            }
            link rp = reverse(head->next);
            head->next->next = head;
            head->next = NULL;
            return rp;
        } 

        link reverse(link head) {//非递归实现
            link prev=NULL, p, pn;
            for (p=head;p !=NULL; p=pn) {
                pn = p->next;
                p->next = prev;
                prev = p;
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

借助三个个指针实现翻转, pre指向第m个节点前面那个，cur指向第m个节点，p1指向m的下一个节点，因为p1有可能是NULL，所以当p1不是NULL的时候，p2指向p1的下一个节点。

### 交换链表中的两个节点(Swap Nodes in Pairs)
>Given a linked list, swap every two adjacent nodes and return its head.
For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.
    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

添加一个亚元节点, 简化处理 

    ListNode *swapPairs(ListNode *h)  {  
        ListNode dummy(0);  
        dummy.next = h;  
        ListNode *pre = &dummy;  
        while (h && h->next)  
        {  
            ListNode *t = h->next->next;  
            pre->next = h->next;  
            h->next->next = h;  
            h->next = t;  
            pre = h;  
            h = t;  
        }  
        return dummy.next;  
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

    // 翻转pre ~ next之间的, 然后返回最有一个节点
    private static ListNode reverse(ListNode pre, ListNode next){
        ListNode last = pre.next;//where first will be doomed "last"
        ListNode cur = last.next;
        while(cur != next){
            last.next = cur.next;
            cur.next = pre.next;
            pre.next = cur;
            cur = last.next;
        }
        return last;
    }

    public static ListNode reverseKGroup2(ListNode head, int k) {
         if(head == null || k == 1) return head;
         ListNode dummy = new ListNode(0);
         dummy.next = head;
         ListNode pre = dummy;
         int i = 0;
         while(head != null){
             i++;
             if(i % k ==0){
                 pre = reverse(pre, head.next);
                 head = pre.next;
             }else {
                 head = head.next;
             }
         }
         return dummy.next;
     }

refer:

- [http://www.cnblogs.com/4everlove/p/3651002.html](http://www.cnblogs.com/4everlove/p/3651002.html)
- [http://blog.csdn.net/kenden23/article/details/17004749](http://blog.csdn.net/kenden23/article/details/17004749)
- [http://www.cnblogs.com/lichen782/p/leetcode_Reverse_Nodes_in_kGroup.html](http://www.cnblogs.com/lichen782/p/leetcode_Reverse_Nodes_in_kGroup.html)
