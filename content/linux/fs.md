
日志文件系统可以在系统发生断电或者其它系统故障时保证整体数据的完整性

Ext3文件系统是直接从Ext2文件系统发展而来，目前Ext3文件系统已经非常稳定可靠，它完全兼容Ext2文件系统，用户可以平滑地过渡到一个日志功能健全的文件系统。Ext3日志文件系统的思想就是对文件系统进行的任何高级修改都分两步进行。首先，把待写块的一个副本存放在日志中；其次，当发往日志的I/O 数据传送完成时（即数据提交到日志），块就写入文件系统。当发往文件系统的I/O 数据传送终止时（即数据提交给文件系统），日志中的块副本就被丢弃。

Ext3既可以只对元数据做日志，也可以同时对文件数据块做日志。具体来说，Ext3提供以下三种日志模式：

- 日志（Journal ） 文件系统所有数据和元数据的改变都记入日志。这种模式减少了丢失每个文件所作修改的机会，但是它需要很多额外的磁盘访问。例如，当一个新文件被创建时，它的所有数据块都必须复制一份作为日志记录。这是最安全和最慢的Ext3日志模式。
- 预定（Ordered ） 只有对文件系统元数据的改变才记入日志。然而，Ext3文件系统把元数据和相关的数据块进行分组，以便把元数据写入磁盘之前写入数据块。这样，就可以减少文件内数据损坏的机会；例如，确保增大文件的任何写访问都完全受日志的保护。这是缺省的Ext3 日志模式。
- 写回（Writeback ） 只有对文件系统元数据的改变才记入日志；这是在其他日志文件系统发现的方法，也是最快的模式。

Ext3 文件系统本身不处理日志，而是利用日志块设备（Journaling Block Device）或叫JBD 的通用内核层。Ext3文件系统调用JDB例程以确保在系统万一出现故障时它的后续操作不会损坏磁盘数据结构。Ext3 与JDB 之间的交互本质上基于三个基本单元：日志记录，原子操作和事务。


ext2/3/4, btfs, jfs, xfs, reiserfs

Atomic COW snapshots
Per-block checksumming
Volume management
File-level/Directory-level compression
为 SSD 优化
动态 inode 分配

refer:

- [http://www.ibm.com/developerworks/cn/linux/l-jfs/](http://www.ibm.com/developerworks/cn/linux/l-jfs/)
- [http://arstechnica.com/information-technology/2014/01/bitrot-and-atomic-cows-inside-next-gen-filesystems/3/](http://arstechnica.com/information-technology/2014/01/bitrot-and-atomic-cows-inside-next-gen-filesystems/3/)
