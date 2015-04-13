from setuptools import find_packages, setup


with open('README.rst') as f:
    long_description = f.read()

setup(name='pycat',
      version='0.1.0',
      packages=find_packages(),
      description='netcat, in Python',
      long_description=long_description,
      author='Alistair Lynn',
      author_email='alistair@alynn.co.uk',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: Utilities'
      ],
      install_requires=[
        'docopt >=0.6, <0.7'
      ],
      setup_requires=[
        'nose >=1.3, <2'
      ],
      entry_points={
        'console_scripts': [
          'pycat = pycat.cli:main'
        ]
      })
