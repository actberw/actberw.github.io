The order, or branching factor, b of a B+ tree measures the capacity of nodes (i.e., the maximum number of children nodes) for internal nodes in the tree. 



B+ trees don't have data associated with interior nodes

The leaf nodes of B+ trees are linked, so doing a full scan of all objects in a tree requires just one linear pass through all the leaf nodes.(a leaf node may include a pointer to the next leaf node to speed sequential access)

Because B trees contain data with each key, frequently accessed nodes can lie closer to the root, and therefore can be accessed more quickly.

minimum degree

http://courses.cs.washington.edu/courses/cse326/08sp/lectures/11-b-trees.pdf
http://en.wikibooks.org/wiki/Algorithm_Implementation/Trees/B%2B_tree
http://www.cnblogs.com/yangecnu/p/introduce-b-tree-and-b-plus-tree.html
http://www.geeksforgeeks.org/b-tree-set-1-introduction-2/
http://www.di.ufpb.br/lucidio/Btrees.pdf

http://blog.jobbole.com/79311/
http://blog.codinglabs.org/articles/theory-of-mysql-index.html
http://www.zhihu.com/question/19836260
http://geeksquiz.com/data-structure/b-and-b-trees/
http://courses.cs.washington.edu/courses/cse326/08sp/lectures/11-b-trees.pdf
http://blog.csdn.net/v_JULY_v/article/details/6530142
http://dblab.cs.toronto.edu/courses/443/2014/05.btree-index.html

