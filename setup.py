#!/usr/bin/env python
# -*- coding: utf-8 -*-
# using helpful guide at: http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html
import sys
from glob import glob
from os.path import splitext, basename
from setuptools import find_packages, setup
# from distutils.core import setup

#if "{}{}".format(sys.version_info.major, sys.version_info.minor) != '27':
#    raise Exception("Error we need to run on python version 2.7 Running on: {}".format(sys.version))

setup(
    name='homeautomation',
    version='0.2dev',
    url='https://github.com/renegaderyu/homeautomation',
    author='Ryan Miguel',
    author_email='miguel.ryanj@gmail.com',
    maintainer='Ryan Miguel',
    maintainer_email='miguel.ryanj@gmail.com',
    description='Home Automation Libs and scripts for my RaspberryPi',
    scripts=glob('bin/*.py') + glob('bin/*.sh'),
    long_description=open('README').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    install_requires=[
        'requests',
        'weather-api'
    ],
)
