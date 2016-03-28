import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_jinja2',
    'psycopg2',
    'requests'
]

tests_require = ['pytest', 'tox', 'pytest-cov', 'webtest']
dev_requires = ['ipython', 'pyramid_ipython']

setup(name='crimemapper',
      version='0.0',
      description='crimemapper',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author=['Selena Flannery', 'Nadia Bahrami', 'Michael Sullivan',
              'Mike Harrison', 'Wenjing Qiang'],
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='crimemapper',
      install_requires=requires,
      extras_require={
        'test': tests_require,
        'dev': dev_requires,
      },
      entry_points="""\
      [paste.app_factory]
      main = crimemapper:main
      [console_scripts]
      initialize_db = crimemapper.scripts.initializedb:main
      """,
      )
