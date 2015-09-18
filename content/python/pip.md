Title: pip 安装

debian 默认没有pip, 也没有easy_install(setuptools包含的命令)

    # 安装setuptools
    wget https://bootstrap.pypa.io/ez_setup.py -O -|sudo python

    # 安装pip
    sudo easy_install pip

常用选项:

- `--user`, 安装到用户home目录，适用于没有sudo权限.

https://pip.pypa.io/en/latest/user_guide.html

