from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()


setup(
    name="simplidb",
    version="0.2.4",
    author="Mauly dotDev",
    author_email="mauly.dev@email.com",
    description="A simple SQLite database wrapper (A package that provides a simplified interface for working with SQLite databases.)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/maulydev/SimpliDB",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
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
    keywords=["SQLite", "database", "wrapper", "simple", "db"],
    install_requires=[
        # Add any required dependencies here
    ],
    python_requires=">=3.0",
)
