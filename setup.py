import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyquoter",
    version="1.0.0",
    author="Joshua Petitma",
    author_email="joshua@joshpetit.dev",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshpetit/pyquoter",
    packages=setuptools.find_packages(),
    entry_points= {
        'console_scripts': [
            'pyquoter=scripts.pyquoter:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)

