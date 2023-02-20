# blueprint-python
A template repository for Python projects. Includes a template class ( Blueprint), a class call (run.py), unit tests, 
and a setup.py enabling installation as a Python package.

## Preliminaries
- Tested on Ubuntu 18.04, bionic

- Uses Python version >=3.7 to enable type annotation

- Compatible with tox for code quality checks and running unit tests

        sudo apt update
        sudo apt install tox

## Usage as Template
1) Rename instances of "blueprint" in package, class calls, tests and setup files.

2) Make any necessary adjustments to the setup.py. Consider license.

3) Ensure the python version of the basepython arguments in tox.ini match the python_requires argument in setup.py

3) Install dependencies
   
        pip install --upgrade pip
        pip install -r requirements*.txt

5) Install package as editable 
        
        pip install -e .

## Run

    usage: run.py [-h] -c CONFIG [-l LOG_LEVEL]
    
    Parses input.
    
    required arguments:
      -c CONFIG, --config CONFIG            Path to config file.
    
    optional arguments:
      -h, --help                            show this help message and exit
      -l LOG_LEVEL, --loglevel LOG_LEVEL    Set log level. ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

## Best Practices

- Set up a virtual environment

        virtualenv -p python3.7 venv

## Resources
For information on python packages, see PyPA docs:

https://packaging.python.org/tutorials/packaging-projects/

https://packaging.python.org/guides/distributing-packages-using-setuptools/
