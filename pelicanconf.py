#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

base_path = os.path.dirname(os.path.realpath(__file__))

AUTHOR = u'Graham Cox <graham@grahamcox.co.uk>'
SITENAME = u'All about Databases'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['.']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Neo4J', 'http://neo4j.com/'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/grahamcox82'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS=[os.path.join(base_path, 'pelican-plugins')]
PLUGINS = ['i18n_subsites', 'sitemap', 'pelican-page-hierarchy', 'subcategory']

THEME = os.path.join(base_path, 'themes/pelican-bootstrap3')
JINJA_EXTENSIONS = ['jinja2.ext.i18n']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }

}

PATH_METADATA= '(?P<subcategory_path>.*)/.*'
DISPLAY_BREADCRUMBS=True
