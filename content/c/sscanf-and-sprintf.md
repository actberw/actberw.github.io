Input white-space characters (as specified by the isspace function) are skipped, unless the specification includes a [, c, or n specifier.

The '\n' character in the format string of scanf("%d\n", &paycode) matches any number of whitespace characters (space, tab, newline etc. - characters for which the isspace function declared in ctype.h yields true) in the input given. Therefore, the scanf call will read and discard any number of whitespace characters till it encounters a non-whitespace character at which point it will return. This is true for any whitespace character in the format string of scanf and not only the newline character. For example, the following will exhibit the same behaviour:

scanf("%d\n", &N);
scanf("%d", &N);

http://www.cnblogs.com/Anker/p/3351168.html
