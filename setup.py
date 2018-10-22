from setuptools import setup, find_packages

with open("README.md") as file:
	long_desc = file.read()

setup(
	name="pybuff",
	author="BigHeadGeorge",
	author_email="tucker1014@hotmail.com",
	url="https://github.com/BigHeadGeorge/overbuff.py",
	version="0.0.1",
	description="A scraper for grabbing info from Overbuff.",
	long_description=long_desc,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operation System :: OS Independent"
	]
)
