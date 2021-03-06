#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gsoc'
SITENAME = u''
SITEURL = '.'
ARCHIVES_URL = 'archives.html'
TAGS_URL = 'tags.html'
AVATAR_IMG = ''
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'
DISQUS_SITENAME = 'gsocmlpack'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

DEFAULT_PAGINATION = 10
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['assets', 'latex']
THEME = "theme"
SUMMARY_MAX_LENGTH = None
STATIC_PATHS = ['images', 'static/favicon.ico']