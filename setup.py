import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='pwntools-dbg-r2',  
    version='0.1.5',
    scripts=['pwntools-gdb', 'r2-session'] ,
    author="Enigmatrix",
    author_email="enigmatrix2000@gmail.com",
    description="Package to enable debugging with Radare2 in pwntools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Enigmatrix/pwntools-dbg-r2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
