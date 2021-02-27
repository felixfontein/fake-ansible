
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description='''Fake Ansible package
====================

Install this to satisfy programs which depend on Ansible, but in fact only need ansible-base or ansible-core.

(You need to manually install ansible-base or ansible-core!)
''',
    name='ansible',
    version='23.42.0',
    description='Changelog tool for Ansible-base and Ansible collections',
    packages=[],
    package_dir={"": "."},
)
