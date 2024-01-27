from setuptools import setup, find_packages

setup(
    name = "dilip_test",
    version="0.1",
    description= "added this to just for testing",
    url= "https://github.com/dilipkumarait/dilip_test.git",
    packages=find_packages(),
    install_requires = ["pandas", "pytest"]
)
