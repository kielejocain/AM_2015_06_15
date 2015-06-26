try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Pet - Tamagotchi Pretender',
    'author': 'Kyle Joecken',
    'url': 'http://www.google.com',
    'download_url': '',
    'author_email': 'joecken@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['my_pet'],
    'scripts': ['my_pet.py'],
    'name': 'my_pet'
}

setup(**config)
