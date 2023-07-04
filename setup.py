from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in export_setting/__init__.py
from export_setting import __version__ as version

setup(
	name="export_setting",
	version=version,
	description="This App Used to Set preselected fields for export",
	author="zaid",
	author_email="zaid@standardtouch.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
