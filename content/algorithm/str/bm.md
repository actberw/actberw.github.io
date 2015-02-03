Title: BM(Boyer-moore) 算法
Tags: algorithm, c, str
Date: 2015-01-14


后缀匹配是指模式串的比较从右到左，模式串的移动也是从左到右的匹配过程，经典的BM算法其实是对后缀蛮力匹配算法的改进。

    i = 0；
    while (i <= strlen(T) - strlen(P)) {
       for (j = strlen(P) - 1; j >= 0 && P[j] ==T[i + j]; --j)
       if (j < 0)
           printf("Pattern found at index %d \n", i);
       else
          ++i；
    }


为了实现更快移动模式串，BM算法定义了两个规则，好后缀规则和坏字符规则，如下图可以清晰的看出他们的含义。利用好后缀和坏字符可以大大加快模式串的移动距离，不是简单的++j，而是j += max(shift(好后缀), shift(坏字符))

![bm-suffix](/img/bm-suffix.png)


refer:

- [http://www.searchtb.com/2011/07/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%82%A3%E4%BA%9B%E4%BA%8B%EF%BC%88%E4%B8%80%EF%BC%89.html](http://www.searchtb.com/2011/07/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%82%A3%E4%BA%9B%E4%BA%8B%EF%BC%88%E4%B8%80%EF%BC%89.html)
- [http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html](http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
- [http://www.geeksforgeeks.org/pattern-searching-set-7-boyer-moore-algorithm-bad-character-heuristic/](http://www.geeksforgeeks.org/pattern-searching-set-7-boyer-moore-algorithm-bad-character-heuristic/)
