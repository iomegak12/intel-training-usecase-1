from importlib.util import find_spec
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(name="orderprocessinglibrary",
                 version="0.0.1",
                 author="Ramkumar JD",
                 author_email="jd.ramkumar@gmail.com",
                 description="Professional and Standard Python Library",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/iomegak12/intel-training-usecase-1",
                 packages=setuptools.find_packages(),
                 python_requires='>=3.6',
                 install_requires=[],
                 )
