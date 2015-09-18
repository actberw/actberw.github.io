### python logging 模块

pyhton 内置logging模块一大好处就是所有的库都可以使用，这样应用就可以搜集自己程序的日志和第三方库的日志了。  

#### 模块提供的基本对象:  

1. Logger 提供了应用程序可以直接调用的写日志接口
2. Handler 发送Logger产生的日志纪录到制定的地方。
3. Filter 提供了细粒度的工具决定输出哪些日志。

#### 模块级别的方法:  

1. logging.getLogger(name) 根据name返回一个Logger对象, 如果name没有指定，返回rootlogger, 如果指定的话name经常是英文句号分隔的层级形势，例如 “a”, “a.b” or “a.b.c.d”。  
2. logging.setLoggerClass(klass) 设定自定义的Logger Class 替代默认的Logger。自定一的Logger Class 必须继承自Logger，__init__方法只需要有一个name参数必须调用Logger.__init__(), 此方法必须在实例化Logger前调用。  
3. logging.getLoggerClass() 返回Logger Class 
4. logging.debug(msg[, *args[, **kwargs]]) root logger纪录DEBUG信息
5. logging.info(msg[, *args[, **kwargs]]) INFO level 
6. logging.warning(msg[, *args[, **kwargs]]) WARNING level
7. logging.error(msg[, *args[, **kwargs]]) ERROR level
8. logging.critical(msg[, *args[, **kwargs]]) CRITIAL level
9. logging.log(level, msg[, *args[, **kwargs]])
10. logging.disable(lvl) 关闭lvl以下的日志，例如: lvl=INFO, 则INFO， DEBUG， NOTSET， 都不会纪录。
11. logging.addLevelName(lvl, levelName)  给int类型的level提供一个字符串表示，对应LogRecord 的levelname属性。
12. logging.basicConfig([**kwargs])  创建StreamHandler(默认是stderr) ， 默认的Formatter 给root logger , 如果root logger没有配置handler则 info(), warning(), error() and critical() 会自动调用 basicConfig().
#### logger level  
1. NOTSET
2. DEBUG
3. INFO
4. WARNING
5. ERROR
6. CRITICAL

log record, logger, handler


### logging file config
[handler_file]
class = logging.handlers.RotatingFileHandler
args = ("spider.log", )
level = INFO
formatter = default
backupCount = 3


refer:

- [http://thinlight.org/2011/08/10/python-logging-from-multiple-processes/](http://thinlight.org/2011/08/10/python-logging-from-multiple-processes/)
