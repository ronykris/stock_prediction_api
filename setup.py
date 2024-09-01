from setuptools import setup, find_packages

setup(
    name="stock_prediction_api",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests*"]),
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