from setuptools import setup, find_packages
from pathlib import Path

from admin_shortcuts import version

HERE = Path(__file__).parent

setup(
    name='django-admin-shortcuts',
    author='Ales Kocjancic',
    author_email='alesdotio@gmail.com',
    version=version,
    description='Add simple and pretty shortcuts to the django admin homepage.',
    long_description=(HERE / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/big-jobs/django-admin-shortcuts',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=[
        'Django>=4.0',
    ],
    download_url='https://github.com/big-jobs/django-admin-shortcuts/tarball/' + version,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
)
