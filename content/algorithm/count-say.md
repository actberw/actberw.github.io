Title: Count and Say problem

>The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

>1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

>Note: The sequence of integers will be represented as a string.

    string s1="" , s2"";
    s1 = "1";
    i=1;
    int tmp,cnt;
    if( N==0 ) print 0 and s1;
    while( i<=N )
    {   s2.clear();
        for( j=0; j<strlen(s1); )
             tmp = s1[j];
             cnt = 0;
             while( s1[j] == tmp && j<strlen(s1) )
                    cnt++;
                    j++;
             s2 += cnt+'0';
             s2 += tmp + '0';
         
        print i and s2;
        s1.clear();
        s1 = s2;
        i++;
    }


http://www.careercup.com/question?id=4425679
