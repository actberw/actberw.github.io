#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'actberw'
SITENAME = u'记录一些工作中的笔记'
SITEURL = 'http://actberw.github.io'
SITE_SOURCE = u"https://github.com/actberw/actberw.github.io"
THEME = 'zurb-F5-basic'
DEFAULT_DATE = 'fs'

TIMEZONE = 'Asia/Shanghai'

ARTICLE_URL = 'posts/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}.html'
FILENAME_METADATA = '(?P<slug>.*)'

DEFAULT_LANG = u'cn'
STATIC_PATHS = ['img']
DISPLAY_PAGES_ON_MENU = False

# tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('github', 'https://github.com/actberw'),)

# Social widget
SOCIAL = (('weibo', 'http://weibo.com/u/1950796544'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
