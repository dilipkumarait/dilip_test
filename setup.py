from setuptools import setup, find_packages

setup(
    name = "dilip_test",
    version="0.1",
    description= "added this to just for testing",
    url= "hwfio",
    packages=find_packages(),
    install_requires = ["pandas", "pytest"]
)