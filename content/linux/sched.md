Title: linux 调度

## process state

#define TASK_RUNNING            0
#define TASK_INTERRUPTIBLE      1
#define TASK_UNINTERRUPTIBLE    2
#define TASK_ZOMBIE             4
#define TASK_DEAD               64

## scheduler policy
Processes scheduled under one of the real-time policies (SCHED_FIFO, SCHED_RR) have a sched_priority value in the range 1 (low) to 99 (high)
For threads scheduled under one of the normal scheduling policies (SCHED_OTHER, SCHED_IDLE, SCHED_BATCH), sched_priority(static scheduling priority) is not used in scheduling decisions 

real time scheduler:

- Hard real-time systems – required to complete a critical task within a guaranteed amount of time
- Soft real-time computing – requires that critical processes receive priority over less fortunate ones(linux support soft real-time)

## 进程优先级

    #define tsk_cpumask(tsk) (&(tsk)->cpus_allowed)
    
    /*
     * Priority of a process goes from 0..MAX_PRIO-1, valid RT
     * priority is 0..MAX_RT_PRIO-1, and SCHED_NORMAL/SCHED_BATCH
     * tasks are in the range MAX_RT_PRIO..MAX_PRIO-1. Priority
     * values are inverted: lower p->prio value means higher priority.
     *
     * The MAX_USER_RT_PRIO value allows the actual maximum
     * RT priority to be separate from the value exported to
     * user-space.  This allows kernel threads to set their
     * priority to a value higher than any user task. Note:
     * MAX_RT_PRIO must not be smaller than MAX_USER_RT_PRIO.
     */
    
    #define MAX_USER_RT_PRIO    100
    #define MAX_RT_PRIO     MAX_USER_RT_PRIO
    
    #define MAX_PRIO        (MAX_RT_PRIO + 40)
    #define DEFAULT_PRIO        (MAX_RT_PRIO + 20)

    struct task_struct {
        ...
        int prio, static_prio, normal_prio;
        unsigned int rt_priority;
        ...
    };

- static_prio, 静态优先级”，由普通进程(非实时进程)使用，静态优先级是进程启动时分配的优先级。该字段的取值范围为[100,139]([MAX_RT_PRIO,MAX_PRIO-1])，值越小优先级越高。

- rt_priority: 实时优先级，由实时进程使用，普通进程没有用到该参数。取值范围为[0,99]。注意：rt_priority是值越大优先级越高。
- normal_prio: normal_prio是基于前两个参数static_prio或rt_priority计算出来的。可以这样理解：static_prio和rt_priority分别代表普通进程和实时进程的”静态优先级”，代表进程的固有属性。由于他们两的表达方式不同，一个是值越小优先级越高，另一个是值越大优先级越高。有必要用normal_prio统一下。统一成值越小优先级越高，因此，normal_prio也可以理解为:统一了单位的”静态优先级”。 

        static inline int normal_prio(struct task_struct *p)
        {
            int prio;
            if (task_has_rt_policy(p))
                prio = MAX_RT_PRIO-1 - p->rt_priority;
            else
                prio = __normal_prio(p);
            return prio;
        }

- prio: 它表示进程的有效优先级(effective priority)，顾名思义，在内核中判断进程优先级时用的便是该参数，调度器考虑的优先级也就是它。其取值范围为[0,139]，值越小，优先级越低。该优先级又叫”动态优先级”。


CFS 中用 prio_to_weight 把prio转换为weight, 权重决定进程虚拟时间的增加速度.

##  pick next (pick_next_task)

vruntime 表示进程的虚拟运行时间由 `update_attr` 更新, 公式: delta_exec * NICE_0_LOAD / curr->load.weight (delta_exec 表示进程实际运行时间), 可见weight越大vruntime增涨越慢, 获得更多的调用机会. pick_next_task会选取vruntime 最小的调度.

最后，说下对CFS “完全公平” 的理解：

- 不再区分进程类型，所有进程公平对待
- I/O消耗型进程，仍然会提供快速响应(对睡眠进程做时间补偿)
- 优先级高的进程，获得CPU时间更多(vruntime增长的更慢)

## CFS 参数

sched_min_granularity_ns (16000000): Minimum preemption granularity for processor-bound tasks. Tasks are guaranteed to run for this minimum time before they are preempted.
sched_latency_ns (80000000): Period over which CFQ tries to fairly schedule the tasks on the runqueue. All of the tasks on the runqueue are guaranteed to be scheduled once within this period.
sched_wakeup_granularity_ns (20000000): Ability of tasks being woken to preempt the current task. The smaller the value, the easier it is for the task to force the preemption.

refer:

 - [http://www.cnblogs.com/tolimit/p/4303052.html](http://www.cnblogs.com/tolimit/p/4303052.html)
 - [http://unicornx.gitcafe.io/2016/03/03/20160303-lk-task-prio/](http://unicornx.gitcafe.io/2016/03/03/20160303-lk-task-prio/)
 - [https://www.ibm.com/developerworks/cn/linux/l-cn-scheduler/](https://www.ibm.com/developerworks/cn/linux/l-cn-scheduler/)
 - [http://home.ustc.edu.cn/~hchunhui/linux_sched.html](http://home.ustc.edu.cn/~hchunhui/linux_sched.html)
 - [http://linuxperf.com/?cat=10](http://linuxperf.com/?cat=10)
