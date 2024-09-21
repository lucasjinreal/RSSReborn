import os
from setuptools import setup, find_packages


_PATH_ROOT = os.path.dirname(__file__)

with open(os.path.join(_PATH_ROOT, "README.md"), encoding="utf-8") as fo:
    readme = fo.read()

setup(
    name="rssreborn",
    version="0.1.0",
    description="Make RSS great again!",
    author="Open Jarvis AI",
    url="https://github.com/lucasjinreal/RSSReborn",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "rssreborn=rsshub.rssreborn:main",
        ],
    },
    install_requires=[
        "openai",
        "Flask>=2.0.2",
        "Flask-Analytics>=0.6.0",
        "Flask-Caching>=2.0.2",
        "Flask-DebugToolbar>=0.11.0",
        "Flask-Moment>=1.0.2",
        "Flask-Script>=2.0.6",
        "gunicorn>=20.1.0",
        "icecream>=2.1.1",
        "arrow"
    ],
    long_description=readme,
    long_description_content_type="text/markdown",
)
