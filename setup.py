# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = []
with open('requirements.txt') as f:
    lines = f.readlines()
    for line in lines:
        requirements.append(line)

print(requirements)

setup(
    name='app',
    version='0.1.0',
    description='Application to read from kafka',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Dipayan Chattopadhyay',
    author_email='dipayan.chatopadhyay@nordstrom.com',
    url='https://gitlab.nordstrom.com',
    license=license,
    install_requires=requirements,
    include_package_data=True,
    test_requires=['pytest'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages=find_packages(exclude=('tests', 'docs'))
)

