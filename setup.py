# -*- coding: UTF-8 -*-

import setuptools
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='wikimd/__init__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='WikiMD',
    version=verstr,
    author='Salmon Thomas',
    author_email='ths871@gmail.com',
    packages=['wikimd'],
    url='https://github.com/tsalmon/wikimd',
    license=open('LICENSE', 'r').read(),
    description='Convert wikipedia\'s page into markdown style',
    long_description=open('README.md', 'r').read(),
    install_requires=[
        'beautifulsoup4 >= 4.3.2',
        'lxml >= 3.4.0',
        'ordereddict == 1.1',
        'requests >= 2.4.2',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts':[
            'wikimd = wikimd.cli:run'
        ]
    },
)
