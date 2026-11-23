# pylint: disable=missing-module-docstring
from setuptools import setup, find_packages

long_description = """A library for image augmentation in machine learning experiments, particularly convolutional
neural networks. Supports the augmentation of images, keypoints/landmarks, bounding boxes, heatmaps and segmentation
maps in a variety of different ways."""

INSTALL_REQUIRES = [
    "six",
    "numpy>=1.21",
    "numpy>=2.3 ; python_version >= '3.14'",
    "scipy",
    "Pillow",
    "matplotlib",
    "scikit-image>=0.18",
    "opencv-python<4.13",
    "imageio",
    "Shapely",
    "imagecorruptions-imaug>=1.1.5"
]

DEV_REQUIRES = [
    "pytest-subtests",
    "xdoctest >= 0.7.2",
    "coverage",
    "pytest-cov",
    "flake8",
]

setup(
    name="imaug",
    version="0.4.4.dev0",
    author="imaug",
    author_email="ej_foss@mailbox.org",
    url="https://github.com/imaug/imaug",
    python_requires='>3.6,<3.15',
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'dev': DEV_REQUIRES,
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["LICENSE", "README.md", "requirements.txt"],
        "imgaug": ["DejaVuSans.ttf", "quokka.jpg", "quokka_annotations.json", "quokka_depth_map_halfres.png"],
        "imgaug.checks": ["README.md"]
    },
    license="MIT",
    description="Image augmentation library for deep neural networks",
    long_description=long_description,
    keywords=["augmentation", "image", "deep learning", "neural network", "CNN", "machine learning",
              "computer vision", "overfitting"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
