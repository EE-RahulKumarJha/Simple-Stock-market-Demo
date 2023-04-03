import random

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self):
        change = random.uniform(-0.1, 0.1) * self.price
        self.price += change

class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def update_prices(self):
        for stock in self.stocks.values():
            stock.update_price()

    def get_price(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol].price
        else:
            raise ValueError("Stock not found.")

if __name__ == '__main__':
    market = StockMarket()
    market.add_stock(Stock("AAPL", 150))
    market.add_stock(Stock("GOOG", 1200))
    market.add_stock(Stock("TSLA", 700))
    for i in range(10):
        market.update_prices()
        print(f"AAPL: {market.get_price('AAPL')}, GOOG: {market.get_price('GOOG')}, TSLA: {market.get_price('TSLA')}")
