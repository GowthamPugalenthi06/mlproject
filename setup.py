from setuptools import find_packages,setup
from typing import List
E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of strings where each string is a requirement
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
        return requirements 
        
setup(
    name='mlproject',
    version='0.0.1',
    author='Gowtham',
    author_email='gowthamp990@gmail.com',
    packages=find_packages(),
    install_requires=[get_requirements('requirements.txt')],
    )