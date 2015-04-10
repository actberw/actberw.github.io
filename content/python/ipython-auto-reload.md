Title: ipython 自动relaod模块
Tags: python, ipython
Date: 2015-04-10 10:00:00

在用ipython中经常会遇到这样的情况: 已经import 一个模块了但是之后又对这个模块做了修改, 这时候需要手动reload或者退出重新import. 下面的配置可以自动的reload已经import的模块.

首先创建ipython profile.

    ipython profile create

编辑产生得配置文件一般是 `/.ipython/profile_default/ipython_config.py `, 取消 `c.InteractiveShellApp.extensions = []` 注释, 增加下面两行

    c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
    c.InteractiveShellApp.exec_lines.append('%autoreload 2')

也可以加条注释

    c.InteractiveShellApp.exec_lines.append('print "Warning: disable autoreload to improve performance." ')

autoreload 的更多参数可以, 在ipython中执行下面两行查看帮助.

    import autoreload
    autoreload?


refer:

- [http://www.reddit.com/r/Python/comments/rsfsi/tutorial_spend_30_seconds_setting_up/](http://www.reddit.com/r/Python/comments/rsfsi/tutorial_spend_30_seconds_setting_up/)
