# https://towardsdatascience.com/six-levels-of-python-decorators-1f12c9067b23

# the simple decorator

"""
def logging_decorator(func):
    def wrapper():
        print(f"[LOG] \t calling {func.__name__}")
        func()
        print(f"[LOG] called {func.__name__}")
    return wrapper

@logging_decorator
def sayhello():
    # Function to be decorated; just prints a string
    print("\t=== Hello from the function")

if (__name__ == "__main__"):
    result = sayhello()
"""


# passing arguments and a return value
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] \t calling {func.__name__}")
        res = func(*args, **kwargs)
        print(f"[LOG] called {func.__name__}")
        return res
    return wrapper

@logging_decorator
def multiply(number_a: int, number_b: int):
    print("\t\t=== Inside the multiply function")
    return number_a * number_b

if (__name__ == "__main__"):
    result = multiply(3,4)
    print(f"[result] \t {result}")