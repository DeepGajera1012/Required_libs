from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    long_description = f.read()

VERSION = '1.0'
DESCRIPTION = 'Important Packages for Machine Learning. \n Installed in a \'One Click\' '

# Setting up
setup(
    name="CE_AI_D001",
    version=1.0,
    author="DeepGajera1012",
    author_email="deepgajera20@gnu.ac.in",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 
                      'scikit-learn', 'statsmodels', 'pyforest', 'pycaret', 'Flask', 'fastapi',
                      'jupyter', 'xgboost', 'imbalanced-learn', 'bokeh', 'kat',
                      'Boruta', 'spyder', 'mlxtend', 'lightgbm', 'catboost',
                      'tensorflow-cpu==2.6.0', 'tensorflow-gpu==2.6.0'],
    keywords=['CE_AI_D001', 'Machine Learning in a single file', 'AI', 'ML', 'Machine Learning'],
    url='http://github.com/DeepGajera1012',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)