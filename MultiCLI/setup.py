from setuptools import setup, find_packages

setup(
    name='multicli',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'python-dotenv',
        'requests',
        'psutil',
        'schedule'
    ],
    entry_points={
        'console_scripts': [
            'multicli=multicli:main',
        ],
    },
)
