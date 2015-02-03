Title: 关于坐标点题目
Tags: algorithm, point
Date: 2014-08-13

### 最近点对
> 在二维平面上的n个点中，如何快速的找出最近的一对点.

见 <编程之美>
已知集合S中有n个点，分治法的思想就是将S进行拆分，分为2部分求最近点对。算法每次选择一条垂线L，将S拆分左右两部分为SL和SR，L一般取点集S中所有点的中间点的x坐标来划分，这样可以保证SL和SR中的点数目各为n/2，
依次找出这两部分中的最小点对距离：δL和δR，记SL和SR中最小点对距离δ = min(δL，δR)
以L为中心，δ为半径划分一个长带，最小点对还有可能存在于SL和SR的交界处，如下图2左图中的虚线带，p点和q点分别位于SL和SR的虚线范围内，在这个范围内，p点和q点之间的距离才会小于δ，最小点对计算才有意义

refer:

- [http://sxnuwhui.blog.163.com/blog/static/137068373201264104915935/](http://sxnuwhui.blog.163.com/blog/static/137068373201264104915935/)
- [http://my.oschina.net/u/923087/blog/279281](http://my.oschina.net/u/923087/blog/279281)

### 最远点对
http://blog.csdn.net/hackbuteer1/article/details/7484746


### 定长线段最多覆盖点的个数 

>给定一系列x轴的点坐标，例如 1，3，7，8，9，11这些坐标升序放在数组中，现在给一根绳子，长度为4，问绳子最多能覆盖的点数有多少，例如绳子放前面只能覆盖两个点，1,3，如果放后面能覆盖4个点。

两个指针前后跑的思路：两个指针往前走，前面的负责加，后面的负责减，前面的每次都移动，如果点间隔长度大于绳子长度，后面指针移动。

    int calculateNum(int * arr, int pointNum, int segLen) {
        if(arr == NULL || pointNum <= 0 || segLen <= 0)   return 0;
     
        int frontPtr = 0, rearPtr = 1, coverMax = 1;
        while(rearPtr < pointNum) {
            while(arr[rearPtr] - arr[frontPtr] > segLen)
            {
                ++frontPtr;
            }
            coverMax = (rearPtr-frontPtr+1) > coverMax ? (rearPtr-frontPtr+1) : coverMax;
            ++rearPtr;
        }
        return coverMax;
    }

refer:

- [http://www.ahathinking.com/archives/181.html](http://www.ahathinking.com/archives/181.html)

### Max Points on a Line

>Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

思路: 以某点O为中心，计算它和其他点的斜率，如果有两个点A、B和O点形成的斜率相等，那么ABO三点是共线的，如果有多个点和O的斜率相等，那么这多个点和O也是共线的，因此我们可以求出包含O的所有直线中点数最多的直线，会得到一个最大共线点数k(O)，如果和O点重复的点有n个（除了O本身），那么K(O) = K(O) + n。这一步的计算中，为了提高效率，我们可以用哈希表来保存某个斜率对应的点的数目。

对数组中的每一个点i，按照第一步计算得到每个点最大点数K(i) , 从k(i)中选取最大的就是本题的解
http://www.cnblogs.com/TenosDoIt/p/3444086.html
