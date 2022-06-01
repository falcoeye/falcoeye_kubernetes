#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

NAME = "falcoeye_kubernetes"
DESCRIPTION = "k8s config files for falcoeye"
URL = "https://github.com/falcoeye/falcoeye_kubernetes"
AUTHOR = "falcoeye Team"

REQUIRED = ["kubernetes", "requests", "PyYAML"]

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), about)


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    url=URL,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=REQUIRED,
    license="MIT",
    keywords="falcoeye",
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
