import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirments.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name = "OSHA-tools",
    version = "0.0.1",
    author = "Leland Peterson",
    author_email = "this_is_private@hotmail.com",
    description = ("A set of tools used by nodes and servers."),
    license = "unknown",
    keywords = "home automation",
    url = "Noneyet",
    packages=['OSHA_tools'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=REQUIRED,
)