import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import speechtools

def readme():
    with open('README.md') as f:
        return f.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-x', '--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        if __name__ == '__main__': #Fix for multiprocessing infinite recursion on Windows
            import pytest
            errcode = pytest.main(self.test_args)
            sys.exit(errcode)

setup(name='speechtools',
      version=speechtools.__version__,
      description='',
      long_description='',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='speech corpus phonetics',
      url='https://github.com/mlml/speechcorpustools',
      author='MLML',
      author_email='michael.e.mcauliffe@gmail.com',
      packages=['speechtools',
                'speechtools.graph',
                'speechtools.sql'],
      install_requires=[
          'sqlalchemy',
          'textgrid',
          'acousticsim',
          'py2neo',
          'polyglotdb'
      ],
    cmdclass={'test': PyTest},
    extras_require={
        'testing': ['pytest'],
    }
      )