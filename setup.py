from setuptools import setup, find_packages
import os

version = '0.9'

setup(name='gomobile.templates',
      version=version,
      description="Code templates creating Go Mobile for Plone add-ons",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://webandmobile.mfabrik.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gomobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel',
          # -*- Extra requirements: -*-
      ],      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      gomobile_theme = gomobile.templates.theme:Theme  
        
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )