Title:进程用户ID
Tags: linux, setuid, getuid, setresuid
Date: 2014-10-24 22:00:00

每个进程有三种用户ID :

 - 实际用户ID(real user id, or ruid)或组
 - 有效用户ID(effective user id, or euid)或组
 - 保存用户ID(saved user id, or suid)或组

### 实际用户ID  
实际用户ID即执行程序得用户ID, 是进程所有者ID. 实际用户ID有两方面的影响:

 - 发送信号的权限, 非特权用户进程只有信号发送进程的实际用户ID或有效用户ID等于信号接收进程的实际用户ID或保存的用户ID时才能发送信号.
 - access函数做权限检测时会用到

### 有效用户ID  
通常跟实际用户ID相同, 但当设置了设置用户ID(set-user-ID bit)时(参见[文件权限](/posts/misc/file-permission.html))，有效用户ID为文件所有者的ID. 有效用户ID通常用来:

 - 权限检测
 - 进程创建的文件的所有者

### 保存用户ID  
保存用户ID常用来以很高权限(elevated privileges)运行的进程暂时要做一些低权限的操作(unprivileged), 以便进程以后可以再修改回原来的有效用户ID重新获得更高的权限(an unprivileged process can only set its effective user ID to three values: its real user ID, its saved user ID, and its effective user ID—i.e., unchanged). 进程启动时保存用户ID从有效用户ID复制, setuid, seretuid, setresuid会修改保存用户ID.

### 测试代码:  

    //1. 测试实际用户ID
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>

    int main(void) {
        uid_t r_uid, e_uid;
        r_uid = getuid();
        e_uid = geteuid();
        printf("Real User ID:\t%d\nEffect User ID:\t%d\n", r_uid, e_uid);
    }

    // 直接gcc 编译
    $ ls -al ./a.out
    -rwxr-xr-x 1 actberw actberw 7085 May 30 22:54 ./a.out
    $ id
    uid=1000(actberw) gid=1000(actberw) groups=1000(actberw)
    $ ./a.out
    Real User ID:   1000
    Effect User ID: 1000

    $ sudo ./a.out
    Real User ID:   0
    Effect User ID: 0


    // 2. 测试有效用户ID  
    $ chmod u+s ./a.out #设置设置用户ID
    $ ls -al ./a.out 
    -rwsr-xr-x 1 actberw actberw 7.0K May 30 22:54 ./a.out
    $ sudo ./a.out
    Real User ID:   0
    Effect User ID: 1000


    // 3. 测试进程创建得文件权限  
    #include <stdio.h>
    #include <unistd.h>
    #include <fcntl.h>
    #include <sys/types.h>
    #define USER_RW (S_IRUSR|S_IWUSR)

    int main(void) {
        uid_t r_uid, e_uid;
        int fd;
        r_uid = getuid();
        e_uid = geteuid();
        printf("Real User ID:\t%d\nEffect User ID:\t%d\n", r_uid, e_uid);
        fd = open("./stat.log", O_CREAT, USER_RW);
        write(fd, "actberw", 7);
        close(fd);
    }

    // 直接gcc编译  
    $ chmod u+s ./a.out
    $ sudo ./a.out 
    Real User ID:   0
    Effect User ID: 1000
    $ ls -al stat.log
    -rw------- 1 actberw root 0 May 30 23:20 stat.log  # 所有者是effective id

### fork 和 exec  
fork时子进程会从父进程继承三个用户ID,  当进程执行exec一个文件时如果设置了设置用户ID标志位, 则有效用户ID和保存用户ID都为文件所有者的ID.

### 相关API  
 - getuid/setuid
 - geteuid/seteuid
 - getresuid/setresuid
 - setreuid

api|作用|root权限(euid=0)| 非root权限(euid!=0)
---|----|--------|-----------
setuid|修改euid|id可以是任意值, 而且三个用户ID都等于新的ID|等于ruid或suid
seteuid|只改变进程euid，而不改变ruid和suid|新euid可以是任意值|新euid等于ruid或suid
setreuid|修改ruid和euid, 如果ruid设置了或者euid不等于以前的ruid则suid等于新的euid|ruid和euid可以是任意值|euid可以可以设置成三个中的任意一个, ruid可以设置成ruid或者euid
setresuid|改变ruid, euid和suid|任意值|每一个等于原来某个id中的一个

注: 如果要临时的降特权则用seteuid, 永久的降特权则可用setuid. 由于权限判断依据有效用户ID, 所以在降特权的时候先降组特权，然后再降用户特权, 否则的话进程可能没有权限降组特权. 

refer: 

- [0][http://www.cs.berkeley.edu/~daw/papers/setuid-usenix02.pdf](http://www.cs.berkeley.edu/~daw/papers/setuid-usenix02.pdf)
