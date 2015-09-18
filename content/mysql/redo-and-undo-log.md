Title: mysql undo 和 redo 日志

The InnoDB transaction log handles REDO logging, this is the mechanism that provides the A (Atomic) C (Consistent)  and D (Durability) in ACID. 

Rules for writing log records:

- Write-ahead-log principle (WAL)(undo)
- Commit-rule ("Force-Log-at-Commit")(redo)

Influence on recovery:

- Force: Flush buffer before EOT (commit processing)
- NoForce: Buffer manager decides on writes, not TA-mgr
- NoSteal : Do not write dirty pages before EOT
- Steal: Write dirty pages at any time 

Instead of logging whole pages (Value / Physical logging) where both the before and after image of a page is logged or by logging logical changesÂ  (Logical logging) to the dataset, InnoDB uses  Physiological logging, this basically means that it combines the two techniques to provide a logging mechanism that is both optimal in terms of the amount of data logged whilst still ensuring the log is action consistent and each operation is idempotent. 

Temporary log file can be small:

- Undo log entries not needed after commit
- Redo log entries not needed after write to stable storage


double write

bin log vs redo log

前者用于point-in-time恢复，后者用于crash recovery；如果mysql发生介质损坏，则需要从备份中恢复然后应用binary log执行point-in-time recovery

refer:

- [http://ask.chinaunix.net/question/772](http://ask.chinaunix.net/question/772)
- [http://www.inf.fu-berlin.de/lehre/SS05/19517-V/FolienEtc/dbs05-20-LogRecovery-2-2.pdf](http://www.inf.fu-berlin.de/lehre/SS05/19517-V/FolienEtc/dbs05-20-LogRecovery-2-2.pdf)
- [http://www.percona.com/blog/2011/02/03/how-innodb-handles-redo-logging/](http://www.percona.com/blog/2011/02/03/how-innodb-handles-redo-logging/)
- [http://tech.uc.cn/?p=716](http://tech.uc.cn/?p=716)
- [http://www.cnblogs.com/Bozh/archive/2013/03/18/2966494.html](http://www.cnblogs.com/Bozh/archive/2013/03/18/2966494.html)
- [http://www.percona.com/blog/2006/08/04/innodb-double-write/](http://www.percona.com/blog/2006/08/04/innodb-double-write/)
- [http://www.orczhou.com/index.php/2010/02/innodb-double-write/](http://www.orczhou.com/index.php/2010/02/innodb-double-write/)
- [http://hedengcheng.com/?p=489](http://hedengcheng.com/?p=489)
