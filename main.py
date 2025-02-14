import yfinance as yf
import pandas as pd

# Define the stock symbol (e.g., AAPL for Apple)
stock_symbol = "AAPL"

# Fetch historical data
stock_data = yf.download(stock_symbol, start="2020-01-01", end="2024-01-01")

# Display the first 5 rows
print(stock_data.head())

# Save the data to a CSV file
stock_data.to_csv("stock_data.csv")
