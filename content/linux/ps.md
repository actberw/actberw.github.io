Title: Linux ps 命令
Tags: linux, ps
Date: 2015-03-31 23:00:00

ps 支持三种形式的参数:

- UNIX 以"-"开头
- BSD 不以"-"开头
- GNU 长选项, 以"--"开头


### 常用的进程选择选项

- -e 所有进程
- -a 除了session leader和没有关联终端的进程

- -p [pidlist] 按进程id选择, 多个进程id按逗号分割
- -C 按进程命令选择
- -u 按照用户选择

### 输出格式选项

- -f full-format 输出
- -F 比 "-f" 更详细
- -L 输出线程信息

- -o 控制输出的列, 所有的选项见 `man ps` 的 STANDARD FORMAT SPECIFIERS 部分, 常用的有uid, pid,cmd, lstart等, 跟 "-f"冲突.


### 排序

- –-sort 可排序的列跟 "-o" 相同, 选项前 "+" 表示增序排序, "-"表示倒叙排序. `ps -af --sort=uid,-ppid,+pid`

### 进程状态

- D    uninterruptible sleep (usually IO)
- R    running or runnable (on run queue)
- S    interruptible sleep (waiting for an event to complete)
- T    stopped, either by a job control signal or because it is being traced
- W    paging (not valid since the 2.6.xx kernel)
- X    dead (should never be seen)
- Z    defunct ("zombie") process, terminated but not reaped by its parent

refer:

- [http://www.thegeekstuff.com/2011/04/ps-command-examples/](http://www.thegeekstuff.com/2011/04/ps-command-examples/)
