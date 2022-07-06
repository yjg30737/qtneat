from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='qtneat',
    version='0.0.4',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Set the Qt frameless titlebar/theme easily',
    url='https://github.com/yjg30737/qtneat.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'qtawesome>=0.0.1',
        'pyqt-svg-button>=0.0.1',
        'pyqt-svg-icon-text-widget>=0.0.1'
    ]
)