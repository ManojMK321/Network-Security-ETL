'''
The setup.py file is an essential part of packing and 
distributing the python project .It is used to package the project 
into a distribution file that can be installed and used by other 
people .It is also used to specify the dependencies,metadata,entry points of the project .
The setup.py file is written in python and uses the setuptools 
library to package the project .
'''

from setuptools import find_packages, setup # find_packages used to find the packages in the project and setup used to setup the project
from typing import List # Used to specify the type hints in the code

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .  It is used to install the project in editable mode this refers to the setup.py
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Manoj Kumar',
    email='manojkumarrmx7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)