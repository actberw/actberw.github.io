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


refer:

- [http://blog.csdn.net/u011095253/article/details/9158449](http://blog.csdn.net/u011095253/article/details/9158449)
