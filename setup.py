from setuptools import setup, find_packages

setup(
    name='shippable',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'coverage'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
)