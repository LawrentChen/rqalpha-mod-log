# !/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='rqalpha-mod-log',
    version="0.1.0",
    description='RQAlpha Mod for logbook',
    packages=find_packages(exclude=[]),
    author='LawrentChen',
    author_email='laurant.chen@gmail.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/lawrentchen/rqalpha-mod-log',
    install_requires=[str(ir.requirement) for ir in parse_requirements("requirements.txt", session=PipSession())],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
