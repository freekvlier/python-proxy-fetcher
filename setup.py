from setuptools import setup, find_packages

# Read the contents of your requirements file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='proxyfetcher',
    version='0.1',
    packages=find_packages(),
    description='A simple proxy fetching tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/proxyfetcher',
    install_requires=required,  # Use the list read from the requirements file
)