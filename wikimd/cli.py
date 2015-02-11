# -*- coding: UTF-8 -*-

from __future__ import print_function

import inspect
from getpass import getpass
from os.path import expanduser
from sys import argv, exit

from wikimd import __version__
from wikimd.exceptions import WikipediaServerError

HELP_FLAGS = ('-h', '-help', '--help')


class WikipediaCli(object):

    def __init__(self, argv):
        self.argv = argv
        self.exe = self.argv.pop(0)
        self.config = DidelConfig.get_default()


    def print_version(self):
        print("WikipediaCli v%s -- http://git.io/wikiMD" % __version__)


    def print_help(self):
        name_offset = len('action_')
        print("\nUsage:\n\t%s <subcommand> args..." % self.exe)
        print("\nAvailable subcommands:\n")
        for mth in dir(self):
            if not mth.startswith('action_'):
                continue
            cmd = getattr(self, mth)
            doc = cmd.__doc__
            name = mth[name_offset:].replace('_', ':')
            print("%s\n%s" % (name, doc.strip('\n')))


    def print_action_help(self, action, params, docstring=''):
        """
        Print an help text for a subcommand
        """
        params = map(lambda s: '<%s>' % s, params)
        print("Usage:\n\t%s %s %s\n" % (self.exe, action, params))
        if docstring:
            print("%s\n" % docstring.strip())


    def run(self):
        """
        Parse the command-line arguments and call the method corresponding to
        the situation.
        """
        argv = self.argv
        argc = len(self.argv)
        if argc == 0:
            return self.print_help()
        action = argv.pop(0)
        argc -= 1
        if action in HELP_FLAGS:
            self.print_version()
            return self.print_help()
        if action in ('-v', '-version', '--version'):
            return self.print_version()
        name = 'action_%s' % action.replace(':', '_')
        if not hasattr(self, name):
            print("Unrecognized action '%s'" % action)
            return self.print_help()
        fun = getattr(self, name)
        spec = inspect.getargspec(fun)
        spec_args = (spec.args or ())[1:]
        spec_defaults = (spec.defaults or ())[1:]
        defaults_len = len(spec_defaults)
        required_len = len(spec_args) - defaults_len
        if argc < required_len or (argc > 0 and argv[0] in HELP_FLAGS):
            defaults = list(reversed(spec_args))[:defaults_len]
            args = []
            for arg in spec_args:
                fmt = '<%s>'
                if arg in defaults:
                    fmt = '[%s]' % fmt
                args.append(fmt % arg)

            if spec.varargs:
                args.append('[<%s...>]' % spec.varargs)
            print("Usage:\n\t%s %s %s" % (self.exe, action, ' '.join(args)))
            return False
        return fun(*argv)


def abort(msg, code=1):
    """
    Print a message and exit.
    """
    print(msg)
    exit(code)


def run():
    """
    Start the command-line app
    """
    try:
        ret = WikiCli(argv).run()
    except KeyboardInterrupt:
        abort("--->[]", 0)
    except WikipediaServerError as e:
        abort("%s" % e)

    exit(1) if ret is None or ret == False else exit(0)
