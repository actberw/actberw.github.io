Title: 单链表排序

## 快排序

    struct link_node {
            int data;
            struct link_node *next;
    };


    typedef struct link_node node_t;
    typedef struct link_node * link_list;

    node_t *partition(node_t *l, node_t *r) {
            int key;
            node_t *p, *q, *prev;
            q = l;;
            prev = l;
            p = prev->next;
            key = p->data;
            while (p != r) {
                    if (p->data < key) {
                            prev->next = p->next;
                            p->next = q->next;
                            q->next = p;
                            q = q->next;
                            p = prev->next;
                    } else {
                            prev = p;
                            p = p->next;
                    }
            }
            return q->next;
    }

    void quick_sort(link_list head, node_t *tail) {
            node_t *pivot;
            if (head->next == NULL || head->next == tail || head->next->next == tail) return; // dummy head;
            pivot = partition(head, tail);
            quick_sort(head, pivot);
            quick_sort(pivot, tail);
    }

## 归并排序

    // 自顶向下
    link merge_sort(link c) {
        link b, slow, fast;
        slow = fast = c;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }

        b = slow->next;
        slow->next = NULL;
        return merge(merge_sort(c), merge_sort(b))
    } 

    // 自底向上
    link merge_sort(link t) {
        link p, q, tmp;
        if (t == NULL || t->next == NULL) return t;
        p = t;

        queue_init();
        while (p != NULL) {
            q = p->next;
            p->next = NULL;
            queue_put(p);
            p = q;
        }
        while (!queue_empty()) {
            tmp = merge(queue_get(), queue_get());
            queue_put(tmp);
        }

        return t;
    }

非递归见refer[1]
refer:

- [0][http://www.geeksforgeeks.org/quicksort-on-singly-linked-list/](http://www.geeksforgeeks.org/quicksort-on-singly-linked-list/)
- [1][http://noalgo.info/834.html](http://noalgo.info/834.html)
