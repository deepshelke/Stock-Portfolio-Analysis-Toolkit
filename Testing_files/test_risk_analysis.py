import pytest
from stock_portfolio_toolkit.risk_analysis import calculate_volatility

def test_calculate_volatility():
    daily_returns = [0.01, -0.01, 0.02, -0.02]
    assert calculate_volatility(daily_returns) > 0
