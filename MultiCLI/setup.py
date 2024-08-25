from setuptools import setup, find_packages

setup(
    name='multicli',
    version='1.0',
    py_modules=['multicli'],
    packages=find_packages(include=['tools']),
    install_requires=[
        'argparse',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'multicli=multicli:main',
        ],
    },
)