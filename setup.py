# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unifihome', 'unifihome.model', 'unifihome.ui', 'unifihome.ui.systeminfo']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['unifihome = unifihome.cli:main']}

setup_kwargs = {
    'name': 'unifihome',
    'version': '0.1.1',
    'license': 'MIT',
    'description': 'Console based application for monitoring and management of at home UNIFI devices',
    'long_description': None,
    'author': 'Brent Clements',
    'author_email': 'brent.clements@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

