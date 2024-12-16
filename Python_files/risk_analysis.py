import numpy as np

#Calculate volatility (standard deviation) of daily returns. 
def calculate_volatility(daily_returns):
    try:
        if daily_returns.empty:
            raise ValueError("Daily returns data is empty.")
        volatility = daily_returns.std() #  This method calculates the standard deviation of the data in daily_returns
        return volatility
    except Exception as e:
        raise RuntimeError(f"Error in calculating volatility: {e}")

# Calculate Sharpe ratio of daily returns 
def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01):
    try:
        if daily_returns.empty:
            raise ValueError("Daily returns data is empty.")
        excess_returns = daily_returns.mean() - risk_free_rate / 252 # The risk-free rate (annualized) is divided by 252 to get the daily risk-free rate, assuming 252 trading days in a year.
        sharpe_ratio = excess_returns / daily_returns.std() #Divides the excess returns by the volatility to calculate the Sharpe Ratio.
        return sharpe_ratio
    except Exception as e:
        raise RuntimeError(f"Error in calculating Sharpe ratio: {e}")