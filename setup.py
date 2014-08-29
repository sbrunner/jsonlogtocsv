# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = (
    open(os.path.join(here, 'README.rst')).read() + '\n\n' +
    open(os.path.join(here, 'CHANGES.rst')).read()
)

install_requires = open(os.path.join(here, 'requirements.txt')).read().splitlines()

setup_requires = [
    'nose',
]
tests_require = [
    'coverage',
    'unittest2',
    'testfixtures',
]

setup(
    name='jsonlogtocsv',
    version='0.1.0',
    description="Tools to filter and export a Json log into a scv file",
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    author='Stéphane Brunner',
    author_email='stephane.brunner@camptocamp.com',
    url='http://github.com/sbrunner/jsonlogtocsv',
    license='BSD',
    keywords='gis json log csv',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'jsonlogtocsv = jsonlogtocsv:main',
        ],
    }
)
