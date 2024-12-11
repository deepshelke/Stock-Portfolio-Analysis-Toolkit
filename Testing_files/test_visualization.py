import pytest
from stock_portfolio_toolkit.visualization import plot_stock_trend

def test_plot_stock_trend():
    data = fetch_stock_data("AAPL", "2024-01-01", "2024-01-31")
    try:
        plot_stock_trend(data, "AAPL")
    except Exception:
        pytest.fail("Plotting failed.")
