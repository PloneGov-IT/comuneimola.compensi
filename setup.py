# -*- coding: utf-8 -*-
"""
This module contains the tool of comuneimola.compensi
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2'

tests_require = ['zope.testing']

setup(name='comuneimola.compensi',
      version=version,
      description="Fees management for the town of Imola - Under Italian Law, the institutional websites of the cities shall contain a detailed list of the amounts of all the contracts (herein we will use the term \"fees\") drawn up with external professionals. This product implements Plone with two new custom archetypes, \"Fees Area\" and \"Fee\".",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 3.3',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='Art18 DL 83/2012 compensi comuneimola',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://plone.org/products/comuneimola.compensi',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['comuneimola', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'collective.js.datatables',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='comuneimola.compensi.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
