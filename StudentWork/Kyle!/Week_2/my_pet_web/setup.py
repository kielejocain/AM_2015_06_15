try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Pet Web App',
    'author': 'Kyle Joecken',
    'url': 'http://www.google.com',
    'download_url': '',
    'author_email': 'joecken@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['my_pet_web'],
    'scripts': [],
    'name': 'my_pet_web'
}

setup(**config)
