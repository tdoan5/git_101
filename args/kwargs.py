def print_tickers(**kwargs):
    for stock, ticker in kwargs.items():
        print("The ticker of {} is {}".format(stock, ticker))

print_tickers(
            stock_1="AAPL",
            stock_2="GOOGL",
            stock_3="AMZN",
            stock_4="FB",
            stock_5="IBM",
            stock_6="TSLA"
        )

def pass_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1: {}".format(kwarg_1))
    print("kwarg_2: {}".format(kwarg_2))
    print("kwarg_3: {}".format(kwarg_3))

kwargs = {"kwarg_1": "ABC", "kwarg_2": "OPQ", "kwarg_3": "XYZ"}
pass_kwargs(**kwargs)