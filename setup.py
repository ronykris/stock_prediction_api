from setuptools import setup, find_packages

setup(
    name="stock_prediction_api",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "fastapi",
        "pydantic",
        "pandas",
        "yfinance",
        "prophet",
    ],
)