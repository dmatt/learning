# Project installation script

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'Project journal',
    'author': 'Daniel Matteson',
    'url': 'URL to get it at',
    'download_url': 'download URL',
    'author_email': 'daniel.matteson@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['journal'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)

