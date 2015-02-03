Title: 已知一个数组不用除法构造另一个数组
Tags: algorithm, data structure, array
Date: 2014-06-12 24:00:00

>给定一数组a[N]，我们希望构造数组b [N]，其中b[j]=a[0]*a[1]…a[N-1] / a[j]，在构造过程中，不允许使用除法；要求O（1）空间复杂度和O（n）的时间复杂度

思路: 观察b[j]的构造公式，发现它实际上是由两部分相乘得到。左边是a[i]到a[j-1]的乘积，右边是a[j+1]到a[N-1]的乘积，中间的a[j]被除掉了。接下来就是怎么实现的问题了。先从左向右扫描a[N]数组，将坐标左边的元素累乘起来存入b[N]；然后可用一个变量保存右边数组元素乘积，从右向左扫描一遍，依次将b[N]和乘积变量相乘即可。


    void main()  {
        int a[N] = {5, 2, 3, 4, 1};
        int b[N];

        int i, j;

        int RightProduct = 1;
        b[0] = 1;

        for (i=1; i<N; i++)
        {
            b[i] = a[i-1]*b[i-1];
        }

        for (j=N-1; j>=0; j--)
        {
            b[j] = b[j] * RightProduct;
            RightProduct = RightProduct * a[j];
        }

        for (i=0; i<N; i++)
            cout << b[i] << " ";
        cout << endl;
    }

refer:

- [http://blog.csdn.net/CL512976287/article/details/21444171](http://blog.csdn.net/CL512976287/article/details/21444171)
