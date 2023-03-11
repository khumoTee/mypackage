from setuptools import setup, find_packages

setup(name= 'mypackage',
    version='0.1',
    packages= find_packages(exclude=['tests*']),
    license='MIT',
    description= 'EDSA example python package',
    long_description=open('README.md').read(),
    requires= ['numpy'],
    url= 'htts://github.com/<username>/<package-name>',
    author= '<Your name>',
    author_email= '<Your Email>',)
    
