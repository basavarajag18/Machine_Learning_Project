from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME= "housing predictor"
VERSION= "0.0.2"
AUTHOR="Basava"
DESCRIPTION="This is a first FSDS Nov batch Mahine Learning Project"
PACKAGES= ["housing"]
REQUIREMENT_FILE_NAME= "requirements.txt"


def get_requirements_list()->List[str]:
    
    """
    Description: This function is going to return a list of requirements
    mention in the requirement.txt file

    return this function is going to return list which contain name
    of libraries mentioned in the requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version= VERSION,
Author= AUTHOR,
description= DESCRIPTION,
packages= find_packages(), #['housing']
install_requires= get_requirements_list()
)

