[![Release](https://github.com/DiogoCarapito/python_package_template/actions/workflows/release.yaml/badge.svg)](https://github.com/DiogoCarapito/python_package_template/actions/workflows/release.yaml)

# python_package_template
Template for a python package
Package available on [PyPI](https://pypi.org/project/templatepackagedc/)
Source code on [GitHub](https://github.com/DiogoCarapito/python_package_template)

It uses the following tools:
- setup.py
- pyproject.toml


## Cheatsheet

### venv
create venv
```bash
python3 -m venv .venv
```

activate venv
```bash
source .venv/bin/activate
```

### Build package

```bash
python3 setup.py sdist bdist_wheel
```

### Use twine to upload to PyPI
```bash
twine check dist/*
````
```bash
twine upload dist/*
```

## Useful links

PyPi
- [https://pypi.org/](https://pypi.org/)
- [https://test.pypi.org/](https://test.pypi.org)
- [https://pypi.org/classifiers/](https://pypi.org/classifiers/)

PyPA
- [https://packaging.python.org/en/latest/overview/](https://packaging.python.org/en/latest/overview/)
- [https://packaging.python.org/guides/distributing-packages-using-setuptools/](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

Sample Project
- [https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)

Twine
- [https://twine.readthedocs.io/en/stable/](https://twine.readthedocs.io/en/stable/)

Legal
- [https://www.tldrlegal.com/](https://www.tldrlegal.com/)
- [https://choosealicense.com/](https://choosealicense.com/)

Youtube tutorials
- [https://www.youtube.com/watch?v=v4bkJef4W94](https://www.youtube.com/watch?v=v4bkJef4W94)


Tutorials
- [https://www.youtube.com/watch?v=tEFkHEKypLI](https://www.youtube.com/watch?v=tEFkHEKypLI)
- [https://www.youtube.com/watch?v=WGsMydFFPMk](https://www.youtube.com/watch?v=WGsMydFFPMk)
- [https://www.youtube.com/watch?v=5KEObONUkik](https://www.youtube.com/watch?v=5KEObONUkik)
