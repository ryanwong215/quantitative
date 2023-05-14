from IndexArbitrage import IndexArbitrage

basket_tickers = ['AAPL', 'MSFT', 'AMZN', 'META', 'GOOGL']
basket_weights = [0.2, 0.2, 0.2, 0.2, 0.2]

arbitrage = IndexArbitrage(basket_tickers, basket_weights)
opportunity = arbitrage.check_arbitrage_opportunity()

if opportunity['opportunity'] == 'buy_spy':
    print(f"Arbitrage Opportunity: Buy SPY at {opportunity['spy_price']} and sell the basket of stocks.")
    # Place your order execution code here

elif opportunity['opportunity'] == 'sell_spy':
    print(f"Arbitrage Opportunity: Sell SPY at {opportunity['spy_price']} and buy the basket of stocks.")
    # Place your order execution code here

else:
    print("No arbitrage opportunity at the moment.")
