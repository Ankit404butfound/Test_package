from distutils.core import setup
import setuptools


def readme() -> str:
    with open(r'README.md') as f:
        README = f.read()
    return README


setup(
    name='remote_kit',
    packages=setuptools.find_packages(),
    version='1.0',
    license='MIT',
    description='Remote Kit is a Python library',
    author='Ankit Raj Mahapatra',
    author_email='ankitrajjitendra816@gmail.com',
    url='https://github.com/Ankit404butfound/Test_package',
    download_url='',
    keywords=['hello'],
    install_requires=[
        'Flask',

    ],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
