from setuptools import setup, find_packages
import os

conf_files = []
for p in os.listdir("conf"):
    conf_files.append(os.path.join("conf", p))

setup(
    name='pydemo',
    version='0.1',
    packages=find_packages(),
    description='This is py pkg test',
    author='anonymous',
    author_email='None',
    url='None',
    entry_points={
        'console_scripts': [
            'pydemo=mypkg.main:main',
        ],
    },
    data_files=[
        ('mypkg', conf_files),
    ],
)
