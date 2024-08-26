from setuptools import setup, find_packages

setup(
    name='multicli',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil',
        'requests',
        'schedule',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'multicli=multicli.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
