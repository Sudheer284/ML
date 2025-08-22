from setuptools import setup,find_packages

with open("Requirements.txt") as f:
    Requirements = f.read().splitlines()

setup (
    name="NutriPlan-AI",
    version="0.1",
    author="Sudheer",
    packages=find_packages(),
    install_requires = Requirements,
)