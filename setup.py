#!/usr/bin/env python
"""
Setup script for Rutgers Repository Utils.
"""

import distutils
import sys

from distutils.core import setup

setup(name              = 'rutgers-repoutils',
      version           = '1.0',
      description       = 'Python scripts for repository management',
      author            = 'Open System Solutions',
      author_email      = 'oss@oss.rutgers.edu',
      url               = 'https://github.com/oss/rutgers-repository-utils',
      license           = 'GPLv2+',
      platforms         = ['linux'],
      long_description  = """These Python scripts are based on yum-utils and
                             createrepo. Together, they create repository
                             directories and do dependency checking.""",
      packages          = ['rutgers-repoutils'],
      package_dir       = {'rutgers-repoutils' : 'lib'},
      scripts           = ['bin/repoclosure'])
