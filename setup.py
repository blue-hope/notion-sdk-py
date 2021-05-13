import setuptools

setuptools.setup(
    name="notion-sdk-py",
    packages=["notion"],
    version="1.0.0",
    license="MIT",
    description="A simple and easy to use client for the Notion API for python",
    author="blue-hope",
    author_email="ms7045436@gmail.com",
    long_description=open("README.md").read(),
    url="https://github.com/blue-hope/notion-sdk-py",
    keywords=[
        "notion",
        "notion-client",
        "notion-api",
        "notion-lib",
    ],
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