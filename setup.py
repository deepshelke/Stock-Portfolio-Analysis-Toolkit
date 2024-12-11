from setuptools import setup, find_packages

setup(
    name="stock_portfolio_toolkit",
    version="0.1.0",
    description="A toolkit for analyzing stock portfolios",
    author="Your Team",
    packages=find_packages(),
    install_requires=["yfinance", "pandas", "numpy", "matplotlib"],
)