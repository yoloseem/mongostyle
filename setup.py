import os.path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from mongostyle.version import VERSION


def get_readme(readme='README.rst'):
    try:
        with open(os.path.join(os.path.dirname(__file__), readme)) as f:
            return f.read()
    except:
        return ''


setup(name='mongostyle',
      author='Hyunjun Kim',
      author_email='kim@hyunjun.kr',
      maintainer='Hyunjun Kim',
      maintainer_email='kim@hyunjun.kr',
      packages=['mongostyle'],
      version=VERSION,
      url='https://github.com/kimjayd/mongostyle',
      description='implements a MongoDB mapper on Python',
      long_description=get_readme(),
      install_requires=['pymongo'],
      extras_require={'docs': ['Sphinx']},
      tests_require=['Attest'],
      test_loader='attest:auto_reporter.test_loader',
      test_suite='mongostyletests.suite',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Topic :: Database',
          'Programming Language :: Python',
      ]
)
