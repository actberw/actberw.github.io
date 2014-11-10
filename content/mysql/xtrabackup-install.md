Title: xtrabackup安装及使用
Date: 2014-08-10 20:00:00
Tags: mysql, xtrabackup

### 安装

    wget http://www.percona.com/redir/downloads/XtraBackup/LATEST/deb/precise/x86_64/percona-xtrabackup_2.1.6-702-1.precise_amd64.deb
    # 可能需要安装依赖:libdbd-mysql-perl 
    dpkg -i ./percona-xtrabackup_2.1.6-702-1.precise_amd64.deb
    # 安装完成后会产生四个命令行工具:innobackupex, xtrabackup, xbcrypt, xbstream

### 使用innobackupex增量备份  

innobackupex 是个perl脚本,封装xtrabackup,会根据mysql服务器得版本选择xtrabackup得版本, innobackupex可以备份myisam和innodb表, 同时也会备份表定义文件(.frm).

    # first setp full backup
    BASE_DIR=/data/mysql_backup/`date +"%Y-%m-%d"`
    innobackupex --defaults-file=/etc/mysql/my.cnf  --user root --no-timestamp --parallel=2 $BASE_DIR/base  # base dir shouldn't exists.

    # second setp incremental backup
    innobackupex --defaults-file=/etc/mysql/my.cnf  --incremental --user root --no-timestamp --parallel=2 --incremental-basedir=$BASE_DIR/base $BASE_DIR/inc-`date +"%H"`

    # third setp another incremental backup
    innobackupex --defaults-file=/etc/mysql/my.cnf  --incremental --user root --no-timestamp --parallel=2 --incremental-basedir=inc-1 $BASE_DIR/inc-`date +"%H"`

    # fourth setp prepare backup, -redo-only should be used when merging all incrementals except the last one
    innobackupex --apply-log --redo-only BASE-DIR
    innobackupex --apply-log  --incremental-dir=INCREMENTAL-DIR-1 --redo-only BASE-DIR
    innobackupex --apply-log BASE-DIR --incremental-dir=INCREMENTAL-DIR-2

    # fifth step
    innobackupex --apply-log BASE-DIR  # create  iblog* files
    
    # six step
    innobackupex --copy-back BASE-DIR # copy data to mysql datadir

refer:

 - [http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/incremental_backups.html](http://www.percona.com/doc/percona-xtrabackup/2.2/xtrabackup_bin/incremental_backups.html)
 - [http://www.percona.com/doc/percona-xtrabackup/2.2/innobackupex/incremental_backups_innobackupex.html](http://www.percona.com/doc/percona-xtrabackup/2.2/innobackupex/incremental_backups_innobackupex.html)
