# -*- coding: utf-8 -*-
"""
This module contains the tool of comuneimola.compensi
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0.dev0'

tests_require = ['zope.testing']

setup(name='comuneimola.compensi',
      version=version,
      description="Gestione Compensi per il comune di Imola",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
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
