Title: 二叉树基本概念

###  平衡二叉树

平衡二叉树或者是一个空树， 或者左右子树都是平衡二叉树, 且左右子树的高度之差的绝对值不超过1.

    bool is_balance_tree(BinaryTreeNode *root, int *depth)  {
        int left_depth, right_depth;
        bool left_result, right_result;
        if(root == NULL) {
            *depth = 0;
            return true;
        }
        left_result = is_balance_tree(root->lchild, &left_depth);
        if (left_result) {
            right_result = is_balance_tree(root->rchild, &right_depth);
            *depth = max(left_depth, right_depth) + 1;
            return right_result && abs(left_depth - right_depth) <= 1;
        }
        return false;
    }

平衡树高度保持在O(lgn), 查找性能最好.

使平衡二叉树保持平衡的基本思想是: 每当插入时检查插入路径上的急诶但是否因为插入而导致了不平衡, 若是则找出其中的最小不平衡二叉树, 在保持二叉排序树的特性下调整最小不平衡树中节点之间的关系, 使之达到平衡.

有四种种情况可能导致二叉查找树不平衡，分别为:

- LL：插入一个新节点到根节点的左子树（Left）的左子树（Left），导致根节点的平衡因子由1变为2
- RR：插入一个新节点到根节点的右子树（Right）的右子树（Right），导致根节点的平衡因子由-1变为-2
- LR：插入一个新节点到根节点的左子树（Left）的右子树（Right），导致根节点的平衡因子由1变为2
- RL：插入一个新节点到根节点的右子树（Right）的左子树（Left），导致根节点的平衡因子由-1变为-2

针对四种种情况可能导致的不平衡，可以通过旋转使之变平衡, 有两种基本的旋转:

- 左旋转：将根节点旋转到（根节点的）右孩子的左孩子位置
- 右旋转：将根节点旋转到（根节点的）左孩子的右孩子位置

### 完全二叉树和满二叉树
满二叉树，完全二叉树


bool is_complete_binary_tree(tree root) {
    bool result, flag;
    tree tmp;
    struct queue q;
    if (root == NULL) return true;
    queue_init(&q);
    put(&q, root);
    
    while (!is_empty(&q)) {
        tmp = get(&q);
        if (flag) {
            if (tmp->lchild != NULL || tmp->rchild != NULL) {
                result = false;
                break;
            }
        } else {
            if (tmp->lchild != NULL && tmp->rchild != NULL) {
                put(&q, tmp->lchild);
                put(&q, tmp->rchild);
            } else if (tmp->lchild != NULL && tmp->rchild == NULL) {
                put(&q, tmp->lchild);
                flag = true; 
            } else if (tmp->lchild == NULL && tmp->rchild != NULL) {
                result = false;
                break;
            } else {
                flag = true;
            }
        }
    }

    return result;
}

### 二叉高度和节点数

    int count(tree root) {
        if (root == NULL) return 0;
        return count(root->lchild) + count(root->rchild) + 1;
    }

    int height(tree root) {
        if (root == NULL) return -1; //start from zero;
        return max(height(root->lchild), height(root->rchild)) + 1;
    }

堆, huffman, 平衡二叉树(avl, red-black)

### 二叉树镜像

    void mirror(struct node* node) {
      if (node==NULL) 
        return;  
      else {
        struct node* temp;
         
        /* do the subtrees */
        mirror(node->left);
        mirror(node->right);
     
        /* swap the pointers in this node */
        temp        = node->left;
        node->left  = node->right;
        node->right = temp;
      }
    }


### Convert a given Binary Tree to Doubly Linked List

    void convert_bst_to_dlist(tree root, link *head, link *prev) {
        if (root == NULL) return;

        convert_bst_to_dlist(root->lchild, head, prev);
        if (*head == NULL)
            *head = root;
        root->lchild = prev; 
        if (prev != NULL) 
            *prev->rchild = root;

        *prev = root;
        convert_bst_to_dlist(root->rchild, head, prev);
    }

https://www.zhihu.com/question/27378693

### 重建二叉树

>Given preorder and inorder traversal of a tree, construct the binary tree.

    struct node* buildTree(char in[], char pre[], int inStrt, int inEnd) {
      static int preIndex = 0;
     
      if(inStrt > inEnd)
         return NULL;
     
      struct node *tNode = newNode(pre[preIndex++]);
     
      if(inStrt == inEnd)
        return tNode;
     
      /* Else find the index of this node in Inorder traversal */
      int inIndex = search(in, inStrt, inEnd, tNode->data);
     
      /* Using index in Inorder traversal, construct left and
         right subtress */
      tNode->left = buildTree(in, pre, inStrt, inIndex-1);
      tNode->right = buildTree(in, pre, inIndex+1, inEnd);
     
      return tNode;
    }

如果是inorder和postorder也是一样的, 不过是postorder需要倒序遍历.

refer:

- [http://dongxicheng.org/structure/avl/](http://dongxicheng.org/structure/avl/)
- [http://www.cppblog.com/guogangj/archive/2009/10/29/99729.html](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888)
- [http://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/](http://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/)
- [http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/](http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/)
- [http://blog.csdn.net/luckyxiaoqiang/article/details/7518888](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888)
- [http://zhedahht.blog.163.com/blog/static/254111742007127104759245/](http://zhedahht.blog.163.com/blog/static/254111742007127104759245/)
- [http://leetcode.com/2011/04/construct-binary-tree-from-inorder-and-preorder-postorder-traversal.html](http://leetcode.com/2011/04/construct-binary-tree-from-inorder-and-preorder-postorder-traversal.html)
- [http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/](http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/)
- [http://leetcode.com/2010/09/saving-binary-search-tree-to-file.html](http://leetcode.com/2010/09/saving-binary-search-tree-to-file.html)
- [http://leetcode.com/2010/09/serializationdeserialization-of-binary.html](http://leetcode.com/2010/09/serializationdeserialization-of-binary.html)
