#!/usr/bin/env python
from distutils.core import setup

setup(name='git-it',
    version='1.1',
    description='Issue tracking for git repositories',
    author='Don Grote',
    author_email='dgrote@tacnetsol.com',
    packages=['gitit'],
    scripts=['bin/it'],
    )
