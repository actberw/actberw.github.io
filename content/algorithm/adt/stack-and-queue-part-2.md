Title: 栈和队列 part 2
Tags: algorithm, data structure, stack, queue
Date: 2014-06-13 20:00:00

### 递归反转stack
>You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on Stack S:
  isEmpty(S)
  push(S)
  pop(S)

把栈{1, 2, 3, 4, 5}看成由两部分组成：栈顶元素1和剩下的部分{2, 3, 4, 5}。如果我们能把{2, 3, 4, 5}颠倒过来，变成{5, 4, 3, 2}，然后在把原来的栈顶元素1放到底部，那么就整个栈就颠倒过来了，变成{5, 4, 3, 2, 1}。

    void reverse(struct sNode** top_ref) {
      int temp;   
      if(!isEmpty(*top_ref)) {
         
        temp = pop(top_ref);                        
        reverse(top_ref);
        insertAtBottom(top_ref, temp);
      }      
    } 

    void insertAtBottom(struct sNode** top_ref, int item) {
       int temp;  
       if(isEmpty(*top_ref)) {  
           push(top_ref, item); 
       }
       else {
         
         temp = pop(top_ref);
         insertAtBottom(top_ref, item);
     
         push(top_ref, temp);
       }             
    } 

### 栈的push、pop序列

>输入两个整数序列。其中一个序列表示栈的push顺序，判断另一个序列有没有可能是对应的pop顺序。为了简单起见，我们假设push序列的任意两个整数都是不相等的。

    bool is_possible_pop_order(int *push_order, int *pop_order, int len) {
        stack s;
        int i, j;
        i = j = 0;
        while (j < len) {
            if (is_empty(&s) || top(&s) != pop_order[j]) {
                if (i >= len) break;
                push(&s, push_order[i++]);
            } else {
                pop(&s);
                j++;
            }
        }
        return (is_empty(&s) && j == len) ? true: false;
    }

### Implement Queue using Stacks

有两种方法:

- By making put operation costly  

        put(q, x)
        1) While stack1 is not empty, push everything from satck1 to stack2.
        2) Push x to stack1 (assuming size of stacks is unlimited).
        3) Push everything back to stack1.
        get(q)
        1) If stack1 is empty then error
        2) Pop an item from stack1 and return it

- By making get operation costly  

        put(q,  x)
          1) Push x to stack1 (assuming size of stacks is unlimited).
        get(q)
          1) If both stacks are empty then error.
          2) If stack2 is empty
               While stack1 is not empty, push everything from satck1 to stack2.
          3) Pop the element from stack2 and return it.


Queue can also be implemented using one user stack and one Function Call Stack. 

    put(q, x)
      1) Push x to stack1.

    get(q):
      1) If stack1 is empty then error.
      2) If stack1 has only one element then return it.
      3) Recursively pop everything from the stack1, store the popped item in a variable res,  push the res back to stack1 and return res

### Implement Stack using Queues
>We are given a Queue data structure that supports standard operations like enqueue() and dequeue(). We need to implement a Stack data structure using only instances of Queue.

同样是两种方法:

- By making push operation costly  

        push(s, x) // x is the element to be pushed and s is stack
          1) Enqueue x to q2
          2) One by one dequeue everything from q1 and enqueue to q2.
          3) Swap the names of q1 and q2 
        // Swapping of names is done to avoid one more movement of all elements 
        // from q2 to q1. 
        pop(s)
          1) Dequeue an item from q1 and return it.

- By making pop operation costly  

        push(s,  x)
          1) Enqueue x to q1 (assuming size of q1 is unlimited).
        pop(s)  
          1) One by one dequeue everything except the last element from q1 and enqueue to q2.
          2) Dequeue the last item of q1, the dequeued item is result, store it.
          3) Swap the names of q1 and q2
          4) Return the item stored in step 2.
        // Swapping of names is done to avoid one more movement of all elements 
        // from q2 to q1.

refer:

- [http://www.geeksforgeeks.org/reverse-a-stack-using-recursion/](http://www.geeksforgeeks.org/reverse-a-stack-using-recursion/)
- [http://www.geeksforgeeks.org/queue-using-stacks/](http://www.geeksforgeeks.org/queue-using-stacks/)
- [http://www.geeksforgeeks.org/implement-stack-using-queue/](http://www.geeksforgeeks.org/implement-stack-using-queue/)
- [http://zhedahht.blog.163.com/blog/static/25411174200732102055385/](http://zhedahht.blog.163.com/blog/static/25411174200732102055385/)
