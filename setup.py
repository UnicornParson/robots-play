from setuptools import setup, find_packages

setup(
    name="robots_play",
    version="0.0.1",
    description="logs parsing utils",
    url="https://github.com/UnicornParson/robots-play",
    author="Dieter",
    packages=find_packages(),
    install_requires=["tqdm"],  # Specify any required packages as a list
)