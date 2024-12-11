import pytest
from stock_portfolio_toolkit.performance import fetch_stock_data

def test_fetch_stock_data():
    data = fetch_stock_data("AAPL", "2024-01-01", "2024-01-31")
    assert "Close" in data.columns
