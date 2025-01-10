from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''This function gets a path of requirements for project and return an list from used libraries'''
    packages = []
    try:
        with open(file_path,'r') as f:
            for library in f:
                if library.strip() == '-e .':
                    continue
                packages.append(library.strip())
            return packages
    except FileNotFoundError:
        print(f"File path {file_path} was not found!")
    except Exception as e:
        print(e)

setup(
    name = 'mlproject',
    version ='0.0.1',
    author= 'Jakub',
    email = 'kubajedrych100@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)