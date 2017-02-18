from setuptools import setup

__version__ = '0.1'

setup(
    name='runalysis',
    version=__version__,
    author='Harris Arvanitis.',
    author_email='xaris@gmx.com',
    py_modules=[''],
    url='',
    license='',
    description='Analisis tools for Garmin Data',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy","python-tcxparser","matplotlib","pandas",
     ]
)

