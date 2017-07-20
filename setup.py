from setuptools import setup, find_packages

setup(
    name='shippable',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'coverage',
        'gunicorn'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov'
        ],
    }
)