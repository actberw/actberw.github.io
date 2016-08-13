Title: bash

http://www.juyimeng.com/freebsd-linux-change-default-shell.html
http://book.51cto.com/art/201205/337149.htm
http://linuxpoison.blogspot.jp/2010/07/how-to-lock-unlock-enable-disable-linux.html
http://unix.stackexchange.com/questions/17906/can-i-allow-a-non-root-user-to-log-in-when-etc-nologin-exists


http://www.dewen.io/q/15349/Linux%EF%BC%9A%28%29%E5%92%8C%7B%7D%E6%89%A7%E8%A1%8C%E6%8C%87%E4%BB%A4%E7%9A%84%E6%97%B6%E5%80%99%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%91%A2%EF%BC%9F

http://blog.csdn.net/honghuzhilangzixin/article/details/7073312
http://codingstandards.iteye.com/blog/1160298

http://www.netingcn.com/tag/shell%E4%B8%AD%E5%86%92%E5%8F%B7%E7%AD%89%E4%BA%8E%E7%94%A8%E9%80%94


特殊符号
http://blog.useasp.net/archive/2014/06/02/summary-of-the-special-characters-in-shell-on-linux.aspx

The double dash "--" means "end of command line flags" `ls -al -- -a.c`
Many commands use a hyphen (-) in place of a filename as an argument to indicate when the input should come from stdin rather than a file.
`command1 | command2 paramater1 | command3 parameter1 - parameter2 | command4`

管道 (“|”, pipe line)，把上一个命令的 stdout 接到下一个命令的 stdin;

If ‘|&’ is used, the standard error of command1 is connected to command2's standard input through the pipe; it is shorthand for "2>&1 |". This implicit redirection of the standard error is performed after any redirections specified by the command(bash 4).
http://stackoverflow.com/questions/7701206/how-does-gcc-invoke-as-ld-and-other-binutils
http://askubuntu.com/questions/24953/using-grep-with-pipe-and-ampersand-to-filter-errors-from-find
http://unix.stackexchange.com/questions/70963/difference-between-2-2-dev-null-dev-null-and-dev-null-21
2>&-
2>/dev/null
|&
&>/dev/null
>/dev/null 2>&1


col
tr
tee

http://man.linuxde.net/tee

here document
http://en.wikipedia.org/wiki/Here_document
http://linuxcommand.org/wss0030.php


cat << EOF > ~/.bashrc
if [ -f ~/project/code/shell/bashrc ]; then
    . ~/project/code/shell/bashrc
fi
EOF

tilde expansion

http://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html


What is the difference between test, [ and [[ ?

http://mywiki.wooledge.org/BashFAQ/031

### shell常用命令使用
1. netcat

     $ nc -l 1234 > sd #接受者
     $ nc 192.168.1.97 1234 < ./feeds.py.back #发送者

2. ngrep

    $ ngrep -q -W byline 'search' host www.google.com.hk and port 80


if 测试文件是否存在最好加引号, 但是如果是"~" 开头就不要加, 加了就不会展开. `man bash` 见 "Tilde Expansion" 章节.

    # 最好加引号
    local b=~/.bashrc    # 这里不要加
    if [ -f "$b" ];then  # 这里加
    ¦   echo "exist"
    else
    ¦   echo "no-exist"
    fi


变量赋值等号两边不能有空格.

快捷键

http://blog.jobbole.com/86948/

