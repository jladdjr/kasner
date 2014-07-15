#!/usr/bin/env python

"""
Call distutils to install Kasner.
"""

from distutils.core import setup

setup(
    name='Kasner',
    version='0.1.0',
    author='James Ladd, Jr.',
    author_email='jladdjr@gmail.com',
    packages=['kasner', 'kasner.test'],
    url='https://github.com/jladdjr/kasner',
    license='LICENSE.txt',
    description='A micro search engine',
    long_description=open('README.txt').read(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Development Status :: 1 - Planning"
        ]

)
