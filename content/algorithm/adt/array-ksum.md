Title: K Sum 问题
Tags: algorithm, 2sum, 3sum
Date: 2014-08-03

### Two Sum
>Given an array of integers, find two numbers such that they add up to a specific target number.

>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

>You may assume that each input would have exactly one solution.

>Input: numbers={2, 7, 11, 15}, target=9

>Output: index1=1, index2=2

两种解法:

- (不适合返回索引的)排序, 然后用二分查找差值, 或者首位两个指针left, right, 如果array[left] + array[right] > target 则 right--, array[left] + array[right] < target 则left++, 等于则返回

- 用hashMap


hashMap 的实现

    public class Solution {
        public int[] twoSum(int[] arr, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] result = new int[2];
     
        for (int i = 0; i < arr.length; i++) {
            if (map.containsKey(arr[i])) {
                int index = map.get(arr[i]);
                result[0] = index+1 ;
                result[1] = i+1;
                break;
            } else {
                map.put(target - arr[i], i);
            }
        }
     
        return result;
        }
    }

### three sum 
>Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

>    For example, given array S = {-1 0 1 2 -1 -4},

>    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

Note:  
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

To avoid duplicate, we can take advantage of sorted arrays, i.e., move pointers by >1 to use same element only once.

这里不是要求返回索引而是元素值, 所以可以进行排序处理.

    ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        Arrays.sort(num);
        for (int i = 0; i < num.length - 2; i++) {

                if(i > 0 && num[i] == num[i-1]) continue; // avoid duplicate solutions
                int two_sum = 0 - num[i];
                int l = i + 1;
                int r = num.length - 1;
     
                while (l < r) {
                    if (num[l] + num[r] == two_sum) {
                        ArrayList<Integer> temp = new ArrayList<Integer>();
                        temp.add(num[i]);
                        temp.add(num[l]);
                        temp.add(num[r]);
     
                        result.add(temp);
                        l++;
                        r--;

                    } else if (num[l] + num[r] < two_sum) {
                        l++;
                    } else {
                        r--;
                    }
                }
     
            }
        }
        
    }

### three Sum Closest 
>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution. For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

This problem is similar with 3 Sum. This kind of problem can be solve by using similar approach, i.e., two pointers from both left and right.

    public class Solution {
        public int threeSumClosest(int[] arr, int target) {
            int min = Integer.MAX_VALUE;
            int result = 0;
     
            Arrays.sort(arr);
     
            for (int i = 0; i < arr.length; i++) {
                int l = i + 1;
                int r = arr.length - 1;
                while (l < r) {
                    int sum = arr[i] + arr[l] + arr[r];
                    int diff = Math.abs(sum - target);
                    if (diff < min) {
                        min = diff;
                        result = sum;
                    }
                    if (sum <= target) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
     
            return result;
        }
    }

### four sum
>Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
>   For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

>    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

A typical k-sum problem. Time is N to the poser of (k-1).

    public ArrayList<ArrayList<Integer>> fourSum(int[] arr, int target) {
        Arrays.sort(arr);
     
        HashSet<ArrayList<Integer>> hashSet = new HashSet<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < arr.length; i++) {

            if(i > 0 && arr[i] == arr[i-1]) continue; // avoid first element duplicate

            for (int j = i + 1; j < arr.length; j++) {

                if(j > i+1 && arr[j] == arr[j-1])continue; // avoid second element duplicate

                int l = j + 1;
                int r = arr.length - 1;
                 
                while (l < r) {
                    int sum = arr[i] + arr[j] + arr[k] + arr[l];
     
                    if (sum > target) {
                        r--;
                    } else if (sum < target) {
                        l++;
                    } else if (sum == target) {
                        ArrayList<Integer> temp = new ArrayList<Integer>();
                        temp.add(arr[i]);
                        temp.add(arr[j]);
                        temp.add(arr[k]);
                        temp.add(arr[l]);
     
                        /*if (!hashSet.contains(temp)) {
                        //    hashSet.add(temp);
                        result.add(temp);
                        //}
     
                        l++;
                        r--;
                    }
                }
            }
        }
     
        return result;
    }

### k sum 
K Sum problem in recursive way is just to reduce K sum problem to K – 1 sum Problem, and then to K – 2 Sum problem … Finally it would be reduced to the basic case 2sum problem.

    vector< vector<int> > KSum(vector<int> &arr, int K, int target, int p) {
            vector< vector<int> > vecResults;
            if (K == 2) { // base case
                vector<int> tuple(2, 0);
                int l = p, r = arr.size() - 1;
                while (l < r) {
                    if (l > p && arr[l] == arr[l - 1]) {
                        ++l;
                        continue;
                    }
                    int sum = arr[l] + arr[r];
                    if (sum == target) {
                        tuple[0] = arr[l++];
                        tuple[1] = arr[r--];
                        vecResults.push_back(tuple);
                    }
                    else if (sum > target) {
                        --r;
                    }
                    else {
                        ++l;
                    }
                }
                return vecResults;
            }
            // K > 2
            for (int i = p; i < arr.size(); ++l) {
                if (i > p && arr[i] == arr[i - 1]) continue;
                vector< vector<int> > K1Sum = KSum(arr, K - 1, target - arr[l], i + 1);
                for (auto it = K1Sum.begin(); it != K1Sum.end(); ++it) {
                    vector<int> tuple;
                    tuple.push_back(arr[l]);
                    tuple.insert(tuple.end(), it->begin(), it->end());
                    vecResults.push_back(tuple);
                }
            }
            return vecResults;
        }

### Find subarray with given sum

>Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

>Examples:

>Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Solution: Initialize a variable curr_sum as first element. curr_sum indicates the sum of current subarray. Start from the second element and add all elements one by one to the curr_sum. If curr_sum becomes equal to sum, then print the solution. If curr_sum exceeds the sum, then remove trailing elemnents while curr_sum is greater than sum. 思想类似于[定长线段最多覆盖点的个数](/posts/algorithm/point.html).

    int subArraySum(int arr[], int n, int sum) {
        /* Initialize curr_sum as value of first element
           and starting point as 0 */
        int curr_sum = arr[0], start = 0, i;
     
        /* Add elements one by one to curr_sum and if the curr_sum exceeds the
           sum, then remove starting element */
        for (i = 1; i <= n; i++) {
            // If curr_sum exceeds the sum, then remove the starting elements
            while (curr_sum > sum && start < i-1)
            {
                curr_sum = curr_sum - arr[start];
                start++;
            }
     
            // If curr_sum becomes equal to sum, then return true
            if (curr_sum == sum)
            {
                printf ("Sum found between indexes %d and %d", start, i-1);
                return 1;
            }
     
            // Add this element to curr_sum
            if (i < n)
              curr_sum = curr_sum + arr[i];
        }
     
        // If we reach here, then no subarray
        printf("No subarray found");
        return 0;
    }

refer:

- [http://www.programcreek.com/2012/12/leetcode-solution-of-two-sum-in-java/](http://www.programcreek.com/2012/12/leetcode-solution-of-two-sum-in-java/)
- [http://segmentfault.com/blog/code/1190000000450743](http://segmentfault.com/blog/code/1190000000450743)
- [http://www.programcreek.com/2012/12/leetcode-3sum/](http://www.programcreek.com/2012/12/leetcode-3sum/)
- [http://www.programcreek.com/2012/12/leetcode-3sum/](http://www.programcreek.com/2012/12/leetcode-3sum/)
- [http://www.cnblogs.com/tenosdoit/p/3649607.html](http://www.cnblogs.com/tenosdoit/p/3649607.html)
- [http://www.programcreek.com/2013/02/leetcode-3sum-closest-java/](http://www.programcreek.com/2013/02/leetcode-3sum-closest-java/)
- [http://www.programcreek.com/2013/02/leetcode-4sum-java/](http://www.programcreek.com/2013/02/leetcode-4sum-java/)
- [k sum problem](http://tech-wonderland.net/blog/summary-of-ksum-problems.html)

