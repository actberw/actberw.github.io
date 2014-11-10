Title: python续行
Tags: python, line join
Date: 2014-08-21
Lang: cn

pep8建议一行不要超过79个字符, python支持把逻辑行拆分成多个物理行(在编译时处理), 遵循一下规则.

### 显式连接
当一个物理行以反斜杠(backslash '\')结尾时(反斜杠不是字符串和注释的一部分), 会跟后面的行合并成一个逻辑行(删除掉反斜杠和后面的换行符), 但反斜杠后面不能加注释, 也不能用来续接关键词.

        if 1900 < year < 2100 and 1 <= month <= 12 \
           and 1 <= day <= 31 and 0 <= hour < 24 \
           and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
                return 1


### 隐式连接
在(), [], {} 的表达式可以拆分成多个物理行不需要显式的用反斜杠, 且隐式连接后面可以加注释.

    month_names = ['Januari', 'Februari', 'Maart',      # These are the
                   'April',   'Mei',      'Juni',       # Dutch names
                   'Juli',    'Augustus', 'September',  # for the months
                   'Oktober', 'November', 'December']   # of the year


### 字符串字面量的连接
python 支持将一个字符串字面量拆分成多行.

    # 反斜杠后不能加注释
    print 'This is a really long line,' \
                             'but we can make it across multiple lines.' 
    print 'niss\
              sfsfs'

    # 可以加注释
    print ('Wow, this also works?' # comment is allowed here
           'I never knew!')

refer:

- [0][https://docs.python.org/2.7/reference/lexical_analysis.html#explicit-line-joining](https://docs.python.org/2.7/reference/lexical_analysis.html#explicit-line-joining)
