When ordering arguments within a function or function call, arguments need to occur in a particular order:

1. Formal positional arguments
2. *args
3. Keyword arguments
4. **kwargs

def some_func(arg_1, arg_2, *args, kw_1="stock", kw_2="bond", **kwargs):
...