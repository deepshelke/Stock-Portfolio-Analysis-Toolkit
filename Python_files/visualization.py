import matplotlib.pyplot as plt

def plot_stock_trend(data, ticker):
    """
    Plot the historical stock price trend.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label=ticker)
        plt.title(f"{ticker} Stock Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()
    except KeyError:
        raise ValueError("Input data must contain a 'Close' column.")

def plot_portfolio_allocation(weights, tickers):
    """
    Plot a pie chart of portfolio allocation.
    """
    try:
        plt.figure(figsize=(8, 8))
        plt.pie(weights, labels=tickers, autopct='%1.1f%%', startangle=140)
        plt.title("Portfolio Allocation")
        plt.show()
    except Exception as e:
        raise ValueError(f"Error plotting portfolio allocation: {e}")
