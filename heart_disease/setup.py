from setuptools import find_packages, setup

setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="Example of ml project",
    author="Khubbatulin Mark email: markhubbatulin@gmail.com",
    install_requires=[
        "setuptools~=52.0.0",
        "pandas~=1.2.4",
        "scikit-learn~=0.23.2",
        "numpy~=1.19",
        "pytest~=6.2.3",
        "py~=1.10.0",
        "pyyaml~=5.4.1"
    ],
    license="MIT",
)
