Title: EOF是什么
Tags: linux, c, eof, stty
Date: 2014-09-20

### EOF
EOF 是end of file的缩写, 表示"文字流"（stream）的结尾. 这里的"文字流"，可以是文件(file), 也可以是标准输入(stdin). 写从终端读取数据的程序时经常会用EOF判断输入结束, 例如:

    int main(void) {
        int c;
        while ((c = getc()) != EOF) {
         　　putchar (c);
        }
        return 0;
    }

这里的EOF是一个定义在头文件stdio.h的常量，一般等于-1.

    # define EOF (-1)

`man getc` 中说 *getc() return the character read as an unsigned char cast to an int or  EOF  on  end  of file or error.*  就是说在文件结束, 或者发生错误的时候返回EOF.  所以这里的EOF用来标示(indicate)要么文件结束了, 要么发生了错误, 并不是一个特殊的符号. 同时为了确定是否真的是文件结束了c提供了一个 `feof()` 函数了来检测.

### ^D(ctrl + d)
运行上面的程序如果想结束输入 Linux 中在新的一行的开头按下 `^D` 就代表EOF(如果在一行的中间按下 `Ctrl-D`，则表示输出"标准输入"的缓存区，所以这时必须按两次`^D`), 这里的 `^D` 是特殊控制符, 表示标准输入结束.

    $ stty -a
    intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = M-^?; eol2 = M-^?; swtch = <undef>; start = ^Q; stop = ^S;
    susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; flush = ^O; min = 1; time = 0;
    -parenb -parodd cs8 -hupcl -cstopb cread -clocal -crtscts
    -ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc ixany imaxbel -iutf8
    opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
    isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke

如果在终端中真的想输入 `^D` 怎么办? 这时必须先按下 `Ctrl-V`, 然后就可以输入 `Ctrl-D`, 系统就不会认为这是EOF. `Ctrl-V` 表示按"字面含义"解读下一个输入, 要是想按"字面含义"输入Ctrl-V, 连续输入两次就行了.

另外要跟 `Ctrl-C` 区分开来, `Ctrl-C` 是给进程发送 TERM 信号是要结束进程.

refer:

- [http://www.ruanyifeng.com/blog/2011/11/eof.html](http://www.ruanyifeng.com/blog/2011/11/eof.html)
- [http://unix.stackexchange.com/questions/110240/why-does-ctrl-d-eof-exit-the-shell](http://unix.stackexchange.com/questions/110240/why-does-ctrl-d-eof-exit-the-shell)
