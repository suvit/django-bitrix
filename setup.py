# -*- coding: utf-8 -
#
# This file is part of django-tecdoc released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

setup(
    name='django-bitrix',
    version=__import__('bitrix').VERSION,

    description='Itegration django and bitrix db',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/django-bitrix',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['django>=1.4',
                      'django-appconf',
                      ],
    include_package_data=True,
)
