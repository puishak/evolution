from setuptools import setup, find_packages

setup(
    name="evolution",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        ],  # Add dependencies if needed
    author="Shakib Absar",
    description="Package for creating and running evolutionary algorithms",
    url="https://github.com/puishak/evolution",
)

