
import yfinance as yf


class IndexArbitrageNative:
    def __init__(self, basket_tickers, basket_weights):
        self.basket_tickers = basket_tickers
        self.basket_weights = basket_weights

    def calculate_fair_value(self, spy_price, basket_prices):
        # Calculate the fair value of the index futures contract
        fair_value = sum(price * weight for price, weight in zip(basket_prices, self.basket_weights))
        return fair_value

    def check_arbitrage_opportunity(self):
        # Fetch the latest prices of the basket of stocks and SPY
        basket_data = yf.download(self.basket_tickers, period='1d')['Adj Close']
        spy_data = yf.download('SPY', period='1d')['Adj Close']

        # Extract the latest prices from the fetched data
        basket_prices = [basket_data[ticker][-1] for ticker in self.basket_tickers]
        spy_price = spy_data[-1]

        # Calculate the fair value of the index futures contract
        fair_value = self.calculate_fair_value(spy_price, basket_prices)

        # Check if there is an arbitrage opportunity
        if spy_price < fair_value:
            return {
                'opportunity': 'buy_spy',
                'spy_price': spy_price,
                'basket_prices': basket_prices
            }
        elif spy_price > fair_value:
            return {
                'opportunity': 'sell_spy',
                'spy_price': spy_price,
                'basket_prices': basket_prices
            }
        else:
            return {
                'opportunity': 'no_arbitrage',
                'spy_price': spy_price,
                'basket_prices': basket_prices
            }
