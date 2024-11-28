from distutils.core import setup
from setuptools import find_packages
from setuptools.command.install import install
import os

setup(
    name='graspnetAPI',
    version='1.2.11',
    description='graspnet API',
    author='Hao-Shu Fang, Chenxi Wang, Minghao Gou',
    author_email='gouminghao@gmail.com',
    url='https://graspnet.net',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.3',
        'scipy',
        'transforms3d==0.3.1',
        'open3d==0.13.0',
        'trimesh',
        'tqdm',
        'Pillow',
        'opencv-python',
        'pillow==10.1.0',
        'matplotlib',
        'pywavefront',
        'trimesh==4.0.5',
        'scikit-image',
        'autolab_core',
        'autolab-perception',
        'cvxopt',
        'dill',
        'h5py',
        'scikit-learn',
        'grasp_nms'
    ]
)
