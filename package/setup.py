import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

with open("VERSION", "r") as vfh:
	l = vfh.read().split('.')
	version = l[0]+'.'+l[1]+'.'+str(int(l[2])+1)
	vfh.close()

setuptools.setup(
	name="litegrade",
	version=version,
	author="Justin Morgan",
	author_email="2justinmorgan@gmail.com",
	description="An intuitive grading tool for IPython notebooks",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/2justinmorgan/litegrade",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

with open("VERSION", "w") as vfh:
	vfh.write(version)

