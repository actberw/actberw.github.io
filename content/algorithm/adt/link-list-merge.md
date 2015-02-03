Title: 链表合并
Tags: algorithm, data structure
Date: 2014-06-13 20:00:00

### 合并两个有序链表
> Merge the two sorted link list in O(n) time and O(1) space  

- 非递归实现，分析:分别用指针p1，p2来遍历两个链表，如果当前p1指向的数据小于p2指向的数据，则将p1指向的结点归入合并后的链表中，否则，将p2指向的结点归入合并后的链表中。如果有一个链表遍历结束，则把未结束的链表连接到合并后的链表尾部。

            link merge_link(link a, link b) {//非递归实现
                link c = NULL, p1 = a, p2 = b, tmp;

                // 也可以用亚元节点避免这段if
                if (p1->item < p2->item) {//初始化c
                    c = p1;
                    p1 = p1->next;
                } else {
                    c = p2;
                    p2 = p2->next;
                }
                tmp = c;
                while (p1 != NULL && p2 != NULL) {
                    if (p1->item < p2->item) {
                    ¦   tmp->next = p1;
                    ¦   p1 = p1->next;
                    } else {
                    ¦   tmp->next = p2;
                    ¦   p2 = p2->next;
                    }
                    tmp = tmp->next;
                }
                
                tmp->next = (p1 != NULL)? p1: p2;

                return c;
            }

- 递归实现

            link merge_link2(link a, linkb) {//递归实现，但是不满足空间复杂度O(1)要求
                link c = NULL;
                if (a == NULL) return b;
                if (b == NULL) return a;
                if (a->item < b->item) {
                    c = a;
                    c->next = merge_link2(a->next, b);
                } else {
                    c = b;
                    c->next = merge_link2(a, b->next);
                }
                return c;
            }


### 合并k个有序的链表

用最小堆实现, 用k个链表的头节点构建K个元素的最小堆, 每次取堆顶元素, 同时把堆顶元素的next加入堆中, 时间复杂度为O(log(k) * n), k is number of list and n is number of total elements.

    //  Definition for singly-linked list.
    class ListNode {
        int val;
        ListNode next;
     
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
     
    public class Solution {
        public ListNode mergeKLists(ArrayList<ListNode> lists) {
            if (lists.size() == 0)
                return null;
     
            //PriorityQueue is a sorted queue
            PriorityQueue<ListNode> q = new PriorityQueue<ListNode>(lists.size(),
                    new Comparator<ListNode>() {
                        public int compare(ListNode a, ListNode b) {
                            if (a.val > b.val)
                                return 1;
                            else if(a.val == b.val)
                                return 0;
                            else 
                                return -1;
                        }
                    });
     
            // add first node of each list to the queue
            for (ListNode list : lists) {
                if (list != null)
                    q.add(list);
            }
     
            ListNode head = new ListNode(0); // 亚元节点
            ListNode p = head; // serve as a pointer/cursor
     
            while (q.size() > 0) {
                //poll() retrieves and removes the head of the queue - q. 
                ListNode temp = q.poll();
                //keep adding next element of each list
                if (temp.next != null)
                    q.add(temp.next);

                p.next = temp;
                p = p.next;
            }
     
            return head.next;
        }
    }


refer:

- [http://www.geeksforgeeks.org/merge-two-sorted-linked-lists/](http://www.geeksforgeeks.org/merge-two-sorted-linked-lists/)
- [http://www.programcreek.com/2013/02/leetcode-merge-k-sorted-lists-java/](http://www.programcreek.com/2013/02/leetcode-merge-k-sorted-lists-java/)
