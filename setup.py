import os

from setuptools import find_packages
from setuptools import setup

import django_xmlrpc_dx


setup(name='django-xmlrpc-dx',
      version=django_xmlrpc_dx.__version__,

      description='XML-RPC Server App for the Django framework.',
      long_description=open(os.path.join('README.rst')).read(),
      keywords='django, service, xmlrpc',

      author='rubeon',
      author_email='rubeon@gmail.com',
      maintainer='rubeon',
      maintainer_email='rubeon@gmail.com',
      url='https://github.com/rubeon/django-xmlrpc',

      packages=find_packages(),
      classifiers=[
          'Framework :: Django',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules'],

      license='New BSD License',
      include_package_data=True,
      zip_safe=False
      )
