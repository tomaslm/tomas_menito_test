# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="sample",
    version="1.0.0",
    description="Techinical test",
    long_description=readme,
    author="Tomas Labella Menito",
    author_email="tomaslm@hotmail.com",
    url="https://github.com/tomaslm/tomas_menito_test",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
