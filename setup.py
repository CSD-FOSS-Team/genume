import setuptools
import tarfile
import os


# Create tar file with required files
def package_artifacts():
    with tarfile.open("package.tar", "w") as package:
        package.add("scripts")
        package.add("bash_helpers")


package_artifacts()
os.rename("package.tar", "genume/package.tar")
setuptools.setup(
    name="genume",
    version="0.1.1",
    author="CSD FOSS Team",
    description="A graphical enumeration tool",
    url="https://github.com/CSD-FOSS-Team/genume",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'genume = genume.console:console_entry'
        ]
    },
    classfilters=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX",
    ],
)
os.remove("genume/package.tar")