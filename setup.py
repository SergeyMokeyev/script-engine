from setuptools import find_packages, setup
from pkg_resources import parse_requirements


with open('requirements.txt') as f:
    install_requires = [str(requirement) for requirement in parse_requirements(f)]


with open('README.md') as f:
    long_description = f.read()


setup(
    name='script-engine',
    version='0.0.1',
    author='Sergey Mokeyev',
    author_email='sergey.mokeyev@gmail.com',
    description='Script engine',
    long_description=long_description,
    url='https://github.com/SergeyMokeyev/script-engine',
    install_requires=install_requires,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    data_files=[
        ('requirements.txt', ['requirements.txt']),
        ('README.md', ['README.md'])
    ]
)
