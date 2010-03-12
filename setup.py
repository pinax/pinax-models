from setuptools import setup, find_packages
 
setup(
    name='logicaldelete',
    version = '1.0',
    author='Patrick Altman',
    author_email='paltman@gmail.com',
    url='http://github.com/paltman/django-logicaldelete',
    description="""django-logicaldelete is a base model that provides some extras for your models.""",
    packages=find_packages(),
    namespace_packages = [],
    include_package_data = True,
    zip_safe=False,
    license='',
    install_requires=[
        'django',
        ]
)
