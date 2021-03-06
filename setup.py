#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'nibabel',
    'numpy',
    'pynrrd',
    'SimpleITK',
    'torch>=1.2',  # for IterableDataset
    'torchvision',
    'tqdm',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Fernando Perez-Garcia",
    author_email='fernando.perezgarcia.17@ucl.ac.uk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description=(
        "Tools for loading, augmenting and writing 3D medical images"
        " on PyTorch."
    ),
    entry_points={
        'console_scripts': [
            'torchio=torchio.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='torchio',
    name='torchio',
    packages=find_packages(include=['torchio', 'torchio.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fepegar/torchio',
    version='0.7.3',
    zip_safe=False,
)
