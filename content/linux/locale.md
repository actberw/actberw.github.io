### locale的问题

1. 查看所有linux支持的locale

    $ cat /usr/share/i18n/SUPPORTED

2. 系统安装的locale

    $ locale -a

3. 系统默认的locale
    
    $ locale

4. 增加locale, 两种方法:  
1) 编辑/etc/locale.gen, uncomment掉想要支持的locale，执行locale-gen  
2) dpkg-reconfigure locales  
  
5. 设置系统默认的local  
1) dpkg-reconfigure locales  
2) update-locale   (`sudo update-locale LC_ALL=en_US.utf8 LANG=en_US.utf8 LANGUAGE=en_US:en`)  
2) 直接编辑 /etc/default/locale(update-locale修改的文件)  


中文支持参见[fbterm](/posts/linxu/fbterm.html)

/usr/share/locale
/usr/share/i18n/locale

refer:  

- [https://help.ubuntu.com/community/Locale](https://help.ubuntu.com/community/Locale)
- [https://wiki.archlinux.org/index.php/locale#My_system_is_still_using_wrong_language](https://wiki.archlinux.org/index.php/locale#My_system_is_still_using_wrong_language)
