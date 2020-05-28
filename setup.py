import sys
from setuptools import setup, find_packages

with open('README.md') as f:
    long_desc = f.read()

if sys.version_info < (3, 6):
    print('EnsArg requires at least Python 3.6 to run reliably.')

install_requires = [
    'matplotlib',
    'sklearn'
    
]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Basicenssembleargumentation',
    version='0.0.1',
    description='A basic argumentation process where the outcomes from different models can argue for generating a final output.',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Istiak Ahmed',
    author_email='istiak.uiu.bd@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keyword='ensemble learning, argumentation',
     project_urls={
        "Code": "https://github.com/Istiak1992/BasicEnsembleArgumentation/",
    },
    packages=find_packages(),
    python_requires=">=3.6"
   
        

)
