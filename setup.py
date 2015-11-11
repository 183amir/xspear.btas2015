#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Elie Khoury <Elie.Khoury@idiap.ch>
# Sat Aug 31 16:39:23 CEST 2013
#
# Copyright (C) 2012-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name='xspear.btas2015',
    version='2.0.1a',
    description='On the Vulnerability of Speaker Verification to Realistic Voice Spoofing',
    url='https://pypi.python.org/pypi/spear.btas2015',
    license='GPLv3',
    keywords = "Speaker verification, Spoofing, Vulnerability, Database",
    author='Elie Khoury',
    author_email='Elie.Khoury@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
   
    
    entry_points={
      'console_scripts': [
        'evaluate_vulnerability.py      = xspear.btas2015.script.evaluate_vulnerability:main'
        ],
        
      'bob.bio.database': [
        'avspoof            = xspear.btas2015.config.database.avspoof:database',
       ],
      'bob.bio.algorithm': [
        'ivec-avspoof  = xspear.btas2015.config.algorithm.ivec_avspoof:algorithm', # I-Vector config used for AVspoof
        'isv-avspoof  = xspear.btas2015.config.algorithm.isv_avspoof:algorithm', # ISV config used for AVspoof
      ],  
      },


install_requires=[
        "setuptools", # for whatever
        "bob.bio.spear",
        "bob.bio.gmm",    
        "bob.db.avspoof_btas2015"    
    ],


    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
)
