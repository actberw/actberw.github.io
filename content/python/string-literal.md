Title: python 字符串字面量表示方式
Tags: python, str, unicode
Date: 2014-06-07

### String Literals
string字面量支持前缀: r/R(raw string), u/U(unicode string), b/B(byte literal in python3, ignore in python 2), u和b后面可以跟r, 支持下面的转义字符.

Escape   |  Meaning
---------|---------
\newline |Ignored (continuation line)
\\       |Backslash (stores one \)
\'       |Single quote (stores ')
\"       |Double quote (stores ")
\a       |Bell
\b       |Backspace
\f       |Formfeed
\n       |Newline (linefeed)
\r       |Carriage return
\t       |Horizontal tab
\v       |Vertical tab
\xhh     |Character with hex value hh (at most 2 digits)
\ooo     |Character with octal value ooo (up to 3 digits)
\0       |Null: binary 0 character (doesn’t end string)
\N{ id } |Unicode database ID
\uhhhh   |Unicode 16-bit hex
\Uhhhhhhhh| Unicode 32-bit hexa
\other   |Not an escape (keeps both \ and other)

### Unicode Literals
unicode字面量用前缀u/U表示, 特殊的字符可以用 `'\u' + 四个十六进制`  或者  `'\U' + 八个十六进制` 转义序列表示, 也可以用string literals的8为转义序列'\x', 但是 '\x' 后面只能跟两个十六进制符号(只能表示ascii字符部分).

    >>> s = u"a\xac\u1234\u20ac\U00008000"
    ... #      ^^^^ two-digit hex escape
    ... #          ^^^^^^ four-digit Unicode escape
    ... #                      ^^^^^^^^^^ eight-digit Unicode escape
    >>> for c in s:  print ord(c),
    ...
    97 172 4660 8364 32768

refer:

- [0][https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-7/string-literals](https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-7/string-literals)
- [1][https://docs.python.org/2/reference/lexical_analysis.html#string-literals](https://docs.python.org/2/reference/lexical_analysis.html#string-literals)
- [2][https://docs.python.org/2/howto/unicode.html#unicode-literals-in-python-source-code](https://docs.python.org/2/howto/unicode.html#unicode-literals-in-python-source-code)
- [3][http://legacy.python.org/dev/peps/pep-0223/](http://legacy.python.org/dev/peps/pep-0223/)
