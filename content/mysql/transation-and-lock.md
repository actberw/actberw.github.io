Title: mysql innodb 事务和锁
Date: 2014-07-15 20:44:00

事务属性(ACID): 
A(automic): it's all or nothing(undo log).
I: 多并发事务, 对相同数据的修改在没commit前对其他事务的可见性.
C: ensures that any transaction will bring the database from one valid state to another.
D: once a commit operation succeeds, the changes made by that transaction are safe from power failures, system crashes(redo log)

### 隔离级别

隔离级别规定了一个事务中所做的修改，哪些在事务内和事务间是可见的，哪些是不可见的。

- 可序列化（Serializable）
实现可序列化要求在选定对象上的读锁和写锁保持直到事务结束后才能释放。在 SELECT 的查询中使用一个 WHERE 子句来描述一个范围时应该获得一个“范围锁(range-locks)”。这种机制可以避免“幻影读(phantom reads)”现象。

- 可重复读（Repeatable read）
对选定对象的读锁(read locks)和写锁(write locks)一直保持到事务结束，但不要求“范围锁(range-locks)”，因此可能会发生“幻影读(phantom reads)”。

- 提交读（Read committed）
DBMS需要对选定对象的写锁(write locks)一直保持到事务结束，但是读锁(read locks)在SELECT操作完成后马上释放（因此“不可重复读”现象可能会发生，见下面描述）。和前一种隔离级别一样，也不要求“范围锁(range-locks)”。 不可重复读是因为，事务只维持了选定对象的写锁，如果一些选定对象只涉及读锁，那么在读锁释放之后，其它事务可以对这些对象进行修改，该事务再次读取时就不一致了。

- 未提交读（Read uncommitted）

In lock-based concurrency control, isolation level determines the duration that locks are held.

### 并发一致性问题(why concurrency control needed?)
并发一致性问题包括:

- The dirty read problem, 读"脏"数据, A dirty read (aka uncommitted dependency) occurs when a transaction is allowed to read data from a row that has been modified by another running transaction and not yet committed.
- Non-repeatable reads, 不可重复读 
- Phantom reads
所谓幻影读是指：事务1按一定条件从数据库中读取某些数据记录后，事务2插入了一些符合事务1检索条件的新记录，当事务1再次按相同条件读取数据时，发现多了一些记录。

不可重复读和幻读的区别: 很多人容易搞混不可重复读和幻读，确实这两者有些相似。但不可重复读重点在于update和delete，而幻读的重点在于insert。

并发控制方法: 乐观并发控制, 悲观并发控制(锁) 

### 锁

A shared (S) lock permits a transaction to read a row.
An exclusive (X) lock permits a transaction to update or delete a row.

Intention Locks(Multiple granularity locking)

Intention locks are table locks in InnoDB that indicate which type of lock (shared or exclusive) a transaction will require later for a row in that table. There are two types of intention locks used in InnoDB (assume that transaction T has requested a lock of the indicated type on table t):

Intention shared (IS): Transaction T intends to set S locks on individual rows in table t.
Intention exclusive (IX): Transaction T intends to set X locks on those rows.

The intention locking protocol is as follows:

- Before a transaction can acquire an S lock on a row in table t, it must first acquire an IS or stronger lock on t.
- Before a transaction can acquire an X lock on a row, it must first acquire an IX lock on t.

InnoDB has several types of record-level locks including record locks, gap locks, and next-key locks. 

metadata locks 

尽管数据库理论对并发一致性问题提供了完善的解决机制，但让程序员自己去控制如何加锁以及加锁、解锁的时机显然是很困难的事情。索性绝大多数数据库以及开发工具都提供了事务隔离级别，让用户以一种更轻松的方式处理并发一致性问题。
两段锁协议与三级封锁协议
两类不同目的的协议
两段锁协议：保证并发调度的正确性
三级封锁协议：在不同程度上保证数据一致性
遵守第三级封锁协议必然遵守两段协议

### two-phase locking 

Two phase locking has two phases:

- growing; where all locks are being acquired by transaction
- shrinking, where locks held by the transaction are being release

保证加锁阶段与解锁阶段不相交。

### OCC(optimistic concurrency control) or optimistic lock

### MVCC
人们一般把基于锁的并发控制机制称成为悲观机制，而把MVCC机制称为乐观机制。这是因为锁机制是一种预防性的，读会阻塞写写也会阻塞读，当锁定粒度较大时间较长时并发性能就不会太好；而MVCC是一种后验性的，读不阻塞写，写也不阻塞读，等到提交的时候才检验是否有冲突. 读不加锁读写不冲突, 从而大大提升了并发性能。 MVCC的一种简单实现是基于CAS（Compare-and-swap）思想的有条件更新（Conditional Update）

多版本并发控制（MVCC）的实现是通过保存数据在某个时间点的快照来实现的。根据事务开始的时间不同，每个事务对同一张表，同一时刻看到的数据可能是不一样的。

Internally, InnoDB adds three fields to each row stored in the database. A 6-byte DB_TRX_ID field indicates the transaction identifier for the last transaction that inserted or updated the row. Also, a deletion is treated internally as an update where a special bit in the row is set to mark it as deleted. Each row also contains a 7-byte DB_ROLL_PTR field called the roll pointer. The roll pointer points to an undo log record written to the rollback segment. If the row was updated, the undo log record contains the information necessary to rebuild the content of the row before it was updated. A 6-byte DB_ROW_ID field contains a row ID that increases monotonically as new rows are inserted. If InnoDB generates a clustered index automatically, the index contains row ID values. Otherwise, the DB_ROW_ID column does not appear in any index.

每开始一个新的事务，系统版本号都会递增。事务开始时刻的系统版本号作为事务的版本号，用来和查询到的每行记录的版本号进行比较。

在 REPEATABLE READ 隔离级别下，MVCC 的具体操作：

select：InnoDB 根据以下两个条件检查每行记录：

a、 InnoDB 只查找版本早于当前事务版本的数据行（也即是行的版本号小于等于事务的系统版本号），这样可以确保事务读取的行，要么是在事务开始前已经存在的，要么是事务自身插入或者修改的。
b、行的删除版本要么未定义，要么大于当前事务版本号。这可以确保事务读取到的行，在事务开始之前未被删除。
只有符合以上两个条件的记录，才能返回作为查询结果。
insert：InnoDB 为新插入的每一行保存当前系统版本号作为行版本号。

delete：InnoDB 为删除的每一行保存当前系统版本号作为行删除标识。

update：InnoDB 为插入一行新纪录，保存当前系统版本号作为行版本号，同时保存当前系统版本号到原来的行作为行删除标识


在可重读Repeatable reads事务隔离级别下：

SELECT时，读取创建版本号<=当前事务版本号，删除版本号为空或>当前事务版本号。
INSERT时，保存当前事务版本号为行的创建版本号
DELETE时，保存当前事务版本号为行的删除版本号
UPDATE时，插入一条新纪录，保存当前事务版本号为行创建版本号，同时保存当前事务版本号到原来删除的行

DB_TRX_ID, DB_ROLL_PTR, DB_ROW_ID

In REPEATABLE READ every lock acquired during a transaction is held for the duration of the transaction(long duration, strict 2PL), creates gap locks for range scans.
In READ COMMITTED the locks that did not match the scan are released after the STATEMENT completes(short duration, not 2PL).

### dead lock(Wait-For-Graph)

用事物做顶点, 等待的锁为边构建图, 检测是否有环.

refer:

- [http://dev.mysql.com/doc/refman/5.7/en/innodb-lock-modes.html](http://dev.mysql.com/doc/refman/5.7/en/innodb-lock-modes.html)
- [http://en.wikipedia.org/wiki/Concurrency_control](http://en.wikipedia.org/wiki/Concurrency_control)
- [http://tech.meituan.com/innodb-lock.html](http://tech.meituan.com/innodb-lock.html)
- [http://hedengcheng.com/?p=286](http://hedengcheng.com/?p=286)
- [http://www.percona.com/blog/2012/08/28/differences-between-read-committed-and-repeatable-read-transaction-isolation-levels/](http://www.percona.com/blog/2012/08/28/differences-between-read-committed-and-repeatable-read-transaction-isolation-levels/)
- [https://www.cs.duke.edu/courses/fall09/cps116/lectures/17-transaction.pdf](https://www.cs.duke.edu/courses/fall09/cps116/lectures/17-transaction.pdf)
- [http://db.lcs.mit.edu/6.893/F04/ccandr.pdf](http://db.lcs.mit.edu/6.893/F04/ccandr.pdf)
- [http://www.cs.berkeley.edu/~franklin/CS186F00/lectures/l22-6up.pdf](http://www.cs.berkeley.edu/~franklin/CS186F00/lectures/l22-6up.pdf)
- [http://www.gpfeng.com/?p=426](http://www.gpfeng.com/?p=426)
- [http://hedengcheng.com/?p=148](http://hedengcheng.com/?p=148)
