Title: 树的遍历
Tags: bst, data structure 
Date: 2014-09-02 14:00:00

### 二叉树的遍历

深度优先遍历: 前序, 中序, 后序
    
    // 递归实现
    void traverse(tree root, void (*visit)(tree)) {
        if (root == NULL) return;
        visit(root); // 前序, 调整visit位置, 可变为中序, 后序
        tranverse(root->lchild);
        tranverse(root->rchild);
    }

    // 前序非递归
    void traverse(tree root, void (*visit)(tree)) {
        struct stack s;
        tree tmp;
        init_stack(&s);
        if (root == NULL) return;
        push(&s, root);
        while (!is_empty(&s)) {
            tmp = pop(&s);
            visit(tmp);
            if (tmp->rchild != NULL) push(&s, tmp->rchild);
            if (tmp->lchild != NULL) push(&s, tmp->lchild);
        }
    }

    // 中序非递归
    void in_traverse(tree root, void (*visit)(tree)) {
        struct stack s;
        tree p = root;
        init_stack(&s);
        if (root == NULL) return;
        while (!is_empty(&s) || p != NULL) {
            while(p != NULL) {
                push(&s, p);
                p = p->lchild;
            }

            p = pop(&s);
            visit(p);
            p = p->right;
        }

    }

    // 后序遍历, two stack 参见最后一个链接.
    void postOrderTraversalIterativeTwoStacks(BinaryTree *root) {
      if (!root) return;
      stack<BinaryTree*> s;
      stack<BinaryTree*> output;
      s.push(root);
      while (!s.empty()) {
        BinaryTree *curr = s.top();
        output.push(curr);
        s.pop();
        if (curr->left)
          s.push(curr->left);
        if (curr->right)
          s.push(curr->right);
      }
      while (!output.empty()) {
        cout << output.top()->data << " ";
        output.pop();
      }
    }



广度优先遍历

    void traverse(tree root, void (*visit)(tree)) {
        struct queue q;
        if (root == NULL) return;
        init_queue(&q);
        put(&q, root);
        while (is_empty(&q)) {
            tmp = get(&q);
            visit(tmp);
            if (tmp->lchild != NULL) put(&q, tmp->lchild);
            if (tmp->rchild != NULL) put(&q, tmp->rchild);
        }
    }

### 分层遍历, 每层一行
1. 加null
2. parent,child size
3. 两个队列

    void PrintNodeByLevel(Node* root) {
        queue<Node*> Q;
        Q.push(root);
        Q.push(0);
        do {
            Node* node = Q.front();
            Q.pop();
            if (node) {
                cout << node->data << " ";
                if (node->pLeft)
                    Q.push(node->pLeft);
                if (node->pRight)
                    Q.push(node->pRight);
            }
            else if (!Q.empty()) {
                Q.push(0);
                cout << endl;
            }
        } while (!Q.empty());
    }

    void PrintNodeByLevel(Node *root) {
        int parentSize = 1, childSize = 0;
        Node * temp;
        queue<Node *> q;
        q.push(root);

        do {
            temp = q.front();
            cout << temp->data << "  ";
            q.pop();

            if (temp->pLeft != NULL)
            {
                q.push(temp->pLeft);
                childSize ++;
            }
            if (temp->pRight != NULL)
            {
                q.push(temp->pRight);
                childSize ++;
            }

            parentSize--;
            if (parentSize == 0)
            {
                parentSize = childSize;
                childSize = 0;
                cout << endl;
          }

        } while (!q.empty());
    }

### 图遍历

深度优先

    short int visited[V] = {0};
    void traverse(int k, void (*visit)(int)) {
        link t = adj[k];
        (*visit)(k);
        visited[k] = 1;
        while (t != NULL) {
            if (!visited[t->value]) traverse(t->next);
            t = t->next;
        }
    }

    void postOrderIterative(struct Node* root) {
        if (root == NULL) return;
         
        struct Stack* stack = createStack(MAX_SIZE);
        do {
            while (root) {
                if (root->right)
                    push(stack, root->right);
                push(stack, root);
     
                root = root->left;
            }
     
            root = pop(stack);
     
            if (root->right && peek(stack) == root->right) {
                pop(stack);
                push(stack, root);
                root = root->right;
            } else {
                printf("%d ", root->data);
                root = NULL;
            }
        } while (!isEmpty(stack));
    }

广度优先

    short int visited[V] = {0};
    void traverse(int k, void (*visit)(int)) {
        struct queue q;
        int tmp;
        link t;
        init_queue(&q);
        push(&q, k);
        while (!is_empty(&q)) {
            tmp = get(&q)
            if (!visited[tmp]) {
                visit(tmp); visited[tmp] = 1;
                for (t = adj[tmp]; t != NULL; t = t->next) {
                    if (!visited[t->value]) push(&q, t->value);
                }
            }
        }
    }

refer:

- [http://mingxinglai.com/cn/2014/07/traverse-binary-by-level/](http://mingxinglai.com/cn/2014/07/traverse-binary-by-level/)
- [http://leetcode.com/2010/04/binary-search-tree-in-order-traversal.html](http://leetcode.com/2010/04/binary-search-tree-in-order-traversal.html)
- [http://leetcode.com/2010/10/binary-tree-post-order-traversal.html](http://leetcode.com/2010/10/binary-tree-post-order-traversal.html)
- [http://noalgo.info/832.html](http://noalgo.info/832.html)
