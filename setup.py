# Modified by MrBlake for the MRB NetBox Topology Views fork: https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views
# Based on mattieserver/netbox-topology-views (Apache License 2.0). See the LICENSE and NOTICE files.
from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).parent / "README.md"
long_description = readme.read_text()

setup(
    name="netbox-topology-views",
    version="4.5.2",
    description="A NetBox plugin to create Topology maps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views",
    author="Mattijs Vanhaverbeke",
    maintainer="MrBlake",
    license="Apache-2.0",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    keywords=["netbox-plugin"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Source": "https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views",
        "Upstream": "https://github.com/mattieserver/netbox-topology-views",
    },
)
