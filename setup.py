from setuptools import setup, find_packages

# Customize
package_name = 'Algorithms'
version = '0.1.0'
description = 'A variety of different algorithms implemented in Python'
install_requires = [
]


setup(
    name=package_name,
    version=version,
    description=description,
    url='https://github.com/dlomelin/%s' % (package_name),
    author='David Lomelin',
    author_email='david.lomelin@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
)
