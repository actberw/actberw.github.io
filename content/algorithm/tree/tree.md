Title: 树的基本概念
Tags: algorithm, data structure
Date: 2014-09-02 12:00:00

1. 树的种类:
    - 无序树
    - 有序树
        - 二叉树
            - 完全二叉树
            - 满二叉树
            - 自平衡二叉查找树(avl, red-black)
        - 霍夫曼树
        - B树(B+, B*)
        - trie树, 后缀树
        - lsm树
        - COLA


### depth and height:

The depth of a node is the number of edges from the node to the tree's root node.
A root node will have a depth of 0.

The height of a node is the number of edges on the longest path from the node to a leaf.
A leaf node will have a height of 0.

![tree height](/img/tree-height.png)

### path length

The path length can have simple recursive definition as follows.
The path length of a tree with N nodes is the sum of the path lengths of the subtrees of its root plus N-1.
It is the sum of all the distances between the nodes and the root.


refer:

- [http://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height](http://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height)
