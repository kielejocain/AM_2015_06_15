try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

config = {
	'description': 'Learn Python the Hard Way: ex48',
	'author': 'Ariel Kaplan',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'ariel@arielkaplan.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)