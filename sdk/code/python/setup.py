import importlib
import os
import pathlib

import setuptools

version_module_fp = os.path.join("idnorm_ddx", "version.py")
spec = importlib.util.spec_from_file_location(name="version", location=version_module_fp)
vmodule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vmodule)
version = vmodule.VERSION



setuptools.setup(
    name='idnorm-ddx',
    version=version,
    description='Client package for integrating Idnorms document data extraction service',
    url='https://github.com/idnorm/document-data-extraction/clients/python',
    author='Idnorm',
    author_email='dev@idnorm.com',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]) + ['idnorm_ddx/google/api'],
    install_requires=pathlib.Path("requirements.txt").read_text().splitlines(),
    python_requires=">= 3.8",
)