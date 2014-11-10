Title: linux 僵尸(zombie)进程和孤儿(orphan)进程
Tags: linux, zombie, orphan, process
Date: 2014-09-12

### Zombie Processes
In Unix and Linux systems, the zombie (or defunct) process is a process that has completed execution but still has an entry in the process table, it is a process in the [Terminated state](http://en.wikipedia.org/wiki/Process_state). A zombie process remains in the operating system and does nothing until the parent process determines that the exit status is no longer needed.

Normally, when a process finishes execution, it reports the execution status to its parent process. Until the parent process decides that the child processes exit status is not needed anymore, the child process turns into a defunct or zombie process. Once the exit status is read via the `wait` system call, the zombie's entry is removed from the process table and it is said to be "reaped". It does not use resources and cannot be scheduled for execution.The `kill` command has no effect on a zombie process, Zombies can be identified in the output from the Unix ps command by the presence of a "Z" in the "STAT" column.

    int main(void) {
        int status;
        pid_t pid = fork();
        if (pid == 0) {// child process
            exit(0);
        } else {
            printf("zombie process: %d\n", pid);
            sleep(30);
            // wait(&status);
            // printf("zombie process: %d\n, status: %d\n", pid, WEXITSTATUS(status));
        }
        return 0;
    }

### Orphan Processes
An Orphan Process is a process that is still executing but whose parent is dead (terminated), then adopted by the init process.
参见[daemon进程](/posts/c/daemon.html)

refer:

- [http://lesca.me/archives/process-relationship.html](http://lesca.me/archives/process-relationship.html)
- [http://en.wikipedia.org/wiki/Zombie_process](http://en.wikipedia.org/wiki/Zombie_process)
- [http://linuxg.net/what-are-zombie-and-orphan-processes-and-how-to-kill-them/](http://linuxg.net/what-are-zombie-and-orphan-processes-and-how-to-kill-them/)

