Title: 电话号码问题
Tags: algorithm, combination
Date: 2014-10-04 13:00:00

### Letter Combinations of a Phone Number
>Given a digit string, return all possible letter combinations that the number could represent.
![phone keyboard](/img/phone-keyboard.png)

>Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

思路: 先计算第一数字的所有排列, 然后由第一个字符的所有排列计算是前两个字符, 依此类推.

    // 非递归实现
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        string charmap[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        res.push_back("");  // 初始
        for (int i = 0; i < digits.size(); i++)
        {
          vector<string> tempres;
          string chars = charmap[digits[i] - '0'];
          for (int c = 0; c < chars.size();c++)
            for (int j = 0; j < res.size();j++)
              tempres.push_back(res[j]+chars[c]);
          res = tempres;
        }
        return res;
    }

    // 递归实现
    public class Solution {
        public String[] letters = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
            public List<String> letterCombinations(String digits) {
                int len = digits.length();
                List<String> res = new ArrayList<String>();
                if(len == 0){
                    res.add("");
                    return res;
                }
                List<String> next = letterCombinations(digits.substring(1));
                int p = Integer.parseInt(digits.substring(0,1));
                String tmp = letters[p];
                for(int i = 0; i < tmp.length(); i++){
                    for(int j = 0; j < next.size(); j++){
                        res.add(tmp.substring(i, i+1).concat(next.get(j)));
                    }
                }
                return res;
            }
    }

思路2: dfs, 像这种在一个ArrayList里面罗列可能的path的题目，recursion的参数一般包括：包含最终结果的集合（ArrayList），input（String），递归层次level（int, 也可以由path length求出），某一条具体的path（String）。最后这个参数虽然不是必须，但是如果使用了它，将会使recursion非常好写：所有关于这条路径的添加、删除、修改都可以以这个具体的path为操作对象，并且一旦条件满足，就可以把这个path添加到最终的结果集合里面去，用ArrayList add函数

       public class Solution {  
        public ArrayList<String> letterCombinations(String digits) {  
            ArrayList<String> list = new ArrayList<String>();  
              
            char[][] keyMap = {{}, {'a','b','c'}, {'d','e','f'}, {'g','h','i'}, {'j','k','l'},  
            {'m','n','o'}, {'p','q','r','s'}, {'t','u','v'}, {'w','x','y','z'}};    
              
            dfs(list, "", digits, keyMap);  
              
            return list;  
        }  
          
        public void dfs(ArrayList<String> list, String path, String digits, char[][] keyMap) {  
            if (path.length() == digits.length()) {  
                list.add(path);  
                return;  
            } else {  
                int num = digits.charAt(path.length()) - '1';  
                  
                for (int i = 0; i < keyMap[num].length; i++) {  
                    dfs(list, path + keyMap[num][i], digits, keyMap);  
                }  
            }  
              
        }  
          
    } 

refer:

- [http://www.cnblogs.com/EdwardLiu/p/3781123.html](http://www.cnblogs.com/EdwardLiu/p/3781123.html)
- [http://blog.csdn.net/u014425050/article/details/24855521](http://blog.csdn.net/u014425050/article/details/24855521)
- [http://blog.csdn.net/linhuanmars/article/details/19743197](http://blog.csdn.net/linhuanmars/article/details/19743197)
- [http://www.geeksforgeeks.org/find-possible-words-phone-digits/](http://www.geeksforgeeks.org/find-possible-words-phone-digits/)
