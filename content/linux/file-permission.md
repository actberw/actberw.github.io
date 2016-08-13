Title: linux 文件权限
Tags:linux, chmod, ls, setuid, chmod, sticky
Date: 2014-10-04 19:00:00

`ls -al /`  显示结果第一栏表示文件的属性共有十个, 第一个代表这个文件类型是, 后面三个一组分别代表: 文件所有者权限(u), 文件所有者组权限(g), 其他用户权限(o).

        drwxrwxrwt  4 root root  4096 Oct  4 19:00 tmp

### 文件类型  

- d 表示目录  
- \- 表示文件  
- l 表示连结档(link file)；   
- b 表示块设备(randomly accessible), 磁盘, CD等  
- c 表示字符设备(only a serial stream of input or output)，例如键盘、鼠标。   
- s 表示socket
- p 表示命名管道

### 文件权限  

权限| 对文件                      | 对目录
----|-----------------------------|--------------------------------------
r(4)| read                        | 可以`ll`
w(2)| write                       | 可以在目录下添加或删除文件
x(1)| execute                     | 可以search或者`cd`
X (chmod 修改权限)|`+X`则忽略(以前是x则不变, 不是也不增加x权限)|
    |`-X`如果有x权限则取消x,没有则忽略. 参见refer[0] | `+X`或`-X`效果跟`x`一样, 
s(4) 设置用户或者用户组ID位(set user ID bit)| |
t(1) 粘滞位(Sticky bit or restricted deletion flag)| linux中该选项对文件无效|对目录其下的文件只能被所有者或者root做unlink, rename或rm例如/tmp, 参见refer[1][2].
S或T| 同s或t, 如果有x权限则表示为小写(s, t), 否则用大写表示(S, T)| 同文件
    
也可以用1～4个八进制数字表示权限, 其中第一个数字表示设置用户ID(4), 设置用户组ID(2)和粘滞位(1), 后三个数字分别表示:文件所有者, 文件所有者组和其他用户权限, 参见refer[2].

### 设置用户ID或组ID位  
设置用户ID和组ID位是linux 访问控制标志, 通常用来暂时允许用户以更高的权限执行一些操作, 例如passwd. 设置了设置用户ID位的可执行文件, 由具有可执行权限的普通用户运行时产生的进程会会获得可执行文件所有者的权限(即进程的有效用户ID为可执行文件的所有者), linux下设置用户ID对目录无效. 

目录设置了设置用户组ID位时("chmod g+s"), 该目录下新生成的文件和目录将会继承其用户组ID而不是创建者的用户组ID(the owner ID is never affected, only the group ID), 而且新生成的子目录会继承设置用户组ID位.

See more `man 7 path_resolution`.

refer:

- [0][http://www.g-loaded.eu/2005/11/08/the-use-of-the-uppercase-x-in-chmod/](http://www.g-loaded.eu/2005/11/08/the-use-of-the-uppercase-x-in-chmod/)
- [1][http://en.wikipedia.org/wiki/Sticky_bit#cite_note-4](http://en.wikipedia.org/wiki/Sticky_bit#cite_note-4)
- [2][http://www.linuxmanpages.com/man1/chmod.1.php](http://www.linuxmanpages.com/man1/chmod.1.php)
- [http://en.wikipedia.org/wiki/Unix_file_types](http://en.wikipedia.org/wiki/Unix_file_types)
- [https://wiki.archlinux.org/index.php/File_permissions_and_attributes](https://wiki.archlinux.org/index.php/File_permissions_and_attributes)
