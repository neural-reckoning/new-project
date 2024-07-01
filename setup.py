from setuptools import setup, find_packages

setup(
    name='newproject',
    version='0.1',
    description='A Python package for newproject',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/neural-reckoning/new-project',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        # Add any dependencies required by your package here
    ],
)