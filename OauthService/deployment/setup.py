from setuptools import setup

requires = [
    'flask',
    'Flask-SQLAlchemy',
    'oursql',
    'flask-cors',
    'flask-testing',
    'requests',
    'pyyaml',
    'Flask',
    'Flask-Login',
    'Flask-OAuth',
    'Flask-SQLAlchemy',
    'Flask-Testing',
    'Jinja2',
    'MarkupSafe',
    'SQLAlchemy',
    'Werkzeug',
    'argparse',
    'asn1crypto',
    'certifi',
    'cffi',
    'chardet',
    'click',
    'client',
    'cryptography',
    'enum34',
    'http',
    'httplib2',
    'idna',
    'ipaddress',
    'itsdangerous',
    'oauth2',
    'oauthlib',
    'pyOpenSSL',
    'pycparser',
    'requests',
    'requests-oauthlib',
    'six',
    'urllib3',
    'wsgiref'
]

setup(
    name='lds',
    version='2.0',
    install_requires=requires
)