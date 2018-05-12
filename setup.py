from setuptools import setup, find_packages
from codecs import open
from os import path

here =  path.abspath(path.dirname(__file__))

with open(path.join(here,'README.md'),'r',encoding = 'utf-8') as f:
    long_description = f.read()



setup(  name='clctn',
        version='0.1',
        description='some collections for being lazy',
        long_description = long_description,
        url='http://github.com/cathowlet/clctn',
        author='cathowlet',
        author_email='cathowlet@gmail.com',
        license='MIT',
        packages=find_packages(exclude=['contrib', 'docs', 'tests']), # Required
        zip_safe=False)