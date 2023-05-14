from pprint import pprint
import csv
import yfinance as yf
import pandas as pd

# Specify the ticker symbol of the stock
ticker_symbol = "TSLA"
start_date = '2022-05-13'
end_date = '2023-05-13'

# Fetch historical price data from Yahoo Finance
# stock_data = yf.download(ticker_symbol, start_date, end_date)
stock_data = yf.download(ticker_symbol, period='1d')
df = pd.DataFrame(stock_data)
# basket_data = yf.download(['AAPL', 'MSFT', 'AMZN', 'META', 'GOOGL'], period='1d')['Adj Close']
# spy_data = yf.download('SPY', period='1d')['Adj Close']

df.to_csv("../data/underlying_price.csv")
# Print the fetched data
pprint(df)
# print(basket_data)
# print(spy_data)
