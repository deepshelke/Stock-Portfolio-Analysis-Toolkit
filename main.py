import yfinance as yf
from Python_files.performance import fetch_stock_data, calculate_daily_returns, calculate_portfolio_returns
from Python_files.visualization import plot_stock_trend, plot_portfolio_allocation
from Python_files.risk_analysis import calculate_volatility, calculate_sharpe_ratio

def get_user_input():
    """Prompt user for at least three stock tickers."""
    while True:
        user_input = input("Enter at least 3 stock tickers, separated by commas (e.g., AAPL, MSFT, TSLA): ")
        tickers = [ticker.strip().upper() for ticker in user_input.split(',')]
        
        if len(tickers) < 3:
            print("You must enter at least 3 stock tickers.")
        else:
            return tickers

def main():
    # Get stock tickers from the user
    tickers = get_user_input()

    # Fetch stock data for the selected tickers
    stock_data = fetch_stock_data(tickers)

    # Calculate daily returns and portfolio returns
    daily_returns = calculate_daily_returns(stock_data)
    portfolio_returns = calculate_portfolio_returns(daily_returns)

    # Calculate risk metrics
    volatility = calculate_volatility(daily_returns)
    sharpe_ratio = calculate_sharpe_ratio(daily_returns)

    # Visualization of stock trends and portfolio allocation
    plot_stock_trend(stock_data)
    plot_portfolio_allocation(portfolio_returns)

    # Output risk analysis
    print("\nRisk Analysis:")
    print(f"Volatility (Standard Deviation):\n{volatility}")
    print(f"Sharpe Ratio:\n{sharpe_ratio}")

if __name__ == "__main__":
    main()
