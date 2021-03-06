from setuptools import setup

setup(
    name="unifihome",
    version="0.1.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "black==22.1.0",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "click==8.0.4",
        "commonmark==0.9.1",
        "idna==3.3",
        "mypy-extensions==0.4.3",
        "pathspec==0.9.0",
        "platformdirs==2.5.1",
        "Pygments==2.11.2",
        "pyunifi==2.21",
        "requests==2.27.1",
        "rich==12.0.0",
        "textual==0.1.17",
        "textual-inputs==0.2.5",
        "tomli==2.0.1",
        "typing-extensions==4.1.1",
        "urllib3==1.26.9",
    ],
    packages=[
        "unifihome",
        "unifihome.ui",
    ],
)
