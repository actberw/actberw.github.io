### debian 上安装mysql-5.6.15
1. 下载deb包

        wget http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.15-debian6.0-x86_64.deb
2. 安装

        sudo dpkg -i ./mysql-5.6.15-debian6.0-x86_64.deb # 需要安装依赖: libaio-dev
        # add account
        sudo groupadd mysql;sudo useradd -r -g mysql mysql
3. 安装默认数据库

        sudo mysql_install_db  --datadir=datadir --user=mysql
4. 配置mysql, 默认msyql安装到*/opt/mysql/server-5.6*目录 

        ln -s /opt/mysql/server-5.6 /usr/local/mysql
        # 修改 PATH
        export PATH=$PATH:/usr/local/mysql/bin
        # init.d脚本
        cd /opt/mysql/server-5.6;sudo cp support-files/mysql.server /etc/init.d/mysql

5. 修改配置文件

        # 修改配置文件
        # 分三个section, client, mysqld_safe, mysqld
        [client]
        port            = 3306
        socket          = /var/run/mysqld/mysqld.sock

        [mysqld_safe]
        socket          = /var/run/mysqld/mysqld.sock
        nice            = 0
        skip-syslog

        [mysqld]
        #
        # * Basic Settings
        #
        user            = mysql # 运行mysqld进程用户
        pid-file        = /var/run/mysqld/mysqld.pid
        socket          = /var/run/mysqld/mysqld.sock
        port            = 3306
        basedir         = /usr/local/mysql #mysql 安装目录
        datadir         = /var/mysql
        tmpdir          = /tmp
        bind-address    = 192.168.1.112 # 如果设置skip-networking,只会监听localhost
        lc-messages-dir = /usr/share/mysql
        skip-external-locking
        explicit_defaults_for_timestamp # 5.6新增选项，控制timestamp字段得值

        # * Query Cache Configuration
        #
        # query_cache_limit      = 1M
        # query_cache_size       = 24M # 查询缓存大小，默认query cache是关闭得,增加query_cache_type=1可以开启

        # 日志,bin log在主从设置里讲
        #general_log             = 1
        #general_log_file        = /var/log/mysql/mysql.log
        
        # 错误日志
        #lc-messages-dir=/usr/local/mysql/share
        #log-error = /var/log/mysql/error.log

        # 慢查询日志
        slow_query_log  = 1
        long_query_time = 1
        slow_query_log_file = /var/log/mysql/mysql-slow.log

        # myisam 得优化
        key_buffer_size = 256M # myisam 索引和数据得缓存大小

        # innodb 表空间
        # innodb_data_home_dir = ./
        # innodb_data_file_path = ibdata1:10M:autoextend

        # innodb 优化, http://dev.mysql.com/doc/refman/5.6/en/innodb-parameters.html
        innodb_file_per_table = 1 # 默认是共享表空间，这个选项控制是否使用独立表空间
        #innodb_file_format    = Antelope
        innodb_buffer_pool_size = 2G # innodb 索引和数据缓存大小

        # redo 日志选项
        # innodb_log_group_home_dir # redo 日志目录
        innodb_log_file_size = 256M 
        innodb_log_files_in_group = 3 #控制redo 日志得个数
        innodb_log_buffer_size = 16M
        innodb_flush_log_at_trx_commit = 2 # 0: 每秒钟把log buffer写到日志文件，刷新到磁盘
                                           # 1: 每次事务提交时log buffer写到日志文件, 刷新到磁盘
                                           # 2: 每次事务提交log buffer写到日志文件，5.6以前每一秒刷新到磁盘一次，5.6引入了innodb_flush_log_at_timeout，控制刷新时间间隔,默认是一秒

6. 修改root密码，删除匿名账户和测试数据库

        # 启动mysql
        sudo /etc/init.d/mysql start
        mysql_secure_installation # 可能需要 ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock

7. 增加账户,授权

        # add user
        create user 'acc'@'%' identified by "123"
        FLUSH PRIVILEGES;
        # create database        
        create database test_1 DEFAULT CHARACTER SET utf8;
        # grant, revoke 
        grant SELECT,INSERT,UPDATE,DELETE,LOCK TABLES on test_1.* to 'acc'@'%';

8. 遇到得错误提示:  

- Using unique option prefix key_buffer instead of key_buffer_size is deprecated and will be removed in a future release. Please use the full name instead  
  把key_buffer 换成 key_buffer_size

- IMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
  修改/etc/my.cnf mysqld 增加 explicit_defaults_for_timestamp=1 

- Can't find messagefile '/usr/share/mysql/errmsg.sys
  增加 lc-messages-dir=/usr/local/mysql/share 选项



