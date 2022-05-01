import os

import setuptools
from setuptools import find_packages

DIR = os.path.dirname(os.path.realpath(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

except ImportError:
    print("Cannot import bdist_wheel, upgrade wheel package")
    bdist_wheel = None

package = "falcoeye_kubernetes"
packages = [f"{package}"] + [f"{package}.{p}" for p in find_packages(f"../{package}")]

setuptools.setup(
    name=f"{package}",
    description="Falcoeye kubernetes library",
    long_description=long_description,
    url="https://github.com/falcoeye/falcoeye_kubernetes",
    packages=packages,
    package_dir={package: f"{DIR}/."},
    zip_safe=False,
    data_files=[
        ("", ["README.md"]),
    ],
)
wheel = os.path.realpath(DIR + "/dist")
print(f"Python wheel saved: {wheel}")
