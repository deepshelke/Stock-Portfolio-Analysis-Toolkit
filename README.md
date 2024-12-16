# Stock-Portfolio-Analysis-Toolkit

A Python package to analyze stock portfolio performance, calculate risk metrics, and visualize stock trends. This toolkit integrates stock data fetching, performance evaluation, risk analysis, and data visualization.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The **Stock Portfolio Analysis Toolkit** is designed to help users analyze and visualize their stock portfolio, calculate key risk metrics like volatility and Sharpe ratio, and plot stock trends over time. This toolkit uses **yfinance** to fetch stock data and includes features for performance evaluation and risk analysis.

## Features
- **Fetch Stock Data**: Fetches historical stock data for multiple tickers using Yahoo Finance.
- **Risk Analysis**: Calculates volatility and Sharpe ratio of a portfolio.
- **Performance Evaluation**: Calculates daily returns and portfolio returns.
- **Data Visualization**: Plots stock trends and portfolio allocation.
- **Error Handling**: Gracefully handles common user errors.

# Installation Guide for the Stock Portfolio Analysis Toolkit

# Download Zip file or Clone the project directly

**Step 1**:
1. Clone the repository from GitHub using the following command:
   ```bash
   git clone https://github.com/username/stock-portfolio-analysis-toolkit.git

**Step 2** Navigate to the project directory:
cd stock-portfolio-analysis-toolkit

**Step 3** Set Up the Environment

I ) Run the following command to create a virtual environment: python3 -m venv .venv

II) Activate the virtual environment:

On macOS/Linux: source .venv/bin/activate

On Windows: .venv\Scripts\activate

**Step 4** Install Dependencies

Install all necessary dependencies from the requirements.txt file:

pip3 install -r requirements.txt

**Step 5**: Additional Package Installation
If any packages are missing (like yfinance), ensure they are installed using the following command:

pip3 install yfinance

**Step 6** Run the Project
To run the project, execute the main.py file:
   ```bash
python3 main.py
