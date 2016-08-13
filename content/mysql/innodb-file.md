Title: innodb 数据文件

By default, when InnoDB is initialized, it creates 3 important files in the data directory – ibdata1, ib_logfile0 and ib_logfile1.
.frm and .ibd files

## role of .frm file
MySQL stores its data dictionary information for tables in .frm files in database directories. Unlike other MySQL storage engines, InnoDB also encodes information about the table in its own internal data dictionary inside the tablespace. When MySQL drops a table or a database, it deletes one or more .frm files as well as the corresponding entries inside the InnoDB data dictionary

## data directory
Metadata that keeps track of InnoDB-related objects such as tables, indexes, and table columns. This metadata is physically located in the InnoDB system tablespace. For historical reasons, it overlaps to some degree with information stored in the .frm files.

The architecture of InnoDB demands the use of four basic types of info pages

- Table Data Pages
- Table Index Pages
- Table MetaData
- MVCC Data (to support Transaction Isolation and ACID Compliance)
    - Rollback Segments
    - Undo Space
- Double Write Buffer (background writing to prevent reliance on OS caching)
- Insert Buffer (managing changes to non-unique secondary indexes)

See the Pictorial Representation of ibdata1
By default, innodb_file_per_table is disabled. This causes all four info page types to land a single file called ibdata1. Many people try to spread out the data by making multiple ibdata files. This could lead to fragmentation of data and index pages.

This is why I often recommend cleaning up the InnoDB infrastructure, using the default ibdata1 file and nothing more.

Copying is very dangerous because of the infrastructure under which InnoDB works. There are two basic infrastructures

innodb_file_per_table disabled
innodb_file_per_table enabled
InnoDB (innodb_file_per_table disabled)
With innodb_file_per_table disabled, all these types of InnoDB info live within ibdata1. The only manifestation of any InnoDB table outside of ibdata1 is the .frm file of the InnoDB table. Copying all InnoDB data at once requires copying all of /var/lib/mysql.

Copying an individual InnoDB table is totally impossible. You must mysqldump to extract a dump of the table as a logical representation of the data and its corresponding index definitions. You would then load that dump to another database on the same server or another server.

InnoDB (innodb_file_per_table enabled)
With innodb_file_per_table enabled, table data and its indexes live in the database folder next to the .frm file. For example, for the table db1.mytable, the manifestation of that InnoDB table outside of ibdata1 would be:

/var/lib/mysql/db1/mytable.frm
/var/lib/mysql/db1/mytable.ibd
System Tablespace ibdata1
All the metadata for db1.mytable still resides in ibdata1 and there is absolutely no way around that. Redo logs and MVCC data also still live with ibdata1.

When it comes to table fragmentation, here is what happens to ibdata1:

innodb_file_per_table enabled: you can shrink db1.mytables with ALTER TABLE db1.mytable ENGINE=InnoDB; or OPTIMIZE TABLE db1.mytable;. This results in /var/lib/mysql/db1/mytable.ibd being physically smaller with no fragmentation.
innodb_file_per_table disabled: you cannot shrink db1.mytables with ALTER TABLE db1.mytable ENGINE=InnoDB; or OPTIMIZE TABLE db1.mytable; because it resides with ibdata1. Running either command actually make the table contiguous and faster to read and write to. Unfortunately, that occurs at the end of ibdata1. This makes ibdata1 grow rapidly. This is fully addressed in my InnoDB Cleanup Post.
WARNING (or DANGER as the Robot would say in Lost in Space)
If you are thinking of just copying the .frm and .ibd file, you are in line for world of hurting. Copying the .frm and .ibd file of an InnoDB table is only good if and only if you can guarantee that the tablespace id of the .ibd file matches exactly with the tablespace id entry in the metdata of the ibdata1 file.

I wrote two posts in DBA StackExchange about this tablespace id concept

Table compression in InnoDB? (under the heading 'Restoring Databases')
How to Recover an InnoDB table whose files were moved around
Here is excellent link on how to reattach any .ibd file to ibdata1 in the event of mismatched tablespace ids : http://www.chriscalender.com/?tag=innodb-error-tablespace-id-in-file. After reading this, you should come to the immediate realization that copying .ibd files is just plain crazy.

For InnoDB you only need to something this to move

CREATE TABLE db2.mytable LIKE db1.mytable;
INSERT INTO db2.mytable SELECT * FROM db1.mytable;
to make a copy of an InnoDB table.

If you are migrating it to another DB server, use mysqldump.

With regard to mixing all InnoDB tables from all databases, I can actually see the wisdom in doing so. At my employer's DB/Web hosting company, I have one MySQL Client that has a table in one database whose constraints are mapped to another table in another database within the same mysql instance. With one common metadata repository, it makes transactional support and MVCC operability possible across multiple databases.


refer:

- [https://blogs.oracle.com/mysqlinnodb/entry/data_organization_in_innodb](https://blogs.oracle.com/mysqlinnodb/entry/data_organization_in_innodb)
- [http://mysqlserverteam.com/a-new-data-dictionary-for-mysql/](http://mysqlserverteam.com/a-new-data-dictionary-for-mysql/)
- [http://zh.scribd.com/doc/31337494/XtraDB-InnoDB-internals-in-drawing](http://zh.scribd.com/doc/31337494/XtraDB-InnoDB-internals-in-drawing)
- [http://dba.stackexchange.com/questions/15531/why-does-innodb-store-all-databases-in-one-file](http://dba.stackexchange.com/questions/15531/why-does-innodb-store-all-databases-in-one-file)
