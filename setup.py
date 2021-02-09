from distutils.command import build

from setuptools import setup
from setuptools.command import develop

setup(
    name='functions-ext-profile',
    version='1.0.0',
    description='Azure Functions Extension Profile',
    author="Roger Zeng",
    author_email="hazeng@microsoft.com",
    keywords="azure azurefunctions python",
    url="https://github.com/Hazhzeng/functions-ext-profile",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: Web Environment',
    ],
    license='MIT',
    packages=['functions_ext_profile'],
    install_requires=[
        'azure-functions',
        'psutil==5.8.0'
    ],
    extras_require={},
    include_package_data=True
)
