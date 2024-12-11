import numpy as np

def calculate_volatility(daily_returns):
    """
    Calculate the standard deviation of daily returns (volatility).
    """
    return daily_returns.std()

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01):
    """
    Calculate the Sharpe Ratio given daily returns and a risk-free rate.
    """
    excess_returns = daily_returns - risk_free_rate / 252
    return np.mean(excess_returns) / np.std(excess_returns)
