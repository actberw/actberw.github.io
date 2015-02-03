Master Boot Record

主引导记录（Master Boot Record，缩写：MBR），又叫做主引导扇区，是计算机开机后访问硬盘时所必须要读取的首个扇区，它在硬盘上的三维地址为（柱面，磁头，扇区）＝（0，0，1）

在MBR分区表中最多4个主分区或者3个主分区＋1个扩展分区，也就是说扩展分区只能有一个，然后可以再细分为多个逻辑分区。

refer:

- [http://blog.csdn.net/bluishglc/article/details/9189437](http://blog.csdn.net/bluishglc/article/details/9189437)
- [http://blog.chinaunix.net/uid-23069658-id-3413957.html](http://blog.chinaunix.net/uid-23069658-id-3413957.html)
