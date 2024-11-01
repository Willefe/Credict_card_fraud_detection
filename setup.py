from setuptools import find_packages, setup
from typing import List

hypen_e = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This functions returns a list of requirement
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements


print(get_requirements('requirements.txt'))

setup(
    name="creditcard",
    version="0.0.1",
    author="efosa",
    author_email="efosa_wil@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))
