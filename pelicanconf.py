#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['/Users/vince/pelican-plugins/']
PLUGINS = ["render_math"]

AUTHOR = u'Vincent Alexander Croft'
SITENAME = u'Higgles Abound Blog'
SITEURL = ''


PATH = 'content'
STATIC_PATHS = ['images']
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

#HEADER_COVER = 'static/atlas.jpg'
THEME = 'pelican-clean-blog'
#THEME_STATIC_PATHS = ['static']

MENUITEMS = (('TO THE TOP',"http://vincentcroft.web.cern.ch/"),
             ('RESEARCH', "http://vincentcroft.web.cern.ch/vincentcroft/#Research"),
             ('TEACHING', "http://vincentcroft.web.cern.ch/vincentcroft/#Teaching"),
             ('PERSONAL', "http://vincentcroft.web.cern.ch/vincentcroft/#Personal")
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/vincecr0ft'),
          ('github', 'https://github.com/vincecr0ft'),
          ('facebook','https://facebook.com/vince.croft'),
          ('flickr','https://www.flickr.com/photos/16758327@N04'),
          ('envelope','mailto:vincecroft@gmail.com'))


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
