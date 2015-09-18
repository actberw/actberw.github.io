Title: Linux nice 和renice 命令
Tags: linux, nice, renice
Date: 2015-04-01 09:00:00

系统每个进程都有优先级(亦称“nice 值”), nice值表示进程的谦让程度 其范围从 -20 (最高优先级)到 19 (最低优先级)。默认情况下，进程的优先级是 0 (“基本”调度优先级).


renice 命令可以修改一个正在运行的进程的优先级

    renice +15 785

nice 命令可以按照指定的优先级启动进程

    nice -n 19 dd if=/dev/cdrom of=~/mdk1.iso

查看进程的优先级可以通过 `ps -afl`, NI 列就是进程的优先级.

refer:

- [http://man.chinaunix.net/linux/mandrake/101/zh_cn/Command-Line.html/process-priority.html](http://man.chinaunix.net/linux/mandrake/101/zh_cn/Command-Line.html/process-priority.html)
