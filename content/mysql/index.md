Title: innodb 索引
Tags: mysql
Date: 2014-07-20 20:44:00

## Cardinality and selectivity

Cardinality: distinct column value count.
selectivity: ount(distinct col)/count(*)

## index type

b tree index and hash index

## Partial Index

postgresql 支持部分索引，只对满足条件的部分record建立索引， innodb 并不支持.

    CREATE INDEX test_index ON test_table (username) WHERE birth_month = 1 AND birth_day = 1;

## prefix Index

前缀索引，只对列的前缀部分建立索引， 会降低索引的区分度(selectivity), 但是会降低索引大小.

## Concatenated Index(联合索引)

对多列一起建立索引. 但是只能做前缀匹配.

## Covering Index

如果要查询到的列可以从索引中得到数据，就不会再去查找记录.

## sort

MySQL has two ways to produce ordered results: filesort or scan an index in order. MySQL can use same index for both sorting and finding rows. If possiable, it's a goog idea to design your indexs so that they're usefull for both tasks at once. Ordering the results by the index works only where indexed columns's order is exactly the same as order by clause and all columns are sorted in the same direction(asc or desc). The order by clause also has the same limitations as lookup queries: it needs to form a leftmost prefix of the index, Otherwise use filesort. One case the order by clause doesn't have to specify a leftmost prefix of the index is if there are constants(equal query in where condition, =) for the leading columns.

## index statistics(random dive 8 pages)

An InnoDB index statistics is used for JOIN optimizations and helping the MySQL optimizer choose the appropriate index for a query. If a index’s statistics or index cardinality becomes outdated, you might see queries which previously performed well suddenly show up on slow query log until InnoDB again updates the statistics. But when does InnoDB perform the updates aside from the first opening of the table or manually running ANALYZE TABLE on it? The 2 instances below are documented from the MySQL and InnoDB plugin’s manual:

- Metadata commands like SHOW INDEX, SHOW TABLE STATUS and SHOW [FULL] TABLES (or their corresponding queries from INFORMATION_SCHEMA.TABLES and INFORMATION_SCHEMA.STATISTICS)
- When 1 / 16th of the table or 2Billion rows has been modified, whichever comes first. ./row/row0mysql.c:row_update_statistics_if_needed

5.6 之前statistics重启后会自动消失，5.6后会持久化到mysql.innodb_table_stats 和 mysql.innodb_index_stats 表, 也可以通过`innodb_stats_persistent_sample_pages`选项控制采样的页数.

optimizer索引选择依据:

- estimate number of rows needs to access
- cardinality statistics

## index condition push down

参见[where 提取](/posts/mysql/where.html)

refer:

- [http://tech.meituan.com/mysql-index.html](http://tech.meituan.com/mysql-index.html)
- [http://www.mysqlperformanceblog.com/2011/10/06/when-does-innodb-update-table-statistics-and-when-it-can-bite/](https://www.percona.com/blog/2011/10/06/when-does-innodb-update-table-statistics-and-when-it-can-bite/)
- [http://www.slideshare.net/myxplain/mysql-indexing-best-practices-for-mysql](http://www.slideshare.net/myxplain/mysql-indexing-best-practices-for-mysql)
