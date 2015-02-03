Title: KMP算法
Tags: algorithm, c, str
Date: 2015-01-14

朴素算法

模式串和母串的比较是从左到右进行, 如果找不到和模式串相同的子串，则从左到右移动模式串，距离为1

    void search(char *pat, char *txt) {
        int M = strlen(pat);
        int N = strlen(txt);
     
        for (int i = 0; i <= N - M; i++) {
            int j;
     
            /* For current index i, check for pattern match */
            for (j = 0; j < M; j++) {
                if (txt[i+j] != pat[j])
                    break;
            }
            if (j == M) {
               printf("Pattern found at index %d \n", i);
            }
        }
    }

KMP算法中的KMP分别是指三个人名：Knuth、Morris、Pratt，其本质也是前缀匹配算法，对比前缀蛮力匹配算法，区别在于它会动态调整每次模式串的移动距离，而不仅仅是加一，从而加快匹配过程。


    void computeLPSArray(char *pat, int M, int *lps) {
        int len = 0;  // lenght of the previous longest prefix suffix
        int i;
     
        lps[0] = 0; // lps[0] is always 0
        i = 1;
     
        // the loop calculates lps[i] for i = 1 to M-1
        while (i < M) {
           if (pat[i] == pat[len]) {
             len++;
             lps[i] = len;
             i++;
           }
           else {
             if (len != 0) {
               // This is tricky. Consider the example AAACAAAA and i = 7.
               // Also, note that we do not increment i here
               len = lps[len-1];
             } else {
               lps[i] = 0;
               i++;
             }
           }
        }
    }

    void KMPSearch(char *pat, char *txt) {
        int M = strlen(pat);
        int N = strlen(txt);

        int *lps = (int *)malloc(sizeof(int)*M);
        int j  = 0;  // index for pat[]
     
        computeLPSArray(pat, M, lps);
     
        int i = 0;
        while (i < N) {

          if (pat[j] == txt[i]) {
            j++;
            i++;
          }
     
          if (j == M) {
            printf("Found pattern at index %d \n", i-j);
            j = lps[j-1];
          } else if (i < N && pat[j] != txt[i]) {
            if (j != 0)
             j = lps[j-1];
            else
             i = i+1;
          }
        }
        free(lps); 
    }

考虑模式串匹配不上母串的最坏情况，前缀蛮力匹配算法的时间复杂度最差是O(n×m)，最好是O(n),其中n为母串的长度，m为模式串的长度。KMP算法最差的时间复杂度是O(n)；最好的时间复杂度是O(n/m)。

refer:

- [http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)
- [http://www.searchtb.com/2011/07/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%82%A3%E4%BA%9B%E4%BA%8B%EF%BC%88%E4%B8%80%EF%BC%89.html](http://www.searchtb.com/2011/07/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%82%A3%E4%BA%9B%E4%BA%8B%EF%BC%88%E4%B8%80%EF%BC%89.html)
