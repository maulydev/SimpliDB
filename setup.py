from setuptools import setup, find_packages

setup(
    name="simplidb",
    version="0.2.1-alpha",
    author="Mauly dotDev",
    author_email="mauly.dev@email.com",
    description="A simple SQLite database wrapper",
    long_description="A Python package that provides a simplified interface for working with SQLite databases.",
    url="https://github.com/maulydev/SimpliDB",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/maulydev/SimpliDB/issues",
        "Source Code": "https://github.com/maulydev/SimpliDB",
    },
    keywords=["SQLite", "database", "wrapper"],
    install_requires=[
        # Add any required dependencies here
    ],
    python_requires=">=3.0",
)
