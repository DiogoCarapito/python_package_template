from setuptools import setup, find_packages
import pathlib


NAME = "templatePackageDC"
VERSION = "0.0.1"
DESCRIPTION = "Template of a Python package"
SOURCE = "https://github.com/DiogoCarapito/python_package_template"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=(pathlib.Path(__file__).parent.resolve() / "README.md").read_text(
        encoding="utf-8"
    ),
    long_description_content_type="text/markdown",
    url=SOURCE,
    author="Person Name",
    author_email="person.name@mail.com",
    license="Apache License 2.0",
    project_urls={
        "Bug Reports": SOURCE + "/issues",
        "Source": SOURCE,
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="template package",
    python_requires=">=3.7,<3.12",
    install_requires=[],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
