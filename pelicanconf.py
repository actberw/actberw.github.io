#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'actberw'
SITENAME = u'记录一些工作中的笔记'
# SITEURL = 'http://actberw.github.io'
SITE_SOURCE = u"https://github.com/actberw/actberw.github.io"
THEME = 'zurb-F5-basic'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'
DISPLAY_PAGES_ON_MENU = False
STATIC_PATHS = []

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
