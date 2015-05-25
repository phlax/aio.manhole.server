"""
aio.manhole
"""
import sys
from setuptools import setup, find_packages

version = "0.0.1"


install_requires = [
    'setuptools',
    'aiomanhole']

if sys.version_info < (3, 4):
    install_requires += ['asyncio']

tests_require = install_requires + ['aio.testing', "telnetlib3"]

setup(
    name='aio.manhole',
    version=version,
    description="Aio core utils",
    classifiers=[
        "Programming Language :: Python 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Ryan Northey',
    author_email='ryan@3ca.org.uk',
    url='http://github.com/phlax/aio.manhole',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['aio'],
    include_package_data=True,
    zip_safe=False,
    tests_require=tests_require,
    install_requires=install_requires,
    entry_points={})
