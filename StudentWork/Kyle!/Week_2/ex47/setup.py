try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LPTHW Exercise 47',
    'author': 'Kyle Joecken',
    'url': 'http://www.google.com',
    'download_url': '',
    'author_email': 'joecken@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
