Title: online ddl

## Fast Index Creation

With MySQL 5.5 and higher, or MySQL 5.1 with the InnoDB Plugin, creating and dropping secondary indexes for InnoDB tables is much faster than before. Historically, adding or dropping an index on a table with existing data could be very slow. The CREATE INDEX and DROP INDEX statements worked by creating a new, empty table defined with the requested set of indexes, then copying the existing rows to the new table one-by-one, updating the indexes as the rows are inserted. After all rows from the original table were copied, the old table was dropped and the copy was renamed with the name of the original table.

The performance speedup for fast index creation applies to secondary indexes, not to the primary key index. The rows of an InnoDB table are stored in a clustered index organized based on the primary key, forming what some database systems call an “index-organized table”. Because the table structure is so closely tied to the primary key, redefining the primary key still requires copying the data.

While an InnoDB secondary index is being created or dropped, the table is locked in shared mode. Any writes to the table are blocked, but the data in the table can be read. When you alter the clustered index of a table, the table is locked in exclusive mode, because the data must be copied. Thus, during the creation of a new clustered index, all operations on the table are blocked. If the server crashes while creating an InnoDB secondary index, upon recovery, MySQL drops any partially created indexes. You must re-run the ALTER TABLE or CREATE INDEX statement.

## online ddl

The online DDL feature builds on the InnoDB Fast Index Creation feature. MySQL 5.6 enhances many other types of ALTER TABLE operations to avoid copying the table. Another enhancement allows SELECT queries and INSERT, UPDATE, and DELETE (DML) statements to proceed while the table is being altered. This combination of features is now known as online DDL.

refer:

- [https://dev.mysql.com/doc/refman/5.6/en/innodb-create-index-overview.html](https://dev.mysql.com/doc/refman/5.6/en/innodb-create-index-overview.html)
- [http://www.slideshare.net/frogd/my-sql-56innodb](http://www.slideshare.net/frogd/my-sql-56innodb)
