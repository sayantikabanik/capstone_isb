"""
Package manager for analysis_framework
"""

from pathlib import Path
from setuptools import find_packages, setup

setup(
    author="sayantikabanik",
    description="Forecasting FP2",
    include_package_data=True,
    name="analysis_framework",
    packages=find_packages(),
    url="https://github.com/sayantikabnik/FP2",
    version="1.0.0")
