from glob import glob
from setuptools import setup, find_packages


setup(
    name="immo_scraper",
    version="1.2.1",
    # about
    license="MIT",
    url="https://github.com/codeformuenster/immo-scout",
    # source
    packages=find_packages(),
    scripts=glob("bin/*"),
    # dependencies
    install_requires=[
        "beautifulsoup4~=4.7.1",
        "boto3",
        "kafka-python~=1.4.6",
        "requests~=2.22.0",
        "scrapy~=1.6.0",
        "toolz~=0.9.0",
    ],
    extras_require={
        "dev": ["black", "jupyter", "m2r", "pylama", "rope", "Sphinx", "sphinx_rtd_theme"],
    },
)
