from setuptools import find_packages,setup


setup(
    name = 'sensor',
    version = '0.0.1',
    author = 'Uday',
    author_email='udaysd01@gmail.com',
    packages=find_packages(),
    install_required=get_requirements(),
)

