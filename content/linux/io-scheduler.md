
Block devices maintain request queues to store their pending block I/O requests.The request queue is represented by the request_queue structure and is defined in <linux/blkdev.h>.

Simply sending out requests to the block devices in the order that the kernel issues them, as soon as it issues them, results in poor performance. One of the slowest operations in a modern computer is disk seeks. Each seek—positioning the hard disk’s head at the loca- tion of a specific block—takes many milliseconds. Minimizing seeks is absolutely crucial to the system’s performance

Therefore, the kernel does not issue block I/O requests to the disk in the order they are received or as soon as they are received. Instead, it performs operations called merging and sorting to greatly improve the performance of the system as a whole.2 The subsystem of the kernel that performs these operations is called the I/O scheduler.

An I/O scheduler works by managing a block device’s request queue. It decides the order of requests in the queue and at what time each request is dispatched to the block device.It manages the request queue with the goal of reducing seeks, which results in greater global throughput.

I/O schedulers perform two primary actions to minimize seeks: merging and sorting. The entire request queue is kept sorted, sectorwise, so that all seeking activity along the queue moves (as much as possible) sequentially over the sectors of the hard disk.The goal is not just to minimize each indi- vidual seek but to minimize all seeking by keeping the disk head moving in a straight line.


- Linus
- Deadline(deadline), 适合随机比较多
- Anticipatory(as) 2.6.18前默认的调度器
- Complete Fair Queuing(cfq), 2.6.18后默认的调度器, 每个提交io请求的进程都有自己的sorted queue, 在一个时间片中cfq选一个进程处理queue中的io请求
- Noop(noop), 只做合并(ssd)

cat /sys/block/sda/queue/scheduler 
echo deadline > /sys/block/hda/queue/scheduler


refer:

- [http://www.slideshare.net/heseymx/linux-io-scheduler](http://www.slideshare.net/heseymx/linux-io-scheduler)
- [http://www.linuxjournal.com/article/6931](http://www.linuxjournal.com/article/6931)
