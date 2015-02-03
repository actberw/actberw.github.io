Title: 二叉排序树(binary search tree)
Tags: bst, data structure
Date: 2014-09-02 13:00:00

### 判断是否是bst

    bool isBSTHelper(BinaryTree *p, int low, int high) {
      if (p == NULL) return true;
      if (low < p->data && p->data < high)
        return isBSTHelper(p->left, low, p->data) && 
               isBSTHelper(p->right, p->data, high);
      else
        return false;
    }
     
    bool isBST(BinaryTree *root) {
      // INT_MIN and INT_MAX are defined in C++'s <climits> library
      return isBSTHelper(root, INT_MIN, INT_MAX);  
    }

也可以中序遍历, 查看前一个值比后面的一个小.

    bool isBSTInOrderHelper(BinaryTree *p, int *prev) {
      if (!p) return true;
      if (isBSTInOrderHelper(p->left, prev)) {
        if (p->data > *prev) {
          *prev = p->data;
          return isBSTInOrderHelper(p->right, prev);
        } else {
          return false;
        }
      }
      else {
        return false;
      }
    }

    bool isBSTInOrder(BinaryTree *root) {
      int prev = INT_MIN;
      return isBSTInOrderHelper(root, &prev);
    }

### 查找 

    typedef struct bst_node {    
        char data;    
        struct bst_node *lchild,*rchild;    
        
    } bst_node, *bst_tree;
    
    bst_tree search(bst_tree root, char data, bst_node ** parent) {
        bst_node *p = root, *parent = NULL; 
        while (p != NULL) {
            if (p->data == data) return p;
            *parent = p;
            if (data < p->data)  p = p->lchild;
            else  p = p->rchild;
        }
        return NULL;
    }


### 插入

    bool bst_insert(bst_tree *root, char data) {
        bst_node *parent, n;
        if (search(data, &parent)) return 0; //已经存在
        n = malloc(sizeof(bst_node)) ;
        n->data = data; n->lchild = n->rchild = NULL; 
        if (parent == NULL) *root = n;
        else if (data < parent->data) parent->lchild = n; // 不用管左右父节点的左右子树是否位空.
        else parent->rchild = n;
        return 1;
    }

### 删除

四种情况:

- 是叶子节点, 将其父节点相应的指针清空
- 右子树为空, 则左子树顶替它的位置
- 左子树为空, 则右子树顶替它的位置
- 如果左右都不为空

        bool bst_delete(bst_tree *root, char data) {
            bst_tree p, s, parent;
            p = search(*root, &parent);
            if (p == NULL) return 0;

            if (p->lchild != NULL && p->rchild != NULL) {
                s = p->rchild;
                while (s->lchild != NULL) {
                    parent = s;
                    s = s->lchild;
                }

                p->data = s->data; // exchange p and s
                p = s;
            }

            s = (p->lchild != NULL) ? p->lchild: p->rchild
            if (p == *root) *root = s;

            if (parent->data < s->data) parent->rchild = s;
            else parent->lchild = s;
            
            free(p);
            return true;
        }

### 构建bst

    tree_tree *build_bst(int *arr, int len):
        int i;
        bst_tree root = NULL;
        for(i = 0; i < len; i++):
            tree = bst_insert(&root, arr[i])
        return root;

refer:

- [http://leetcode.com/2010/09/determine-if-binary-tree-is-binary.html](http://leetcode.com/2010/09/determine-if-binary-tree-is-binary.html)
