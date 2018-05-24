from setuptools import setup, find_packages

setup(
    name='isp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'bottle>=0.12.13',
        'pandas>=0.23.0',
        'scikit-learn>=0.19.1',
        'scipy>=1.1.0',
        'nltk>=3.3'],
    entry_points={
        'console_scripts': ['isp=web_api.web_api:main'],
    },
    include_package_data=True,
)
