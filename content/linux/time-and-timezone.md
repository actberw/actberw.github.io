Title: linux 时间和时区
Tags: linux, timezone, hwclock, time, date
Date: 2014-10-06

### RTC(real time clock)时间
Today such an RTC is usually integrated into the mainboard's chipset(south bridge) 
RTCs should not be confused with the system clock, which is a software clock maintained by the kernel and used to implement gettimeofday(2) and time(2)

hwclock 命令可以获取和修改RTC时间

### 系统时间(jiffies & xtime)

Linux会在开机时读取硬件时间初始化系统时间, 而后通过 *计时器中断* 来维护它, Linux上的系统时间其实是从1970年开始至今的秒数，而且，它还是一个实数（虚拟精度无穷大）。在关机时，Linux会将系统时间写回硬件时间。

System time is measured by a system clock, which is typically implemented as a simple count of the number of ticks that have transpired since some arbitrary starting date, called the epoch. 

在早期 Linux 内核中，定时器所能支持的最高精度是一个 tick。为了提高时钟精度，人们只能提高内核的 HZ 值 (一个内核参数，代表内核时钟中断的频率)。更高的 HZ 值，意味着时钟中断更加频繁，内核要花更多的时间进行时钟处理。而内核的任何工作对于应用来说纯粹是无益的开销。Linux 2.5以上将HZ从100改成1000，相当于系统时钟从10ms变成每1ms要中断一次，当时也引起较大的争议。

目前支持的clock source 有:

- PIT(Programmalbe Interval Timer)(IRQ0中断)
- TSC(Time Stamp Counter, 依赖于外部脉冲(clock Generator))
- HPET

可以 `cat /sys/devices/system/clocksource/clocksource0/available_clocksourc` 查看有效的clock source.

使用系统时间的原因是硬件时间毕竟要通过BIOS读取，无法提供足够的精度和速度, 另一个是硬件时间并不准确。主板的时间芯片会产生较为明显的“漂移”(drift).

date命令可以获取和修改系统时间, 或者[ntp](/posts/linux/ntp.html)

### time 命令和cpu 时间(clock 函数)

time命令的三种时间:

- 实际运行时间(real time, Wall clock time), 从命令行执行到运行终止的消逝时间；
- 用户CPU时间(user CPU time), 命令在用户态中执行时间的总和；
- 系统CPU时间(system CPU time), 命令在系统核心态中执行时间的总和。

### 时区timezone

    //查看当前时区：
    $ cat /etc/timezone

    //修改时区
    $ dpkg-reconfigure tzdata

refer:

- [http://blog.robotshell.org/2012/linux-time/](http://blog.robotshell.org/2012/linux-time/)
- [http://en.wikipedia.org/wiki/CPU_time](http://en.wikipedia.org/wiki/CPU_time)
- [http://serverfault.com/questions/48455/what-are-the-differences-between-wall-clock-time-user-time-and-cpu-time](http://serverfault.com/questions/48455/what-are-the-differences-between-wall-clock-time-user-time-and-cpu-time)
- [linux 系统中的时间](http://www.uml.org.cn/embeded/201308211.asp)
- [http://www.cnblogs.com/chezxiaoqiang/archive/2012/03/23/2674386.html](http://www.cnblogs.com/chezxiaoqiang/archive/2012/03/23/2674386.html)
- [http://timyang.net/linux/linux-timer-tick/](http://timyang.net/linux/linux-timer-tick/)
- [http://www.cnblogs.com/hjslovewcl/archive/2011/06/28/2314322.html](http://www.cnblogs.com/hjslovewcl/archive/2011/06/28/2314322.html)
- [http://www.ibm.com/developerworks/cn/linux/1308_liuming_linuxtime4/](http://www.ibm.com/developerworks/cn/linux/1308_liuming_linuxtime4/)
- [http://blog.csdn.net/DroidPhone/article/category/1263459](http://blog.csdn.net/DroidPhone/article/category/1263459)
- [http://blog.csdn.net/zs634134578/article/details/8982788](http://blog.csdn.net/zs634134578/article/details/8982788)
- [RTC/PIT/TSC](http://guojing.me/linux-kernel-architecture/posts/time-system/)
- [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_MRG/2/html/Realtime_Reference_Guide/chap-Realtime_Reference_Guide-Timestamping.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_MRG/2/html/Realtime_Reference_Guide/chap-Realtime_Reference_Guide-Timestamping.html)
