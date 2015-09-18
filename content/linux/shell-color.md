Title: bash 终端颜色 
Tags: linux, shell, bash color

In Bash, the <Esc> character can be obtained with "\e", "\033" or "^[".

format: "\e[attribute code;text color code;background color codem".

Attribute codes:
0=none 1=bold 4=underscore 5=blink 7=reverse 8=concealed

Text color codes:
30=black 31=red 32=green 33=yellow 34=blue 35=magenta 36=cyan 37=white

Background color codes:
40=black 41=red 42=green 43=yellow 44=blue 45=magenta 46=cyan 47=white

Terminals allow attribute combinations. The attributes must be separated by a semicolon (”;”).

refer:

- [http://www.csc.uvic.ca/~sae/seng265/fall04/tips/s265s047-tips/bash-using-colors.html](http://www.csc.uvic.ca/~sae/seng265/fall04/tips/s265s047-tips/bash-using-colors.html)
- [http://misc.flogisoft.com/bash/tip_colors_and_formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting)
- [http://www.wuzesheng.com/?p=2177](http://www.wuzesheng.com/?p=2177)
