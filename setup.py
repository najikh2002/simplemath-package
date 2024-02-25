from setuptools import setup, find_packages

NAME = "simplemath"
VERSION = "0.1.0"
AUTHOR = "Hizbullah Najihan"
DESCRIPTION = "Bikin package sederhana :)"

DEPEDENCIES = [
    "wheel",
]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    requires=DEPEDENCIES,
    entry_points={
        "console_scripts": [
            "mycommand = simplemath.module:main",
        ]
    },
)

