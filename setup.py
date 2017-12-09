# coding=utf-8
from setuptools import find_packages, setup

# noinspection PyProtectedMember
from pytio import __version__ as version

setup(
    name='pytio',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing',
    ],
    author='Thomas Ward',
    author_email='teward@dark-net.io',
    description="A library to interact with TIO.run and execute code, as well as return the results for the execution.",
    long_description="A library to interact with TIO.run and execute code, as well as return the results for the "
                     "execution. This is basically a Python version of https://github.com/SocraticPhoenix/TioJ but "
                     "using Pythonic approaches and software rather than the complex Java solutions.",
    license='AGPLv3+',
    url='https://github.com/teward/pytio',
    download_url='https://pypi.python.org/pypi/pytio',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='tryitonline tio',
    platforms='any',
    test_suite='test_tio',
)
