#!/usr/bin/env python3

import setuptools
import gradelab50

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gradelab50",
    version=gradelab50.__version__,
    author="Abrantes Araújo Silva Filho",
    author_email="abrantesasf@pm.me",
    description=gradelab50.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/computacaoraiz/gradelab50",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Jinja2>=2.10.1',
    ],
    entry_points={
        'console_scripts':
            ['gradelab50 = gradelab50.main:main'],
    },
    package_data={'gradelab50': ['templates/*.jinja2']},
)
