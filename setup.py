#!/usr/bin/env python
# $Id$

import glob
import os
import platform

from setuptools import setup

PACKAGE_NAME = "impacket-armis"

if platform.system() != 'Darwin':
    data_files = [(os.path.join('share', 'doc', PACKAGE_NAME), ['README.md', 'LICENSE']+glob.glob('doc/*'))]
else:
    data_files = []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# This is based on version 0.9.23 of impacket, with re-versioning starting at 1.0.
setup(name = PACKAGE_NAME,
      version = "1.1.7",
      description = "Network protocols Constructors and Dissectors",
      url = "https://www.secureauth.com/labs/open-source-tools/impacket",
      author = "SecureAuth Corporation",
      author_email = "oss@secureauth.com",
      maintainer = "SecureAuth's Innovation Labs ",
      maintainer_email = "oss@secureauth.com",
      license = "Apache modified",
      long_description = read('README.md'),
      long_description_content_type="text/markdown",
      platforms = ["Unix","Windows"],
      packages=['impacket', 'impacket.dcerpc', 'impacket.dcerpc.v5', 'impacket.dcerpc.v5.dcom',
                'impacket.krb5', 'impacket.ldap', 
                ],
      data_files = data_files,
      install_requires=['pyasn1>=0.2.3', 'pycryptodomex', 'pyOpenSSL>=0.13.1', 'six', 'ldap3>=2.5,!=2.5.2,!=2.5.0,!=2.6', 'ldapdomaindump>=0.9.0'],
      extras_require={
                      'pyreadline:sys_platform=="win32"': [],
                    },
      classifiers = [
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 2.7",
      ]
      )
