try:
	from setuptools import setup
except ImportError:
	from distutils.cor import setup
	
config = {
	'description' : 'Boats Game',
	'author': 'Emily Cain',
	'url': 'emcain.net'
	'download_url': 'Where to download it.',
	'author_email': 'contact@emcain.net'
	'version': '0.1'
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)