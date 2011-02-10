# -*- coding: utf-8 -*-
"""Setup for quotationtool.relation package

$Id$
"""
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name='quotationtool.relation'

setup(
    name = name,
    version='0.1.0',
    description="Relation schema for the quotationtool application",
    long_description=(
        read('README')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'quotationtool', 'relation', 'README.txt')
        + '\n' +
        'Download\n'
        '********\n'
        ),
    keywords='quotationtool, blue bream',
    author=u"Christian Luck",
    author_email='cluecksbox@googlemail.com',
    url='',
    license='ZPL 2.1',
    # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Environment :: Web Environment',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                 'Framework :: Zope3',
                 ],
    packages = find_packages('src'),
    namespace_packages = ['quotationtool',],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'setuptools',
        'quotationtool.site',
        'zope.interface',
        'zope.schema',
        'zope.component',
        'zope.intid',
        'zope.keyreference',
        'zc.relation',
        'zope.app.appsetup',
        'zope.processlifetime',
        ],
    extras_require = dict(
        test = [
            'zope.testing',
            'zope.configuration',
            'zope.container',
            ],
        ),
    )
