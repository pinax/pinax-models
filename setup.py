from setuptools import setup

VERSION = __import__("logicaldelete").__version__

 
setup(
    name = "django-logicaldelete",
    version = VERSION,
    author = "Patrick Altman",
    author_email = "paltman@gmail.com",
    url = "http://github.com/paltman/django-logicaldelete",
    description = "a base model that provides built in logical delete functionality",
    long_description = open("README.rst").read(),
    packages = [
        "logicaldelete"
    ],
    license="BSD",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
