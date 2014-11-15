Title: 链表
Tags: algorithm, data structure
Date: 2014-06-12 19:00:00

链表是一组数据项的集合, 其中每个数据项是节点的一部分，每个节点包含指向下一个节点的链接. 对比数组链表的优缺点如下:可以高效的重排数据项例如插入节点的复杂度为O(1)，但是不能快速的访问任意的数据项，只能沿着链表一个一个节点的访问.

 - 优点
     - 链表是动态数据结构，可以按需分配内存
     - 删除和增加节点复杂度为O(1)

 - 缺点
     - 因为额外的指针域需要更多的内存 
     - 只能从头节点顺序的访问

### 分类

- 单链表(Singly linked list)  
它包含两个域，一个信息域和一个指针域。这个链接指向列表中的下一个节点，而最后一个节点则指向一个空值。
- 双向链表(Doubly linked list)  
每个节点有两个连接：一个指向前一个节点，（当此“连接”为第一个“连接”时，指向空值或者空列表）；而另一个指向下一个节点，（当此“连接”为最后一个“连接”时，指向空值或者空列表）
- 循环链表(Circular list)  
在一个 循环链表中, 首节点和末节点被连接在一起。这种方式在单向和双向链表中皆可实现。

### 基本操作
- 插入(在指定元素之前插入新结点)

         void insert_afteri(link head, int i, item_t x) {//第i个元素之后插入
             //判断第i个节点是否存在
             link p = head, pnode;
             int j = 0;
             while (p != NULL && j < i) {
                 p = p->next;
                 j++;
             }

             if (j == i && p != NULL) {
                 pnode = new_node(x);
                 pnode->next = p->next;
                 p->next = pnode;
             } else {
                 printf("插入位置不存在\n");
             }
         }

- 删除

        void delete(link head, int i) {
            //移动到i-1个节点
            int j = 0;
            link p = head, pnode;
            while (p != NULL && j < (i-1)) {
                p = p->next;
                j++;
            }

            if (p != NULL && p->next != NULL) {
                pnode = p->next;
                p->next = pnode->next;
                free(pnode);
            } else {
                printf("i节点不存在\n");
            }
        }

- 反转

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

refer:

- [http://blog.csdn.net/dxdxsmy/article/details/7346326](http://blog.csdn.net/dxdxsmy/article/details/7346326)
- [http://www.acmerblog.com/category/data-struct/linear/](http://www.acmerblog.com/category/data-struct/linear/)
- [http://www.cnblogs.com/Jax/archive/2009/12/11/1621504.html](http://www.cnblogs.com/Jax/archive/2009/12/11/1621504.html)
