Title: lca和节点最大距离

### lca

如果是bst

    struct node *lca(struct node* root, int n1, int n2) {
        if (root == NULL) return NULL;
     
        // If both n1 and n2 are smaller than root, then LCA lies in left
        if (root->data > n1 && root->data > n2)
            return lca(root->left, n1, n2);
     
        // If both n1 and n2 are greater than root, then LCA lies in right
        if (root->data < n1 && root->data < n2)
            return lca(root->right, n1, n2);
     
        return root;
    }


refer:

- [http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/](http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/)
http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
http://leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html
http://leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html
http://blog.csdn.net/yxc135/article/details/10081419
http://dongxicheng.org/structure/lca-rmq/
http://blog.csdn.net/v_july_v/article/details/18312089
http://www.zhihu.com/question/19957473


### 节点最大距离 

递归解法:

- 如果二叉树为空，返回0，同时记录左子树和右子树的深度，都为0
- 如果二叉树不为空，最大距离要么是左子树中的最大距离，要么是右子树中的最大距离，要么是左子树节点中

    struct NODE
    {
        NODE *pLeft;
        NODE *pRight;
    };
     

    int GetMaximumDistance(NODE* root, int *depth) {
        int lhs, rhs, ldepth, rdepth;
        if (root == NULL)
        {
            *depth = -1;
            return 0;
        }
     
        lhs = GetMaximumDistance(root->pLeft, &ldepth);
        rhs = GetMaximumDistance(root->pRight, &rdepth);
     
        depth = max(ldepth, rdepth) + 1;
        return max(max(lhs, rhs), ldepth + rdepth + 2);
    }

refer:

- [http://blog.csdn.net/luckyxiaoqiang/article/details/7518888](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888)
- [http://www.cnblogs.com/miloyip/archive/2010/02/25/binary_tree_distance.html](http://www.cnblogs.com/miloyip/archive/2010/02/25/binary_tree_distance.html)
- [http://www.geeksforgeeks.org/diameter-of-a-binary-tree/](http://www.geeksforgeeks.org/diameter-of-a-binary-tree/)
