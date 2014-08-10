Title: xtrbackup备份原理
Date: 2014-08-10 21:00:00
Tags: mysql, xtrabackup

xtrabackup备份主要做两件事情:

 - 后台启动一个日志复制线程监控innodb日志文件，发现变动时复制到xtrabackup_logfile
 - 复制innodb数据文件, 并不是简单的复制，跟innodb同样的方式打开文件，打开数据字典( data dictionary)复制innodb page.

当数据文件复制完成时，停止日志复制线程同时创建文件xtrabackup_checkpoints记录 LSN(log sequence number)信息.

复制数据文件时每次读取1M大小(这个没法配置), 并检查每个page是否损坏.日志文件时每次512KB.

innodb page(通常是16kb)包含一个日志序列号LSN, LSN是整个数据库的版本号, LSN的大小表示最近多久被修改过. 增量备份的原理就是复制LSN大于xtrabackup_checkpoints记录的最后LSN.有两种算法找到变动的page:

 - 读取所有的page比较LSN，mysql及Percona Server都支持 (数据库的大小影响备份的快慢)
 - Percona Server 用bitmap实现了跟踪变化的innodb page 特性, 会快很多.

xtrabackup调用innodb库来读数据文件，而innodb以read-write打开数据文件, 所以用xtrabackup备份的时候需要有对数据文件写的权限，但是并不会写文件.
refer:

- [http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/creating_a_backup.html](http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/creating_a_backup.html)
- [http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/implementation_details.html](http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/implementation_details.html)
