def my_decorator(some_function):

    def wrapper():

        print("Before some_function() is called.")

        some_function()

        print("After some_function() is called.")

    return wrapper


def just_some_function():
    print("What here?!")


just_some_function = my_decorator(just_some_function)

just_some_function()