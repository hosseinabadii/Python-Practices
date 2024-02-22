import functools
import os
from time import sleep

os.system("clear")


def delay(seconds=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting for {seconds} seconds...")
            sleep(seconds)
            output = func(*args, **kwargs)
            return output

        return wrapper

    return decorator


@delay(seconds=3)  # When calling the time_delay(3), it returns the 'decorator' function
def factorial(n: int) -> int:
    """Calculate the factorial of n"""
    fact = 1
    for num in range(1, n + 1):
        fact *= num
    return fact


print(f"factorial of input  : {factorial(5)}")
print(f"function name       : {factorial.__name__}")
print(f"function docstring  : {factorial.__doc__}")
print(f"function annotations: {factorial.__annotations__}")
