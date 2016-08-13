Title: daemon进程c实现
Tags: linux, daemon, c
Date: 2014-09-11

### 守护进程(daemon process)特点

 - PPID 为 1
 - 控制终端(TTY, Teletypes) 为"?"
 - 守护进程必须与其运行前的环境隔离开来，包括未关闭的文件描述符，控制终端，会话，工作目录，以及umask等。这些都是从父进程继承过来的。

### 创建守护进程的步骤

 - fork创建子进程, 父进程退出
 - 调用setsid() 创建新会话
 - 再次fork，父进程退出(This guarantees that the daemon is not a session leader, which prevents it from acquiring a controlling terminal under the System V rules.)
 - 将当前工作目录改为根目录
 - 设定uamsk值为0
 - 关闭不必要的文件描述符
 - 打开/dev/null，dup2(0, 1, 2)


### 代码示例

    # include <unistd.h>

    int daemonize(void) {
        int  fd;

        switch (fork()) {
        case -1:
            //log_error(NGX_LOG_EMERG, log, ngx_errno, "fork() failed");
            return NGX_ERROR;

        case 0:
            break;

        default:
            exit(0);
        }

        ngx_pid = ngx_getpid();

        if (setsid() == -1) {
            ngx_log_error(NGX_LOG_EMERG, log, ngx_errno, "setsid() failed");
            return NGX_ERROR;
        }

        chdir('/')
        umask(0);

    
        fd = open("/dev/null", O_RDWR);
        if (fd == -1) {
            ngx_log_error(NGX_LOG_EMERG, log, ngx_errno,
                          "open(\"/dev/null\") failed");
            return NGX_ERROR;
        }

        if (dup2(fd, STDIN_FILENO) == -1) {
            ngx_log_error(NGX_LOG_EMERG, log, ngx_errno, "dup2(STDIN) failed");
            return NGX_ERROR;
        }

        if (dup2(fd, STDOUT_FILENO) == -1) {
            ngx_log_error(NGX_LOG_EMERG, log, ngx_errno, "dup2(STDOUT) failed");
            return NGX_ERROR;
        }
    }
