from setuptools import setup, find_packages

setup(
    name='igautofollow',
    version='0.1.0',
    description='A script to automate Instagram tasks such as following people who followed a particular page, following everyone who liked a particular post, and unfollowing everyone',
    author='@erikonasz',
    author_email='erikuzas123@gmail.com',
    packages=find_packages(),
    install_requires=['selenium', 'webdriver-manager', 'random', 'time'],
    entry_points={
        'console_scripts': [
            'igautofollow=igautofollow.main:main',
        ],
    },
)