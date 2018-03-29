from stocks.stock import Stock

my_stock = Stock("GOOGL")
my_stock.get_ticker()

# set price to sell
my_stock.set_price(1000)

if float(my_stock.get_price()) >= 999:
    my_stock.sell(500)