from setuptools import setup, find_packages

setup(
    name = "StreamDecompressor",
    version = "2.0",
    author = "Cecile Tonglet",
    author_email = "cecile.tonglet@gmail.com",
    description = ("A simple module to decompress streams compressed multiple "
                   "times"),
    license = "GPLv2",
    keywords = "postgres database dump restore",
    url = "https://github.com/cecton/StreamDecompressor",
    packages = find_packages(),
    install_requires = ['StreamDecompressor'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Archiving :: Compression",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)