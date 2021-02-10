# blueprint-python
A template repository for Python projects. Includes a template class ( Blueprint), a class call (run.py), unit tests, 
and a setup.py enabling installation as a Python package.

## Preliminaries
- Tested on Ubuntu 18.04, bionic

- Python version >=3.7 to enable type annotation.

        virtualenv -p python3.7 venv

## Dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    pip install -r requirements-test.txt

## Installation
Install package as editable

    pip install -e .

## Resources
For information on python packages, see PyPA docs:

https://packaging.python.org/tutorials/packaging-projects/

https://packaging.python.org/guides/distributing-packages-using-setuptools/
