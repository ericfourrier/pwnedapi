from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pwnedapi',
      version="0.1",
      description='pwnedapi is a python wrapper of the https://haveibeenpwned.com api',
      long_description=readme(),
      author=['Eric Fourrier'],
      author_email='ericfourrier0@gmail.com',
      license='MIT',
      url='https://github.com/ericfourrier/pwnedapi.git',
      packages=['pwnedapi'],
      test_suite='test',
      install_requires=[
          'requests']
      )
