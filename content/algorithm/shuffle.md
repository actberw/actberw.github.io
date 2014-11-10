Title: 洗牌算法之Knuth Shuffle 
Tags: algorithm, random, shuffle
Date: 2014-09-05

算法描述:
>Let X1, X2…. XN be the set of N numbers to be shuffled.

>Set j to N  
Generate a random number R. (uniformly distributed between 0 and 1)  
Set k to (jR+1). k is now a random integer, between 1 and j.  
Exchange Xk and Xj  
Decrease j by 1.  
If j > 1, return to step 2.

    void shuffle(int *array, int len) {  
        int rand;  
        for (int i = len; i >=0; i--) {  
            rand = _rand(0, i); //_rand(int min, int max)是一个随机数生成器。
            swap(array[i], array[rand]);  
        }  
    } 

refer:

- [http://blog.csdn.net/dwyane_mys/article/details/8053896](http://blog.csdn.net/dwyane_mys/article/details/8053896)
- [http://en.wikipedia.org/wiki/Random_permutation](http://en.wikipedia.org/wiki/Random_permutation)
- [http://blog.csdn.net/v_july_v/article/details/7329314](http://blog.csdn.net/v_july_v/article/details/7329314)

