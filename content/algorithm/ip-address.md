Title: ip地址相关题目
Tags: algorithm, ip
Date: 2014-10-04 12:00:00

### Restore IP Addresses
>Given a string containing only digits, restore it by returning all possible valid IP address combinations.

>For example:
Given "25525511135",

>return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


Given a number string, find all of the possible IP address that it may represent in decimal form.

Finding all possible answer means we usually have to do a search, either DFS or BFS. This problem can be properly solved with DFS.


    public class Solution {  
        public ArrayList<String> restoreIpAddresses(String s) {  
            ArrayList<String> res = new ArrayList<String>();  
            if (s.length()<4||s.length()>12) return res;  
            dfs(s,"",res,0);  
            return res;  
        }  
          
        public void dfs(String s, String tmp, ArrayList<String> res, int count){  
            if (count == 3 && isValid(s)) {   // 缺少s超限(NULL)的判断
                res.add(tmp + s);  
                return;  
            }  
            for(int i=1; i<4 && i<s.length(); i++){  
                String substr = s.substring(0,i);  
                if (isValid(substr)){  
                    dfs(s.substring(i), tmp + substr + '.', res, count+1);  
                }  
            }  
        }  
          
        public boolean isValid(String s){  
            if (s.charAt(0)=='0') return s.equals("0");  
            int num = Integer.parseInt(s);  
            return num<=255 && num>0;  
        }  
    } 


### IP地址字符串转无符号整型uint

利用状态机的思想: 
输入有两种情况: 数字或者点, 设初始状态S0 为 reading_dot, 则如果在都到dot state 转error， 数字转reading_num, 状态为reading_num 时都到dot转reading_dot， 都到数字状态不变.

    int pton(char *str, unsigned int *result) {
            char ch, *iter;
            int state, digital, dot_num;
            state = 0 ; // 0 means read dot, 1 means read num.
            digital = dot_num = 0;
            for (iter = str; ; iter++) {
                    ch = *iter;
                    if (state == 0) {
                            if (ch >= '0' && ch <= '9') {
                                    digital = ch - '0';
                                    state = 1;
                            } else {
                                    return -1;
                            }
                    } else {
                            if (ch >= '0' && ch <= '9') {
                                    digital = digital * 10 + (ch - '0');
                                    if (digital > 255) return -1;
                            } else if (ch == '.'){
                                    dot_num++;
                                    if (dot_num > 3) return -1;
                                    state = 0;
                                    *result = (*result << 8) + digital;
                            } else if (ch == '\0'){
                                    *result = (*result << 8) + digital;
                                    return 0;
                            } else {
                                    return -1;
                            }
                    }
            }
    }

refer:

- [http://blog.csdn.net/u011095253/article/details/9158449](http://blog.csdn.net/u011095253/article/details/9158449)
- [http://www.ahathinking.com/archives/209.html](http://www.ahathinking.com/archives/209.html)
