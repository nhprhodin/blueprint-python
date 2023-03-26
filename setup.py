from setuptools import find_packages, setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="blueprint",
    version="0.0.1",
    description="A Python-project blueprint.",
    long_description=readme,
    url="https://github.com/nhprhodin/blueprint-python",
    author="Henrik P. Rhodin",
    author_email="nhp.rhodin@gmail.com",
    license="MIT",
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    data_files=["requirements.txt"],
    zip_safe=False,
)
