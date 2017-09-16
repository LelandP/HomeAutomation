import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirments.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name = "OSHA-nodes",
    version = "0.0.1",
    author = "Leland Peterson",
    author_email = "this_is_private@hotmail.com",
    description = ("A set of tools/nodes for a server."),
    license = "unknown",
    keywords = "home automation",
    url = "Noneyet",
    packages=['OSHA_nodes', 'OSHA_nodes.resources'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
    ],
    package_data={'': ['api.yaml']},
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['OSHA-Water=OSHA_nodes.sensor:main']
    },
)