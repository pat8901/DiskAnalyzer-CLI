from setuptools import setup

setup(
    name="space",
    version="0.1.0",
    py_modules=[
        "space",
        "src/bar",
        "bar/histogram",
        "bar/pie",
        "bar/tools",
        "bar/writer",
    ],
    install_requires=["Click", "matplotlib", "numpy", "pandas", "Pillow", "pypdf"],
    entry_points={
        "console_scripts": [
            "space = space:main",
        ],
    },
)
