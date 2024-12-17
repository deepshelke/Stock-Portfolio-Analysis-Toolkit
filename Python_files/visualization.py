import matplotlib.pyplot as plt

# Plot stock price trends.
def plot_stock_trend(stock_data):
    try:
        if stock_data.empty:
            raise ValueError("Stock data is empty.")
        stock_data.plot(figsize=(10, 6), title="Stock Price Trends")
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close Price ($)")
        plt.show()
    except Exception as e:
        raise RuntimeError(f"Error in plotting stock trends: {e}")
    
# Plot cumulative portfolio returns.
def plot_portfolio_allocation(portfolio_returns):
    try:
        if portfolio_returns.empty:
            raise ValueError("Portfolio returns data is empty.")
        portfolio_cumulative = (1 + portfolio_returns).cumprod() #Calculates the cumulative product of these values over time, simulating how the portfolio grows.
        portfolio_cumulative.plot(figsize=(10, 6), title="Cumulative Portfolio Returns")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value")
        plt.show()
    except Exception as e:
        raise RuntimeError(f"Error in plotting portfolio allocation: {e}")
