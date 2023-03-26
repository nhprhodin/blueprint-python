# blueprint-python
A template repository for Python projects. Includes a template class ( Blueprint), a class call (run.py), unit tests, 
and a setup.py enabling installation as a Python package.

## Preliminaries
- Tested on Linux-MANJARO

- Uses Python 3.10 (version >=3.7 to enable type annotation)

- Compatible with tox for code quality checks and unit testing

        pip install --upgrade pip
        pip install tox

## Usage as Template
1) Rename instances of "blueprint" in package, class calls, tests and setup files.

2) Make any necessary adjustments to the setup.py. Consider license.

3) Install dependencies
   
        pip install --upgrade pip
        pip install -r requirements*.txt

4) Install package as editable 
        
        pip install -e .

## Run
Run package on input:

    usage: run.py [-h] -c CONFIG [-l LOG_LEVEL]
    
    Parses input.
    
    required arguments:
      -c CONFIG, --config CONFIG            Path to config file.
    
    optional arguments:
      -h, --help                            show this help message and exit
      -l LOG_LEVEL, --loglevel LOG_LEVEL    Set log level. ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

Run tox:

    tox

## Best Practices

- Set up a virtual environment

        virtualenv -p python3.10 venv

## Resources
For information on python packages, see PyPA docs:

https://packaging.python.org/tutorials/packaging-projects/

https://packaging.python.org/guides/distributing-packages-using-setuptools/
