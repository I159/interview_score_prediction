from setuptools import setup, find_packages

setup(
    name='isp',
    version='0.1',
    packages=find_packages(),
    install_requires=['bottle>=0.12.13'],
    entry_points = {
        'console_scripts': ['isp=web_api.web_api:main'],
    }
)
