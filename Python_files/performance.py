# Python_files/performance.py

import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(tickers):
    """
    Fetch stock data for the given tickers using yfinance.
    """
    try:
        data = yf.download(tickers, start="2020-01-01", end="2023-01-01")
        if data.empty:
            raise ValueError("No data returned for the given tickers.")
        return data['Adj Close']
    except Exception as e:
        raise RuntimeError(f"Failed to fetch stock data: {e}")

def calculate_daily_returns(stock_data):
    """
    Calculate daily returns for the given stock data.
    """
    try:
        if stock_data.empty:
            raise ValueError("Stock data is empty.")
        daily_returns = stock_data.pct_change().dropna()
        return daily_returns
    except Exception as e:
        raise RuntimeError(f"Error in calculating daily returns: {e}")

def calculate_portfolio_returns(daily_returns, weights=None):
    """
    Calculate portfolio returns given daily returns and weights.
    """
    try:
        if daily_returns.empty:
            raise ValueError("Daily returns data is empty.")
        num_stocks = daily_returns.shape[1]
        if weights is None:
            weights = np.ones(num_stocks) / num_stocks
        if len(weights) != num_stocks:
            raise ValueError("Weights length must match the number of stocks.")
        portfolio_returns = daily_returns.dot(weights)
        return portfolio_returns
    except Exception as e:
        raise RuntimeError(f"Error in calculating portfolio returns: {e}")
