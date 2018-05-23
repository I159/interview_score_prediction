from setuptools import setup

setup(
    name='intervirview_score_prediction',
    version='0.1',
    py_modules=['main'],
    install_requires=['bottle>=0.12.13'],
    entry_points = {
        'console_scripts': ['isp=main:main'],
    }
)
