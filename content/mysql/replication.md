###mysql5.6配置主从复制

1. master配置
        
        # http://dev.mysql.com/doc/refman/5.6/en/replication-options-master.html
        server-id               = 1 # 唯一得
        binlog-format           = ROW # row, mixed, statement
        log-bin                 = /var/log/mysql/mysql-bin.log
        log-bin-index           = master-bin.index
        sync_binlog             = 0 # 0:依赖操作系统
                                    # 1~n: 在每sync_binlog 次bin log写操作后同步到磁盘
        binlog_cache_size       = 32k
        expire_logs_days        = 5
        max_binlog_size         = 128M
        #binlog-do-db           = db_name 
        #binlog-ignore-db       = exclude_database_name
         
2. slave配置

        # http://dev.mysql.com/doc/refman/5.6/en/replication-options-slave.html
        server-id               = 2
        
        # relay-log=file_name        # 默认值是: host_name-relay-bin
        # relay-log-index=file_name  # 默认值是: host_name-relay-bin.index
        # max_relay_log_size    = 1G # 默认值是: 1G
        # relay_log_space_limit = 2G # relay log 占用的磁盘最大空间
        # sync_relay_log        = 0     # 同sync_binlog, 0 每次写都同步到磁盘

        # log-slave-updates          # 配合log-bin控制是否slave是否写bin log

        # sync-master-info  
        # master-info-file = master.info # 默认值是: master.info, 5.6引入master-info-repository=TABLE, 可以把信息写到mysql.slave_master_    info表中
        # sync_relay_log_info 
        # relay-log-info-file=file_name  # 默认值是: relay-log.info, 5.6引入relay-log-info-repository=TABLE， 可以吧信息写到mysql.slave_rela    y_log_info 表中

        # replicate-do-db=db_name        # 跟binlog-do-db 对应
        # replicate-ignore-db=db_name  

        # report-host=host_name          # 在master中得注册ip或者host，在master上执行 SHOW SLAVE HOSTS, 可以看到

        # slave-parallel-workers = 3     # 5.6新增，控制并发得SQL thread, 0 关闭并发执行

3. 创建复制账户
       
        # master上创建账户
        CREATE USER 'repl'@'%' IDENTIFIED BY 'slavepass';
        # 授权
        GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
        

4. 设置master 信息,启动复制

        # slave 上MASTER_DELAY 控制延迟时间
        CHANGE MASTER TO
        -> MASTER_HOST='master_host_name',
        -> MASTER_USER='replication_user_name',
        -> MASTER_PASSWORD='replication_password',
        -> MASTER_LOG_FILE='recorded_log_file_name',
        -> MASTER_LOG_POS=recorded_log_position;
        start slave;

7. 复制得管理

        # 在master上
        SHOW SLAVE HOSTS;
        SHOW PROCESSLIST \G;
        show master status

        # 在salve上 
        SHOW SLAVE STATUS\G

        # 关闭复制
        stop slave
        STOP SLAVE IO_THREAD;
        STOP SLAVE SQL_THREAD;

        START SLAVE;

### Replication Implementation Details
三个线程, 一个在master, 两个在slave上:

- Binlog dump thread
- Slave I/O thread
- Slave SQL thread

### `show slave status` 几个重要字段

"Seconds_Behind_Master": When the slave is actively processing updates, this field shows the difference between the current timestamp on the slave and the original timestamp logged on the master for the most event currently being processed on the slave. In essence, this field measures the time difference in seconds between the slave SQL thread and the slave I/O thread. this column is useful only for fast networks. 


"Relay_Log_File": The name of the current relay log file
"Relay_Log_Pos": The current position within the relay log file; events up to this position have been executed on the slave database

"Relay_Master_Log_File": The name of the master binary log file from which the events in the relay log file were read
"Exec_Master_Log_Pos": The equivalent position within the master's binary log file of events that have already been executed

"Master_Log_File":The name of the master binary log currently being read from the master
"Read_Master_Log_Pos": The current position within the master binary log that have been read from the master

Relay_Master_Log_File & Exec_Master_Log_Pos 和 Relay_Log_File & Relay_Log_Pos是对应的，它们表示的是Slave中的SQL进程中正在执行的语句的位置.

Relay_Master_Log_File & Exec_Master_Log_Pos 和 Master_Log_File & Read_Master_Log_Pos可以看出主从同步的状态, 跟Seconds_Behind_Master 表明的意思差不多, 当他们一致时 Seconds_Behind_Master 为0.

refer:

- [http://huoding.com/2011/04/05/59](http://huoding.com/2011/04/05/59)
- [http://www.slideshare.net/ylouis83/mysqlmha](http://www.slideshare.net/ylouis83/mysqlmha)
