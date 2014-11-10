Title: 循环的时间复杂度
Tags: algorithm analysis
Date: 2014-06-07 16:00:00
1. O(1)  
  一个函数调用或是一组语句都认为是O(1)的复杂度  (如果没有调用不包含循环，递归或其他非常量复杂度的函数), 如果循环的次数是一个常量，则也认为是 O(1).
2. O(n)  
  如果在一个大小为n循环中，循环变量按照一个常量C递增或递减，这个循环的复杂度就为O(n).

        // c是常量  
        for (int i = 1; i <= n; i += c) { 
             // some O(1) expressions
        }

        for (int i = n; i > 0; i -= c) {
             // some O(1) expressions
        }

3. O(n^c)  
  嵌套循环的时间复杂度等于行最内层语句执行的次数。例如，下面的示例循环具有为O(n^2)的时间复杂度

        for (int i = 1; i <=n; i += c) {
            for (int j = 1; j <=n; j += c) {
               // some O(1) expressions
            }
        }

        for (int i = n; i > 0; i += c) {
            for (int j = i+1; j <=n; j += c) {
               // some O(1) expressions
            }
        }

4. O(Log n)  
  如果在一个大小为n循环中，循环变量按照一个常量C的进行倍数的递增或递减，这个循环的复杂度就为O(Log  n).

        for (int i = 1; i <=n; i *= c) {
            // some O(1) expressions
        }

        for (int i = n; i > 0; i /= c) {
            // some O(1) expressions
        }

5. O(Log Log n)  

        // c为比1大的常量
        for (int i = 2; i <=n; i = pow(i, c)) {
            // some O(1) expressions
        }

        //这里的 fun 函数可以是sqrt 或 cuberoot 或任何其他恒定的根

        for (int i = n; i > 0; i = fun(i)) {
            // some O(1) expressions
        }

当有连续的循环，我们计算时间复杂度为时间各个循环的复杂总和。

refer:

- [http://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/](http://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/)
- [http://www.acmerblog.com/analysis-of-loops-5069.html](http://www.acmerblog.com/analysis-of-loops-5069.html)
