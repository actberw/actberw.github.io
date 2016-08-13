Title: debian 配置
Tags: debian, linux
Date: 2014-09-23 15:00:00

### /etc/apt/sources.list 中源格式  

    # format  
    deb http://site.example.com/debian distribution component1
    # example  
    deb-src http://ftp.us.debian.org/debian/ wheezy main

 - 第一部分(deb or deb-src)表示文档类型, deb表示预编译得二进制包, deb-src表示源码包.  
 - 第二部分是镜像url.   
 - 第三部分表示debian发型版本号, 可以是release code名(squeeze, wheezy)或者是release class (oldstable, stable, testing, unstable)    
 - 第四部分包许可类型:   
     - main 本身是自由软件，且所有直接依赖的包也都是自由软件。  
     - contrib 本身是自由软件，但直接依赖的包中有某个是非自由软件。  
     - non-free 本身并非自由软件  

注: 修改/etc/apt/sources.list后要执行apt-get update 更新有效软件包列表.

### 开发者文档

aptitude search manpages
aptitude search libstdc++

manpages-dev, manpages-posix-dev, libstdc++6-4.7-doc

refer:

- [0][https://wiki.debian.org/SourcesList](https://wiki.debian.org/SourcesList)
- [1][http://forum.ubuntu.org.cn/viewtopic.php?t=366506](http://forum.ubuntu.org.cn/viewtopic.php?t=366506)
- [2][http://mirrors.163.com/.help/debian.html](http://mirrors.163.com/.help/debian.html)
