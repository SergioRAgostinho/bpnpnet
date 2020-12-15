from setuptools import setup, find_packages


def long_description():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="bpnpnet",
    version="0.1.0",
    license="MIT",
    description="Solving the Blind Perspective-n-Point Problem End-To-End With Robust Differentiable Geometric Optimization.",
    long_description_content_type="text/markdown",
    install_requires=["torch", "numpy", "opencv-python", "scipy"],
    author="Dylan Campbell",
    url="https://github.com/SergioRAgostinho/bpnpnet",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)
