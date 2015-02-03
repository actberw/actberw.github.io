Title: Stock Buy Sell to Maximize Profit 
Tags: algorithm
Date: 2014-09-07

>Say you have an array for which the ith element is the price of a given stock on day i.

>If you were only permitted to buy one share of the stock and sell one share of the stock, design an algorithm to find the best times to buy and sell.

如果是买卖一次则可以参照数组中两个元素最大差值来解决.

    int maxDiff(int arr[], int arr_size) {
      int max_diff = arr[1] - arr[0];
      int min_element = arr[0];
      int i;
      for(i = 1; i < arr_size; i++)
      {       
        if(arr[i] - min_element > max_diff)                               
          max_diff = arr[i] - min_element;
        if(arr[i] < min_element)
             min_element = arr[i];                     
      }
      return max_diff;
    }

如果要买卖多次, Solution:
- Find the local minima and store it as starting index. If not exists, return.
- Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
- Update the solution (Increment count of buy sell pairs)
- Repeat the above steps if end is not reached.

实际就是找一段上升子序列，在每段上升子序列两端买进和卖出, 代码如下

    struct Interval {
        int buy;
        int sell;
    };

    void stockBuySell(int price[], int n) {
        // Prices must be given for at least two days
        if (n == 1)
            return;
     
        int count = 0; // count of solution pairs
     
        // solution vector
        Interval sol[n/2 + 1];
     
        // Traverse through given price array
        int i = 0;
        while (i < n-1)
        {
            // Find Local Minima. Note that the limit is (n-2) as we are
            // comparing present element to the next element. 
            while ((i < n-1) && (price[i+1] <= price[i]))
                i++;
     
            // If we reached the end, break as no further solution possible
            if (i == n-1)
                break;
     
            // Store the index of minima
            sol[count].buy = i++;
     
            // Find Local Maxima.  Note that the limit is (n-1) as we are
            // comparing to previous element
            while ((i < n) && (price[i] >= price[i-1]))
                i++;
     
            // Store the index of maxima
            sol[count].sell = i-1;
     
            // Increment count of buy/sell pairs
            count++;
        }
     
        // print solution
        if (count == 0)
            printf("There is no day when buying the stock will make profit\n");
        else {
           for (int i = 0; i < count; i++)
              printf("Buy on day: %d\t Sell on day: %d\n", sol[i].buy, sol[i].sell);
        }
     
        return;
    }

refer:

- [http://leetcode.com/2010/11/best-time-to-buy-and-sell-stock.html](http://leetcode.com/2010/11/best-time-to-buy-and-sell-stock.html)
- [http://www.geeksforgeeks.org/stock-buy-sell/](http://www.geeksforgeeks.org/stock-buy-sell/)
- [http://courses.csail.mit.edu/iap/interview/Hacking_a_Google_Interview_Handout_3.pdf](http://courses.csail.mit.edu/iap/interview/Hacking_a_Google_Interview_Handout_3.pdf)
- [http://www.geeksforgeeks.org/maximum-difference-between-two-elements/](http://www.geeksforgeeks.org/maximum-difference-between-two-elements/)
- [http://www.cnblogs.com/xiongqiangcs/p/3806828.html](http://www.cnblogs.com/xiongqiangcs/p/3806828.html)
