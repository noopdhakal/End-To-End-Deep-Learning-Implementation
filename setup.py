from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "xray-ai"
VERSION = "0.0.1"
DESCRIPTION = "End-to-end X-ray analysis and ML pipeline"
AUTHOR_NAME = "Anup Dhakal"
AUTHOR_EMAIL = "anup@example.com"  # change if needed

REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements(REQUIREMENTS_FILE_NAME),
)
