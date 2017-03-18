try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'project: ex47',
    'author': 'Mingyi Zhang',
    'url': 'NA',
    'download_url': 'NA',
    'author_email': 'mingyizhang1987(AT)gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
