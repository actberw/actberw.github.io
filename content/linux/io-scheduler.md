Title: linux io 调度

IO调度器:

- 提高IO吞吐量
- 降低IO响应时间

Block devices maintain request queues to store their pending block I/O requests.The request queue is represented by the request_queue structure and is defined in <linux/blkdev.h>.

Simply sending out requests to the block devices in the order that the kernel issues them, as soon as it issues them, results in poor performance. One of the slowest operations in a modern computer is disk seeks. Each seek—positioning the hard disk’s head at the loca- tion of a specific block—takes many milliseconds. Minimizing seeks is absolutely crucial to the system’s performance

Therefore, the kernel does not issue block I/O requests to the disk in the order they are received or as soon as they are received. Instead, it performs operations called merging and sorting to greatly improve the performance of the system as a whole.2 The subsystem of the kernel that performs these operations is called the I/O scheduler.

An I/O scheduler works by managing a block device’s request queue. It decides the order of requests in the queue and at what time each request is dispatched to the block device.It manages the request queue with the goal of reducing seeks, which results in greater global throughput.

I/O schedulers perform two primary actions to minimize seeks: merging and sorting. The entire request queue is kept sorted, sectorwise, so that all seeking activity along the queue moves (as much as possible) sequentially over the sectors of the hard disk.The goal is not just to minimize each individual seek but to minimize all seeking by keeping the disk head moving in a straight line.


- Linus
- Deadline(deadline), 适合随机比较多
- Anticipatory(as) 2.6.18前默认的调度器
- Complete Fair Queuing(cfq), 2.6.18后默认的调度器, 每个提交io请求的进程都有自己的sorted queue, 在一个时间片中cfq选一个进程处理queue中的io请求
- Noop(noop), 只做合并(ssd)

修改调度器:

    cat /sys/block/sda/queue/scheduler 
    echo deadline > /sys/block/hda/queue/scheduler

## Deadline

    struct deadline_data {
        // requests (deadline_rq s) are present on both sort_list and fifo_list
        struct rb_root sort_list[2];    
        struct list_head fifo_list[2];

        struct request *next_rq[2];
        unsigned int batching;
        sector_t last_sector;
        unsigned int starved;
        int fifo_expire[2];
        int fifo_batch;
        int writes_starved;
        int front_merges;
    };

sort_list: 存储request的红黑树，request按照其读写方向被分别存放在不同的红黑树上
fifo_list：存储request的FIFO队列，为了解决request饿死问题，每个request也按照读写方向被分别存放在两个FIFO链表中

`deadline_dispatch_requests`

## CFQ(ionice)

CFQ scheduler moved to a new time sliced design dubbed CFQv3. Among other things, it implements ioprio_get(2) and ioprio_set(2) which allows user to set per-process I/O priorities, usually using ionice(1) command (although using nice(1) also modifies I/O priorities somewhat)
a process can be in one of three scheduling classes:

- Idle
- Best-effort, This  is  the effective scheduling class for any process that has not asked for a specific I/O priority.  This class takes a priority argument from 0-7, with a lower number being higher prior‐ ity.  Programs running at the same best-effort priority are served in a round-robin fashion.
- Realtime, The RT scheduling class is given first access to the disk

For kernels after 2.6.26 with the CFQ I/O scheduler, a process that has not asked for an I/O priority inherits its CPU scheduling class.  The I/O priority is derived from the CPU nice level of the process:io_priority = (cpu_nice + 20) / 5.

## Noop

    struct noop_data {
            struct list_head queue;
    };

  该算法实现了最最简单的FIFO队列，所有IO请求大致按照先来后到的顺序进行操作。之所以说“大致”，原因是NOOP在FIFO的基础上还做了相邻IO请求的合并，并不是完完全全按照先进先出的规则满足IO请求。NOOP假定I/O请求由驱动程序或者设备做了优化或者重排了顺序(就像一个智能控制器完成的工作那样)。

refer:

- [http://www.slideshare.net/heseymx/linux-io-scheduler](http://www.slideshare.net/heseymx/linux-io-scheduler)
- [http://www.linuxjournal.com/article/6931](http://www.linuxjournal.com/article/6931)
- [http://blog.csdn.net/vanbreaker/article/details/8299491](http://blog.csdn.net/vanbreaker/article/details/8299491)
