# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

try:
    from urlparse import urlparse, parse_qs
except ImportError:  # Python 3
    from urllib.parse import urlparse, parse_qs

from wikimd.base import Page, ROOT_URL
from wikimd.souputils import parse_homemade_dl



class Page(object):
    """
    A Page.
    """


    def __init__(self, ref):
        """
        Create a new Page from a reference, and an optional student
        """
        super(Page, self).__init__(ref)


    def populate(self, soup, session):
        """
        fetch page
        """
