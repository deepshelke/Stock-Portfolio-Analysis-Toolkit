# Python_files/risk_analysis.py

import numpy as np

def calculate_volatility(daily_returns):
    """
    Calculate volatility (standard deviation) of daily returns.
    """
    try:
        if daily_returns.empty:
            raise ValueError("Daily returns data is empty.")
        volatility = daily_returns.std()
        return volatility
    except Exception as e:
        raise RuntimeError(f"Error in calculating volatility: {e}")

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01):
    """
    Calculate Sharpe ratio of daily returns.
    """
    try:
        if daily_returns.empty:
            raise ValueError("Daily returns data is empty.")
        excess_returns = daily_returns.mean() - risk_free_rate / 252
        sharpe_ratio = excess_returns / daily_returns.std()
        return sharpe_ratio
    except Exception as e:
        raise RuntimeError(f"Error in calculating Sharpe ratio: {e}")
