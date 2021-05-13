import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notion-sdk-py",
    packages=["notion"],
    version="0.0.1",
    license="MIT",
    description="A simple and easy to use client for the Notion API for python",
    author="blue-hope",
    author_email="ms7045436@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blue-hope/notion-sdk-py",
    keywords=[
        "notion",
        "notion-client",
        "notion-api",
        "notion-lib",
    ],
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)