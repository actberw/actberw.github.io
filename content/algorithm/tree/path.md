Title: 有关路径的题目

### 二元树中和为某一值的所有路径

>输入一个整数和一棵二元树。从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径。打印出和与输入整数相等的所有路径。
例如输入整数22和如下二元树
>
                                            10  
                                           /   \  
                                          5     12  
                                        /   \   
                                     　4     7   
则打印出两条路径：10, 12和10, 5, 7。

    //二元树结点的数据结构定义为：

    struct BinaryTreeNode // a node in the binary tree
    {
          int              m_nValue; // value of node
          BinaryTreeNode  *m_pLeft;  // left child of node
          BinaryTreeNode  *m_pRight; // right child of node
    };
    
    void FindPath (
          BinaryTreeNode*   pTreeNode,    // a node of binary tree
          int               expectedSum,  // the expected sum
          std::vector<int>& path,         // a path from root to current node
          int&              currentSum    // the sum of path
    )
    {
          if(!pTreeNode)
                return;

          currentSum += pTreeNode->m_nValue;
          path.push_back(pTreeNode->m_nValue);

          // if the node is a leaf, and the sum is same as pre-defined, 
          // the path is what we want. print the path
          bool isLeaf = (!pTreeNode->m_pLeft && !pTreeNode->m_pRight);
          if(currentSum == expectedSum && isLeaf)
          {    
               std::vector<int>::iterator iter = path.begin();
               for(; iter != path.end(); ++ iter)
                     std::cout << *iter << '\t';
               std::cout << std::endl;
          }

          // if the node is not a leaf, goto its children
          if(pTreeNode->m_pLeft)
                FindPath(pTreeNode->m_pLeft, expectedSum, path, currentSum);
          if(pTreeNode->m_pRight)
                FindPath(pTreeNode->m_pRight, expectedSum, path, currentSum);

          // when we finish visiting a node and return to its parent node,
          // we should delete this node from the path and 
          // minus the node's value from the current sum
          currentSum -= pTreeNode->m_nValue;
          path.pop_back();
    } 

### maximum sum leaf to root path in a Binary Tree
>Given a Binary Tree, find the maximum sum path from a leaf to root. For example, in the following tree, there are three leaf to root paths 8->-2->10, -4->-2->10 and 7->10. The sums of these three paths are 16, 4 and 17 respectively. The maximum of them is 17 and the path for maximum is 7->10.

Solution
1) First find the leaf node that is on the maximum sum path. In the following code getTargetLeaf() does this by assigning the result to *target_leaf_ref.
2) Once we have the target leaf node, we can print the maximum sum path by traversing the tree. In the following code, printPath() does this.

    #include<stdio.h>
    #include<limits.h>
     
    /* A tree node structure */
    struct node
    {
        int data;
        struct node *left;
        struct node *right;
    };
     
    // A utility function that prints all nodes on the path from root to target_leaf
    bool printPath (struct node *root, struct node *target_leaf) {
        // base case
        if (root == NULL)
            return false;
     
        if (root == target_leaf || printPath(root->left, target_leaf) ||
                printPath(root->right, target_leaf) )
        {
            printf("%d ", root->data);
            return true;
        }
     
        return false;
    }
     
    void getTargetLeaf (struct node *node, int *max_sum_ref, int curr_sum, struct node **target_leaf_ref) {
        if (node == NULL)
            return;
     
        // Update current sum to hold sum of nodes on path from root to this node
        curr_sum = curr_sum + node->data;
     
        // If this is a leaf node and path to this node has maximum sum so far,
        // then make this node target_leaf
        if (node->left == NULL && node->right == NULL)
        {
            if (curr_sum > *max_sum_ref)
            {
                *max_sum_ref = curr_sum;
                *target_leaf_ref = node;
            }
        }
     
        // If this is not a leaf node, then recur down to find the target_leaf
        getTargetLeaf (node->left, max_sum_ref, curr_sum, target_leaf_ref);
        getTargetLeaf (node->right, max_sum_ref, curr_sum, target_leaf_ref);
    }
     
    // Returns the maximum sum and prints the nodes on max sum path
    int maxSumPath (struct node *node) {
        // base case
        if (node == NULL)
            return 0;
     
        struct node *target_leaf;
        int max_sum = INT_MIN;
     
        // find the target leaf and maximum sum
        getTargetLeaf (node, &max_sum, 0, &target_leaf);
     
        // print the path from root to the target leaf
        printPath (node, target_leaf);
     
        return max_sum;  // return maximum sum
    }

### Binary Tree Maximum Path Sum
>Given a binary tree, find the maximum path sum.

>The path may start and end at any node in the tree.

    /**
     * Definition for binary tree
     * public class TreeNode {
     *     int val;
     *     TreeNode left;
     *     TreeNode right;
     *     TreeNode(int x) { val = x; }
     * }
     */
    public class Solution {
        int result = Integer.MIN_VALUE;
        public int maxPathSum(TreeNode root) {
            maxPath(root);
            return result;
        }
        
        private int maxPath(TreeNode root){
            if(root == null)
                return 0;
            int left = maxPath(root.left);
            int right = maxPath(root.right);
            int arch = left + right + root.val;
            int pass_up = Math.max(Math.max(left,right)+root.val,root.val);
            result = Math.max(result,Math.max(arch,pass_up));
            return pass_up;
        }
    }

refer:

- [http://zhedahht.blog.163.com/blog/static/254111742007228357325/](http://zhedahht.blog.163.com/blog/static/254111742007228357325/)
- [http://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number/](http://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number/)
- [http://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/](http://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/)
- [http://www.elvisyu.com/binary-tree-maximum-path-sum/](http://www.elvisyu.com/binary-tree-maximum-path-sum/)
- [http://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/](http://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/)
