from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    Return list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name= "mlpipeline",
    version= "0.0.1",
    author= "Suyog",
    author_email= "suyog.parab92@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)