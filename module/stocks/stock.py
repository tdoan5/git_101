class Stock():
    def __init__(self, ticker):
        self.ticker = ticker

    def set_price(self,price):
        self.price = price

    def get_ticker(self):
        return self.ticker

    def get_price(self):
        return self.price

    def sell(self, volumn):
        print(str(volumn) + " " + 
            str(self.get_ticker()) + " stocks sold with price $" + str(self.get_price()))