from glob import glob
from setuptools import setup, find_packages

setup(
    name="immo_scraper",
    version="0.4.0",
    # about
    license="MIT",
    url="https://github.com/codeformuenster/immo-scout",
    # source
    packages=find_packages(),
    scripts=glob("bin/*"),
    # dependencies
    install_requires=[
        "beautifulsoup4",
        "boto3",
        "docutils~=0.15.2",
        "requests",
        "scrapy",
        "toolz",
    ],
    extras_require={
        "dev": [
            "black",
            "jupyter",
            "m2r",
            "pylama",
            "rope",
            "Sphinx",
            "sphinx_rtd_theme",
        ],
    },
)
