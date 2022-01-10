#creates distributable package
from setuptools import setup

setup(    
    name='packagecalc',
    version='1.0',
    description='package round and potentiation',
    author='me',
    author_email='me@mail.com',
    url='www.mwweb.com',
    packages=['package','package'] #the files (no the folders) into 'package' folder
    )
#->cmd in this directory->python setup.py sdist
#it's created a folder 'dist' in this directory y a foldef 'packagecalc.egg-info'
#to install: go to 'dist' en cmd with cd->pip3 install 'packagecalc-1.0.tar', now is part of syspath. The py what depend it, can be anywhere
#to uninstall: pip3 uninstall packagecalc 