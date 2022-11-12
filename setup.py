import os
from setuptools import setup, find_packages

project_name = 'dearpyapp'
description = 'Wrapper for DearPyGui'
url = 'https://github.com/means0nothing/DearPyApp'


def readme():
    with open('README.md') as file:
        return file.read()


def version():
    result = ''
    with open(os.path.join(project_name, '__init__.py')) as file:
        for line in file.readlines():
            if line.startswith('__version__'):
                result = line[line.find('\'') + 1:line.rfind('\'')]
                break
    if not result:
        raise ValueError("Unable to determine version.")
    return result


def requirements():
    with open('requirements.txt') as file:
        return [str.strip(line) for line in file.readlines()]


setup(
    name=project_name,
    version=version(),
    description=description,
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Pavel Shevcov',
    author_email='means0nothing@gmail.com',
    url=url,
    keywords=[],
    python_requires=">=3.9",
    classifiers=[
        'Development Status :: 3 - Alpha',  # '3 - Alpha', '4 - Beta', '5 - Production/Stable'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    ext_modules=[],
    setup_requires=['wheel'],
    install_requires=requirements(),
    extras_require={},
)
