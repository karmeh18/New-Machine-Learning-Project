from setuptools import setup, find_packages
from pathlib import Path
from typing import List


def get_requirements(filename: Path)-> List[str]:
    with open("requirements.txt") as file:
        files=file.readlines()
        files=[files.replace("/n","") for files in files]

        if "-e ." in files:
            files.remove("-e .")
        return files

setup(name="ML_Project",
      version="1.0",
      description="Machine Learning Project",
      author="Karan Mehta",
      author_email='kemhta883@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt"))