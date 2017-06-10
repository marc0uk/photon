#!/usr/bin/env python
import os
import sys
from setuptools import setup

# Load the __version__ variable without importing the package
exec(open('photon/version.py').read())

setup(name='photon',
        version=__version__,
        description="PhotPipe python toolbox",
        author='Marco Riello',
        author_email='riellomarco@gmail.com',
        license='MIT',
        packages=[
            'photon',
            'photon.plotting'
            ],
        install_requires=['astropy>=1.3.0',
            'numpy',
            'matplotlib>=2.0.0',
            'pandas'],
        classifiers=[
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering :: Astronomy",
            ],
        )

