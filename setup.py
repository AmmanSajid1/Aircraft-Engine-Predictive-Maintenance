import setuptools

__version__ = "0.0.0"

REPO_NAME = "Aircraft-Engine-Predictive-Maintenance"
AUTHOR_USER_NAME = "AmmanSajid1"
SRC_REPO = "Aircraft Engine Predictive Maintenance"
AUTHOR_EMAIL = "ammansajid1@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)