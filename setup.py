try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="exo-pyface",
    version="0.1.0",
    author="Shankhanil Ghosh",
    author_email="shankha.rik@gmail.com",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
