Title: 内存分页
Date:2017-07-23

perf 是linux 2.6+ 之后提供的一个profiling性能诊断工具, 可以找到系统的热点.

### 命令

执行 `perf`可以查看到所有支持的命令, `perf help <command>` 或者 `perf <command> -h` 可以看到命令的详细文档.常用的命令有: list, stat, top, record, report. 

### 事件

三类事件: 

- software events.
- hardware events 和 hardware cache events. 依赖于PMU(Performance Monitor Uint), `cat /proc/cpuinfo |grep arch_perfmon` 检测是否支持.
- tracepoint events

`perf list` 可以列出所有支持的事件, 执行perf权限的问题参考 "sys.perf_event_paranoid" 选项. 执行
`sudo perf list | awk -F: '/Tracepoint/ {stat[$1]++} END {for ( x in stat) { printf("%-16s %d\n", x, stat[x]);}}' | column` 可以查看tracepoint的事件.

指定事件可以通过"-e"选项指定, 多个事件逗号分割。事件名后可以加事件修饰符格式为冒号加事件修饰符名， 支持的事件修饰符：

|Modifiers|Description|Example|
|---------|-----------|-------|
|u        |monitor at priv level 3, 2, 1 (user)|event:u|
|k        |monitor at priv level 0 (kernel)    |event:k|
|h        |monitor hypervisor events on a virtualization environment|event:h|
|H        |monitor host machine on a virtualization environment     |event:H|
|G        |monitor guest machine on a virtualization environment    |event:G|

The perf tool can be used to count events on a per-thread, per-process, per-cpu or system-wide basis.By default, perf stat counts for all threads of the process and subsequent child processes and threads. 

### 模式

counting mode
sampling mode

### perf stat 

"-I" 可以控制输出时间间隔.

### perf record

The perf_events interface allows two modes to express the sampling period:

- the number of occurrences of the event (period), "-c"
- the average rate of samples/sec (frequency), 这个是默认的, "-F"


### perf top

### refer:

- https://perf.wiki.kernel.org/index.php/Tutorial
- http://www.brendangregg.com/perf.html
- https://www.ibm.com/developerworks/cn/linux/l-cn-perf1/index.html
- http://kernel.taobao.org/index.php?title=Documents/Perf_FAQ
- http://www.brendangregg.com/blog/2014-07-03/perf-counting.html
