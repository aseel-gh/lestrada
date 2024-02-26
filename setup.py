from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lestrada/__init__.py
from lestrada import __version__ as version

setup(
	name="lestrada",
	version=version,
	description="Erpnext 14 ",
	author="Aseel",
	author_email="aseel.gharbia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
