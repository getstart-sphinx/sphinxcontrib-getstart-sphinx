# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

long_desc = open('README.rst').read()

requires = ['Sphinx>=1.6', 'sphinxcontrib-reviewbuilder>=0.0.8']

setup(
    name='sphinxcontrib-getstart-sphinx',
    version='1.0.0',
    url='https://github.com/getstart-sphinx/sphinxcontrib-getstart-sphinx',
    license='BSD',
    author='Takeshi KOMIYA',
    author_email='i.tkomiya@gmail.com',
    description='Sphinx extensions for "Getting Started with Sphinx 2nd Edition"',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
