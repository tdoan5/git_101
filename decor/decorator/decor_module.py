def my_decorator(some_function):

    def wrapper():

        print("Before some_function() is called.")

        some_function()

        print("After some_function() is called.")

    return wrapper


if __name__ == "__main__":
    my_decorator()