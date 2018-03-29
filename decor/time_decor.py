import time

def timing_func(some_func):

    def wrapper():
        t1 = time.time()
        some_func()
        t2 = time.time()
        return "Runtime: " + str((t2 - t1)) + "\n"
    return wrapper

@timing_func
def my_func():
    num_list = []
    for num in (range(0, 1000)):
        num_list.append(num)
    print("\nSum = : " + str((sum(num_list))))

print(my_func())