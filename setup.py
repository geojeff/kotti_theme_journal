import os

from setuptools import find_packages
from setuptools import setup

version = '0.1'
project = 'kotti_theme_journal'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name=project,
    version=version,
    description="Journal theme from http://bootswatch.com/journal/ for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        'License :: Repoze Public License',
    ],
    keywords='kotti theme',
    author='Jeff Pittman',
    author_email='geojeff@me.com',
    url='https://github.com/geojeff/kotti_theme_journal',
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Kotti',
    ],
    entry_points={
        'fanstatic.libraries': [
            'kotti_theme_journal = kotti_theme_journal:library',
        ],
    },
    extras_require={
        'development': [
            'minify',
        ]
    },
    message_extractors={
        'kotti_theme_journal': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)
