from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in assignment_test/__init__.py
from assignment_test import __version__ as version

setup(
	name="assignment_test",
	version=version,
	description="Customisations in Item Doctype",
	author="Aashish Vashisht",
	author_email="aashishvashisht6@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
