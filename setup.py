from setuptools import setup, find_packages

# Read the contents of your requirements file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='proxyfetcher',
    version='1.0.0',
    packages=find_packages(),
    description='A proxy fetching tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Freek van Lier',
    author_email='contact@freekvanlier.nl',
    url='https://github.com/freekvlier/python-proxy-fetcher',
    install_requires=required,  # Use the list read from the requirements file
)