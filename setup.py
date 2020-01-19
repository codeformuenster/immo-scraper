from glob import glob
from setuptools import setup, find_packages


setup(
    name="pest_pi",
    version="1.1.1",
    author="Thorben Jensen",
    author_email="jensen.thorben@gmail.com",
    license="MIT",
    description=("Pest monitoring with Raspberry Pi."),
    keywords="raspberry pi tensorflow",
    url="https://github.com/thorbenJensen/pest-pi",
    packages=find_packages(),
    scripts=glob("bin/*"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
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