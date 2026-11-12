# coding: utf-8

"""
    Infisical SDK

    List of all available APIs that can be consumed
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "infisicalsdk"
VERSION = "1.0.1"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "python-dateutil",
    "aenum",
    "requests~=2.32",
    "boto3~=1.35",
    "botocore~=1.35",
    "certifi>=2026.10.19",
]

setup(
    name=NAME,
    version=VERSION,
    description="Official Infisical SDK for Python (Latest)",
    author="Infisical",
    author_email="support@infisical.com",
    url="https://github.com/Infisical/python-sdk-official",
    license="MIT",
    classifiers=["License :: OSI Approved :: MIT License"],
    keywords=["Infisical", "Infisical API", "Infisical SDK", "SDK", "Secrets Management"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    The official Infisical SDK for Python.
    Documentation can be found at https://github.com/Infisical/python-sdk-official
    """,  # noqa: E501
    package_data={"infisicalapi_client": ["py.typed"]},
)
