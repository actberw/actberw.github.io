Title: Linux上的Shebang符号(#!)
Tags: linux, shebang
Date: 2014-10-24 21:00:00 

shebang取自#(SHArp)和!(bang), 它是很多脚本文件中第一行的前两个字符, 用来告诉Unix系统要用shebang后面指定的解释器来解释该脚本, 同时把文件名和参数一起作为参数传递给制定的解释器。所以，在很多脚本中，第一行往往都是这么写的

     #!/bin/bash

shebang符号后的解释程序一定要是绝对路径.
