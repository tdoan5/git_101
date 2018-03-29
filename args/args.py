# *args allows to pass in as many arguments as needed
def sum(*args):
    s = 0
    for num in args:
        s += num
    print(s)

sum(1, 2)
sum(1, 2, 3)
sum(1, 2, 3, 4)
"""
3
6
10
"""

# use *args to pass arguments into functions
def pass_args(arg_1, arg_2, arg_3):
    print("argument 1: %s" % arg_1)
    print("argument 2: %s" % arg_2)
    print("argument 3: %s" % arg_3)

print()
args = ("AAPL", "AMZN", "GOOGL")
pass_args(*args)
"""
argument 1: AAPL
argument 2: AMZN
argument 3: GOOGL
"""

print()
args = ("AMZN", "GOOGL")
pass_args("AAPL", *args)
"""
argument 1: AAPL
argument 2: AMZN
argument 3: GOOGL
"""

print()
pass_args(*args, "AAPL")
"""
argument 1: AMZN
argument 2: GOOGL
argument 3: AAPL
"""