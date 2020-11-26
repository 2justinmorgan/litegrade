import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="litegrade",
    version="0.0.1",
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
