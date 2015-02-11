# -*- coding: UTF-8 -*-


class WikipediaServerError(Exception):

    def __init__(self, resp):
        self.msg = u"Server error %s: \"%s\" on %s" % (
            resp.status_code, resp.reason, resp.url)
        super(WikipediaServerError, self).__init__(self.msg)
        self.response = resp

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg

class WikiError(Exception):
    """
    Base exception for WikiError errors
    """

    pass
