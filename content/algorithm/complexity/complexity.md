Title: 算法复杂度分析
Tags: algorithm, algorithm analysis
Date: 2014-06-07 15:00:00
slug:complexity-analysis

  算法的复杂度是用来衡量算法运行所需要的计算机资源（时间、空间）的量, 分为时间复杂度和空间复杂度. 时间复杂度是指衡量算法执行时间的长短；空间复杂度是指衡量算法所需存储空间的大小。

### Landau符号  

Landau符号其实是由德国数论学家保罗·巴赫曼（Paul Bachmann）在其1892年的著作《解析数论》首先引入，由另一位德国数论学家艾德蒙·朗道（Edmund Landau）推广。Landau符号的作用在于用简单的函数来描述复杂函数行为，给出一个上或下（确）界。在计算算法复杂度时一般只用到大O符号，Landau符号体系中的小o符号、Θ符号等等比较不常用。这里的O，最初是用大写希腊字母，但现在都用大写英语字母O；小o符号也是用小写英语字母o，Θ符号则维持大写希腊字母Θ.

Asymptotic comparison  | operatorNumeric comparison operator|------
-----------------------|-----------------------------------|------
f(n) = o(g(n)) | ∀ε>0,∃$n_0$∈ℕ,∀n≥$n_0$,f(n)/g(n)<ε | f的阶低于g的阶
f(n) = O(g(n)) | ∃c>0,$n_0$∈ℕ,∀n≥$n_0$,f(n)≤cg(n)   | f的阶不高于g的阶。
f(n) = Ω(g(n)) | ∃c>0,$n_0$∈ℕ,∀n≥$n_0$,f(n)≥cg(n)   | f的阶不低于g的阶。
f(n) = θ(g(n)) | ⟺ f(n)=O(g(n))&&f(n)=Ω(g(n)) | f的阶等于g的阶。

### 大O表示法  

f (n) = Ο(g (n)) 表示存在一个常数C，使得在当n趋于正无穷时总有 f (n) ≤ C * g(n)。简单来说，就是f(n)在n趋于正无穷时最大也就跟g(n)差不多大。虽然对g(n)没有规定，但是一般都是取尽可能简单的函数。例如，O($2n^2+n+1$) = O ($3n^2+n+3$) = O ($7n^2+n$) = O ($n^2$) ，一般都只用O($n^2$)表示就可以了。

注意到大O符号里隐藏着一个常数C，所以g(n)里一般不加系数。如果把f(n)当做一棵树，那么O(g(n))所表达的就是树干，只关心其中的主干，其他的细枝末节全都抛弃不管。

### 渐进分析法 (asymptotic behavior)

Asymptotic Analysis is the big idea that handles above issues in analyzing algorithms. In Asymptotic Analysis, we evaluate the performance of an algorithm in terms of input size (we don’t measure the actual running time). We calculate, how does the time (or space) taken by an algorithm increases with the input size.

随着问题得规模n得增加丢掉增长慢得因子，只保留增长最快得那个(参见refer[5]).

- f(n) = 109 gives f(n) = O(1)
- f(n) = 5n + 12 gives f(n) = O(n)
- f(n) = $n^2 + 3n + 112$ gives f(n) = O($n^2$)


### 时间复杂度和渐近时间复杂度  

  一个是时间复杂度，一个是渐近时间复杂度。前者是某个算法的时间耗费，它是该算法所求解问题规模n的函数，而后者是指当问题规模趋向无穷大时，该算法时间复杂度的数量级, 含有。

### 常用的函数  
  一个良好的算法能够对性能起到关键作用，因此性能改进的首要点是对算法的改进。在算法的时间复杂度排序上依次是:
O(1) -> O(lg n) -> O(n) -> O(n lg n) -> O($n^2$) -> O($n^3$) -> O($n^k$) -> O($k^n$) -> O(n!), 注: 在算法复杂度分析中，lg通常表示以2为底的对数。

refer:

 - [0][Asymptotic Notations][http://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/]
 - [1][常用算法的复杂度](http://bigocheatsheet.com/)
 - [2][http://www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html](http://www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html)
 - [3][http://discrete.gr/complexity/](http://discrete.gr/complexity/)
 - [4][princeton lectures](http://aofa.cs.princeton.edu/home/)
 - [5][渐进式分析法](http://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

