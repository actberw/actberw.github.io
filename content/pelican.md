Title: pelican
Tags: python, pelican, latex
Date: 2014-06-05

### 安装

依赖  

At this time, Pelican is dependent on the following Python packages:

* feedgenerator, to generate the Atom feeds
* jinja2, for templating support
* docutils, for supporting reStructuredText as an input format

If you’re not using Python 2.7, you will also need the argparse package.  Optionally:

- pygments, for syntax highlighting
- Markdown, for supporting Markdown as an input format
- Typogrify, for typographical enhancements

安装

参考refer[0]

### 配置

timezone

    TIMEZONE = 'Asia/Shanghai'

文章发布时间

    DEFAULT_DATE = 'fs'

文章url

    ARTICLE_URL = 'posts/{category}/{slug}.html'
    ARTICLE_SAVE_AS = 'posts/{category}/{slug}.html'

文章名字

    FILENAME_METADATA = '(?P<slug>.*)'

其他配置参见[官方文档](http://docs.getpelican.com/en/3.1.1/settings.html)


### File metadata

支持下面几种

    Title: My super title
    Date: 2010-12-03 10:20
    Tags: thats, awesome
    Category: yeah
    Slug: my-super-post
    Author: Alexis Metaireau
    Summary: Short version for index and feeds

    This is the content of my super blog post.

### 部署到github

github pages有两种:

- user or group page (依赖master分支)
- project page(依赖gh-pages分支)

这里主要说下user or group page, 下面的操作是为了把原数据, 和生成的html页面放在同一个版本库中, source分支存原数据, master 存html页面, 借助于ghp-import工具.

- 创建一个usrname.github.io 库
- 本地`pelican-quickstart` 创建一个博客
    
        make blog
        cd blog
        pelican-quickstart

- 链接远程库(username换成实际的名字)

        git remote add origin git@github.com:username/username.github.io.git
        git pull origin master

- 编辑.gitignore, 忽略output目录, pid文件, .pyc文件

        echo "output/" >> .gitignore
        echo "*.pid" >> .gitignore
        echo "*.pyc" >> .gitignore

- 创建source分支

        git co -b source (可能需要--orphan选项)

- 修改Makefile, 把github: publish 下面的两行换成如下:

        ghp-import -b master -m 'Update site at $(shell "date")' $(OUTPUTDIR)
        git push origin master

以后所有操作都在source分支下进行，就可以执行make github 发布博客, `git add .`保存源码推到source分支.

注: make github之后需要等一会才能生效.

### 添加latex 插件

使用MathJax Latex JavaScript库来渲染Latex语法.

在 template/base.html 文件中增加如下代码

    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
          "HTML-CSS": {
              styles: {
                  ".MathJax .mo, .MathJax .mi": {color: "black ! important"}}
          },
          tex2jax: {inlineMath: [['$','$'], ['\\\\(','\\\\)']],processEscapes: true}
      });
    </script>

    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>

参见refer[1]

refer:

- [0][http://www.linuxzen.com/shi-yong-pelicanda-zao-jing-tai-bo-ke.html](http://www.linuxzen.com/shi-yong-pelicanda-zao-jing-tai-bo-ke.html)
- [1][http://www.southampton.ac.uk/~fangohr/blog/setting-up-pelican-how-to-make-equations-work.html](http://www.southampton.ac.uk/~fangohr/blog/setting-up-pelican-how-to-make-equations-work.html)
