from setuptools import setup

setup(
    name='cinemascore.py',
    author='XenonNSMB',
    version='0.1',
    packages=['cinemascore',],
    license='MIT License',
    summary='A tiny Python library for getting Cinemascore movie grades.',
    home-page='https://github.com/xenonnsmb/cinemascore.py',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.18.4",
        "lxml >= 4.1.1",
    ],
)