from setuptools import setup

setup(
    name='isp_client',
    version='0.1',
    py_modules=['isp_client'],
    install_requires=['requests>=2.18.4'],
    entry_points = {
        'console_scripts': ['isp_client=isp_client:main'],
    }
)
