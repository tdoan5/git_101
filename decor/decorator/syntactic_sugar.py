from decor_module import my_decorator

# syntactic sugar "pie"
@my_decorator
def just_some_function():
    print("Hello decor!")

just_some_function()