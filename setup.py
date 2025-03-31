from setuptools import setup, find_packages

setup(
    name="listConversions",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    author="Dementia Gaming",
    description="A package for converting lists to different formats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DementiaGaming/List-Conversions-Package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
