Title: ipython 简介
Tags: python, ipython
Date: 2015-04-11

### 四个最有用的命令

command    | description
-----------|-------------
?          | Introduction and overview of IPython’s feat        ures.
%quickrefQuick | reference.
help    | Python’s own help system.
object? | Details about ‘object’, use ‘object??’ for extra details. 

### tab 补全

可以补全对象的属性, 关键字, 和文件目录名.

### 查看对象帮助

`object_name?` 会打印出所有跟对象相关的信息: 包括doc string, 函数定义, 类构造器. 也可以用magic函数 %pdoc, %pdef, %psource and %pfile 获得相应的信息.

### Magic 函数

ipython 提供了很多预定义的magic 函数, 可以想shell命令一样的调用. 有两种magic函数: line-oriented 和 cell-oriented.  Line magic 函数前缀是一个百分号 "%", 执行 `%automagic` 命令可以在执行line magic 函数时避免输入百分号; cell magic 函数是两个百分号开头, 把后面的行也作为参数来处理, cell magic 函数必须以两个百分号开头.

    In [1]: %timeit range(1000)
    100000 loops, best of 3: 7.76 us per loop

    In [2]: %%timeit x = range(10000)
       ...: max(x)
       ...:
    1000 loops, best of 3: 223 us per loop

内置的magic 函数包括:

- Functions that work with code: %run, %edit, %save, %macro, %recall, etc.
- Functions which affect the shell: %colors, %xmode, %autoindent, %automagic, etc.
- Other functions such as %reset, %timeit, %%writefile, %load, or %paste.

执行 `%magic` 查看更详细的文档.

### 运行和编辑

`%run` magic 函数可以执行任何python脚本.
`%edit` magic 函数会调用一个编辑器, 可以输入代码执行.
`%save` magic 函数使用跟 `%history` 一样的参数格式, 保存代码到文件.

### 调试

在发生异常后, 可以执行 `%debug` 跳到pdb检查代码.


### 历史纪录

ipython会存储输入的命令和产生的结果, 可以简单的上下方向键查看历史纪录, 也可以用'CTRL+R'搜索历史记录.

输入和输出历史记录保存在 `In` 和 `Out` 两个变量中可以通过prompt的数字访问, 例如 `In[4]`. 最后三个输出历史纪录保存在 '_', '__'和'__'变量中.

可以用 ` %history` magic 函数访问历史纪录, 前一个session的历史纪录保存在数据库里面了.

    %history 18-20 ~1/1-5 

表示打印出当前18~20行的历史纪录, 和前一个session的1~5行.

### 系统shell命令

可以在ipython中加前缀 "!" 执行shell命令, 也可以执行 `%rehashx` 避免 "!" 前缀.

    !ping baidu.com

也可以捕获shell命令的输出 `files = !ls` ,也可以把python变量和表达式传递个shell命令当参数加上前缀 "$" 就行.
refer:

https://ipython.org/ipython-doc/dev/interactive/tutorial.html
