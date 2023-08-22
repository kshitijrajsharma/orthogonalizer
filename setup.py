import io

from setuptools import find_packages, setup

with io.open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="orthogonalizer",
    version="0.0.4",
    url="https://github.com/kshitijrajsharma/orthogonalizer",
    author="Kshitij Raj Sharma",
    author_email="skshitizraj@gmail.com",
    description="A pip installation for orthogonalization of polygons",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="GPL-3.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "shapely<=2.0.1",
        "geopandas<=2.0.3",
    ],
)
