from setuptools import setup, find_packages

setup(
    name='common',
    version='0.0.1',
    description='common packages',
    author='daesoo',
    author_email='',
    license='MIT',
    package_dir={"": "common"},
    package=find_packages(),
    zip_safe=False,
    install_requires=[
    ]
)
