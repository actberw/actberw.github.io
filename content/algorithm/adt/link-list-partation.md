Title: 链表划分
Tags: algorithm, data structure
Date: 2014-06-12 21:00:00

>Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

>You should preserve the original relative order of the nodes in each of the two partitions.

>For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.

一次遍历，遇小前插，关键是要维护一个指向要插入位置的指针, 对链表的快排可以用到这个子过程(按头节点划分).

    public class Solution {
        public ListNode partition(ListNode head, int x) {
            if(head == null) return null;
     
            ListNode fakeHead1 = new ListNode(0);
            ListNode fakeHead2 = new ListNode(0);
            fakeHead1.next = head;
     
            ListNode p = head;
            ListNode prev = fakeHead1;
            ListNode p2 = fakeHead2;
     
            while(p != null){
                if(p.val < x){
                    p = p.next;
                    prev = prev.next;
                }else{
     
                    p2.next = p;
                    prev.next = p.next;
     
                    p = prev.next;
                    p2 = p2.next;
                } 
            }
     
            // close the list
            p2.next = null;
     
            prev.next = fakeHead2.next;
     
            return fakeHead1.next;
        }
    }
