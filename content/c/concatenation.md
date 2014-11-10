Title: c字符串续行
Tag: c, line join, concatenation
Date: 2014-08-21
lang: cn

示例:  

    char *my_string = "Line 1 \
                       Line 2";

    char *my_string = "Line 1 "
                      "Line 2";

注: With a #define, you have to add an extra '\' to concatenate the two strings:

    #define kMyString "Line 1"\
                      "Line 2";

refer:

- [0][http://stackoverflow.com/questions/797318/how-to-split-a-string-literal-across-multiple-lines-in-c-objective-c](http://stackoverflow.com/questions/797318/how-to-split-a-string-literal-across-multiple-lines-in-c-objective-c)
