from setuptools import setup, find_packages

setup(
    name='mon_calendrier',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Adrien Berard ',
    author_email='adrienberard@hotmail.fr',
    description='Une bibliothèque simple pour gérer un calendrier.',
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/Adrizen89/calendarAPI',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11.2',
        'License :: OSI Approved :: MIT License',
    ],
)
