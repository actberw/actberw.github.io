Title: bash tab自动补全

### bash completion

### redline配置

在 "~/.inputrc" 中增加如下三行:

    # 忽略大小写
    set completion-ignore-case on
    set show-all-if-ambiguous on
    # 使用vim补全方式
    TAB: menu-complete

`man bash` 查看 READLINE 部分.

refer:

- http://www.nenew.net/arch-linux-sudo-auto.html
https://wiki.archlinux.org/index.php/Bash
http://www.linuxjournal.com/content/more-using-bash-complete-command

- [ReadLine](https://wiki.archlinux.org/index.php/Readline)
