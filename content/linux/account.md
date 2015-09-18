Title: linux 账户管理
Tags: linux, useradd, passwd
Date: 2015-04-27

debian "passwd" 包提供了如下命令管理用户和用户组:

- useradd, userdel, usermod, passwd, chage
- groupadd, groupdel, groupmod
- gpasswd 管理用户与组的关系.

The /etc/passwd file consists of user records, one to a line. Each record contains multiple fields, separated by colons (:). The fields are:

    username

    encrypted password (or x if shadow passwords are in use)

    UID

    default GID

    real name (also known as the GECOS field)

    home directory

    default shell
See also `man 5 passwd` 

The /etc/group file consists of group records, one to a line. Each record contains multiple fields, separated by colons (:). The fields are:

    group name

    encrypted group password (or x if shadow passwords are in use)

    GID

    group members' usernames, comma-separated

See also `man 5 group`

If shadow passwords are being used, the /etc/shadow file contains users' encrypted passwords and other information about the passwords. Its fields are colon-separated as for /etc/passwd, and are as follows:

    username

    encrypted password

    Days since Jan 1, 1970 that password was last changed

    Days before password may be changed

    Days after which password must be changed

    Days before password is to expire that user is warned

    Days after password expires that account is disabled

    Days since Jan 1, 1970 that account is disabled

    A reserved field

See also `man 5 shadow`. The password expiry related fields are modified by the chage program.

adduser/addgroup

### 锁定和禁用账户
锁定账户, 就是在密码前加一个"!": 

    passwd -l username or usermod 
锁定的账户仍然可以通过其他的认证手段登陆, 例如 ssh key.

禁用账户: 

    usermod -L -e 1 tom or usermod -L -e 1970-01-01 tom
    usermod -s /sbin/nologin tom or usermod -s /bin/false tom

Following program will not affected by this shell (/sbin/nologin):

    FTP clients
    mail clients
    sudo
    many setuid programs

### 查看用户和组信息

id/whoami, groups

refer:

- [账户管理](https://wiki.archlinux.org/index.php/Users_and_groups)
- [禁用账户](http://www.cyberciti.biz/faq/linux-disable-user-account-command/)
