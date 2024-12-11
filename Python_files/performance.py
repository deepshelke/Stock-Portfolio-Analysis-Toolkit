import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        return data
    except Exception as e:
        raise ValueError(f"Error fetching data for {ticker}: {e}")

def calculate_daily_returns(data):
    """
    Calculate daily percentage returns from stock price data.
    """
    try:
        daily_returns = data['Close'].pct_change().dropna()
        return daily_returns
    except KeyError:
        raise ValueError("Input data must contain a 'Close' column.")

def calculate_portfolio_returns(stock_data, weights):
    """
    Calculate the total returns of a portfolio with given stock data and weights.
    """
    try:
        returns = [calculate_daily_returns(data) for data in stock_data]
        portfolio_returns = pd.concat(returns, axis=1).dot(weights)
        return portfolio_returns
    except Exception as e:
        raise ValueError(f"Error calculating portfolio returns: {e}")
