Title: 直方图中长方形的最大面积(Largest Rectangular Area in a Histogram)
Tags: algorithm
Date: 2014-06-14

>Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 2, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)


![hisgogram](/img/histogram.png)


算法步骤: 

- Create an empty stack.
- Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
    - a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
    - b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
- If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.

pop出栈的时候长方形的左右边界通过栈顶元素和当前遍历直方图的索引来确定的.


    int get_max_area(int *arr, int n) {
        int i = 0, tmp, max_area = 0, curr_area;
        stack<int> s;
        while (i < n) {
            if (s.empty() || s.top() <= arr[i])
                s.push(i++);
            else {
                tmp = s.top();
                s.pop();
                curr_area = arr[tmp] * (s.empty() ? i : (i - 1 - s.top()));
                if (curr_area > max_area)
                    max_area = max_area
            }

        }

        while (!s.empty()) {
            tmp = s.top();
            s.pop();
            curr_area = arr[tmp] * (s.empty() ? i : (i - 1 - s.top()));
            if (curr_area > max_area)
                max_area = max_area
        }

        return max_area;
    }


refer:

- [http://www.geeksforgeeks.org/largest-rectangle-under-histogram/](http://www.geeksforgeeks.org/largest-rectangle-under-histogram/)
