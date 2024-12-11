# main.py

# main.py

from Python_files.performance import fetch_stock_data, calculate_daily_returns, calculate_portfolio_returns
from Python_files.visualization import plot_stock_trend, plot_portfolio_allocation
from Python_files.risk_analysis import calculate_volatility, calculate_sharpe_ratio


# Define stock tickers and portfolio weights
tickers = ["AAPL", "GOOGL", "MSFT"]
weights = [0.4, 0.3, 0.3]

# Define the date range for stock data
start_date = "2024-01-01"
end_date = "2024-02-01"

# Fetch stock data for each ticker
stock_data = [fetch_stock_data(ticker, start_date, end_date) for ticker in tickers]

# Calculate portfolio returns
portfolio_returns = calculate_portfolio_returns(stock_data, weights)

# Visualize stock trends and portfolio allocation
for ticker, data in zip(tickers, stock_data):
    plot_stock_trend(data, ticker)

plot_portfolio_allocation(weights, tickers)

# Calculate risk metrics for each stock and the portfolio
for ticker, data in zip(tickers, stock_data):
    daily_returns = calculate_daily_returns(data)
    volatility = calculate_volatility(daily_returns)
    sharpe_ratio = calculate_sharpe_ratio(daily_returns)
    print(f"{ticker} Volatility: {volatility:.4f}")
    print(f"{ticker} Sharpe Ratio: {sharpe_ratio:.4f}")

# Calculate portfolio risk
portfolio_volatility = calculate_volatility(portfolio_returns)
portfolio_sharpe_ratio = calculate_sharpe_ratio(portfolio_returns)
print(f"Portfolio Volatility: {portfolio_volatility:.4f}")
print(f"Portfolio Sharpe Ratio: {portfolio_sharpe_ratio:.4f}")
