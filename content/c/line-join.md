Title: c字符串续行
Tag: c, line join
Date: 2014-08-21

http://stackoverflow.com/questions/797318/how-to-split-a-string-literal-across-multiple-lines-in-c-objective-c

char *my_string = "Line 1 \
                   Line 2";

char *my_string = "Line 1 "
                  "Line 2";

NOTE: With a #define, you have to add an extra '\' to concatenate the two strings:

#define kMyString "Line 1"\
                  "Line 2"
