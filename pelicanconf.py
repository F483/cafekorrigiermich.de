#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kristyn Bacon'
SITENAME = u'Cafe Korrigier Mich'
SITESUBTITLE = u'Deutsch sprechen wie die Deutschen'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images', 'files', 'styles', 'scripts']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


##### THEME SETTINGS #####

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEMES = [
    "amelia", "darkly", "paper", "simplex", "yeti", "cerulean", "flatly",
    "readable", "slate", "cosmo", "journal", "readable-old", "spacelab",
    "cupid", "lumen", "sandstone", "superhero", "cyborg", "shamrock", "united",
]
BOOTSTRAP_THEME = BOOTSTRAP_THEMES[17] # see http://bootswatch.com/slate/ for usage
#BOOTSTRAP_NAVBAR_INVERSE = True
#SITELOGO = "images/favicon.png"
FAVICON = 'images/favicon.png'
CUSTOM_CSS = 'styles/cafekorrigiermich.css'
DISPLAY_TAGS_ON_SIDEBAR = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 5
#TWITTER_USERNAME = ""
GOOGLE_ANALYTICS = 'UA-56350575-1'

MENUITEMS = (
    ("Uns",                     "/"),
#    ("Neues",                   "/category/blog.html"),
    ("Lehrer",                  "/pages/lehrer.html"),
    ("Angebot",                 "/pages/angebot.html"),
    ("Anfahrt",                 "/pages/anfahrt.html"),
)

SOCIAL = (
#    ('Facebook',                'https://www.facebook.com/fabe.py'),
#    ('LinkedIn',                'https://www.linkedin.com/profile/view?id=321928002'),
#    ('Twitter',                 'https://twitter.com/fbarkhau'),
#    ('Google+',                 'https://plus.google.com/109332326730675118824/'),
)

LINKS =  (
    ('Facebook',                 'https://www.facebook.com/TODO'),
    ('leo.org',                  'http://www.leo.org/'),
    ('bvg.de',                   'http://bvg.de'),
)

