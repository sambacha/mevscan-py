from codecs import open
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mevscan",
    description="python mev scan tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    url="https://github.com/sambacha/mevscan-py",
    license="MIT",
    install_requires=["pandas_datareader", "pandas >= 0.20",],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=["Programming Language :: Python :: 3",],
    keywords=["finance", "analysis",],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    python_requires=">=3",
)
