from setuptools import setup, find_packages

setup(
    name="stock_prediction_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pandas",
        "yfinance",
        "prophet",
        "pytest"
    ],
)