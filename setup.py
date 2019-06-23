"""
argparse-schema
Parse Argument with JSON Schema
Author: SF-Zhou
Date: 2019-04-10
"""

from setuptools import setup

name = 'argparse-schema'
module = name.replace("-", "_")
setup(
    name=name,
    version='0.0.7',
    description='Parse Argument with JSON Schema',
    url=f'https://github.com/FebruaryBreeze/{name}',
    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',
    keywords='Argument Schema',
    entry_points={
        'console_scripts': [f'{name}={module}:main'],
    },
    py_modules=[f'{module}']
)
