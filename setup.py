#!/usr/bin/env python

from setuptools import setup, find_packages

import paypal

setup(
    name='django-paypal',
    version="0.1.2.",
    author='John Boxall',
    maintainer="Matt Warren",
    url='http://github.com/johnboxall/django-paypal',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating PayPal Payments Standard or Payments Pro',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)

