import yfinance as yf
import pandas as pd
import numpy as np

class IndexArbitrage:
    def __init__(self, basket_tickers, basket_weights):
        self.basket_tickers = basket_tickers
        self.basket_weights = basket_weights

    def calculate_fair_value(self, basket_prices):
        # Calculate the fair value of the index futures contract using numpy
        fair_value = np.dot(basket_prices, self.basket_weights)
        return fair_value

    def check_arbitrage_opportunity(self):
        # Fetch the latest prices of the basket of stocks and SPY using pandas
        basket_data = yf.download(self.basket_tickers, period='1d')['Adj Close']
        spy_data = yf.download('SPY', period='1d')['Adj Close']

        # Extract the latest prices from the fetched data using pandas
        basket_prices = basket_data.iloc[-1].values
        spy_price = spy_data.iloc[-1]

        # Calculate the fair value of the index futures contract
        fair_value = self.calculate_fair_value(basket_prices)

        print('fair_value: ' + str(fair_value))
        print('market_value: ' + str(spy_price))

        # Check if there is an arbitrage opportunity
        if spy_price < fair_value:
            return {
                'opportunity': 'buy_spy',
                'spy_price': spy_price,
                'basket_prices': basket_prices.tolist()
            }
        elif spy_price > fair_value:
            return {
                'opportunity': 'sell_spy',
                'spy_price': spy_price,
                'basket_prices': basket_prices.tolist()
            }
        else:
            return {
                'opportunity': 'no_arbitrage',
                'spy_price': spy_price,
                'basket_prices': basket_prices.tolist()
            }

