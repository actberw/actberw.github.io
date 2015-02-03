交互式进程, 批处理进程, 实时进程


调度算法:

每个进程控制块中都有 5 个参数，分别是policy、priority、counter、 rt_priority和nice, nice是负向优先级,其值标志“谦让”的程度

SCHED—RR和SCHED—FIFO用于实时进程。分别表示轮转调度策略和先进先出调度策略

O(1)调度器在两个方面修改了Linux2.4调度器，一是进程优先级的计算方法；二是pick next算法(bitmap)。

队列的结构用 struct
prio_array 表示如下：

    struct prio_array {
        unsigned int nr_active;
        unsigned long bitmap[BITMAP_SIZE];
        struct list_head queue[MAX_PRIO];
    };
其中 nr_active 表示该队列中存在的进程总数。MAX_PRIO 定义为 140，即优先级分为 140 级，分别为 0 至 139，queue[MAX_PRIO]是表示共有 140 个队列，每个队列的优先级为 queue 的下标，即进程按优先级的大小放在不同的队列中，相同优先级的进程在同一队列中。 bitmap[BITMAP_SIZE]表示队列的位图，它对应 140 级队列，若某一队列中有进程，则该队 列对应位为 1，否则为 0。通过 bitmap 可快速确定在 140 级队列中，最高优先级的进程所在 的队列。当 active 队列中的进程将时间片用完后，就被放到 expired 队列中，并设置好新 的初始时间片。当 active 队列中无就绪进程时，即所有进程用完时间片，或进程的状态发 生了改变离开了该队列，这时，active 和 expired 两队列进行对换，重新开始下一轮的调 度过程。

为了支持实时进程，CFS提供了调度器模块管理器。各种不同的调度器算法都可以作为一个模块注册到该管理器中。不同的进程可以选择使用不同的调度器模块。2.6.23中，CFS实现了两个调度算法，CFS算法模块和实时调度模块。对应实时进程，将使用实时调度模块。对应普通进程则使用CFS算法。Ingo Molnar还邀请Con Kolivas可以将RSDL/SD写成一个调度算法模块。

refer:

- [http://www.ibm.com/developerworks/cn/linux/l-cn-scheduler/](http://www.ibm.com/developerworks/cn/linux/l-cn-scheduler/)
- [http://www.slideshare.net/punj25/final-18087303?related=1](http://www.slideshare.net/punj25/final-18087303?related=1)
- [http://blog.csdn.net/fangjian1204/article/details/39736725](http://blog.csdn.net/fangjian1204/article/details/39736725)
