import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danmaku2ass",
    version="1.0.0",

    # guessed from commit author
    author="Star Brilliant",
    author_email="coder@poorlab.com",

    description="Converter for Danmaku format to ASS subtitles",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/m13253/danmaku2ass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
