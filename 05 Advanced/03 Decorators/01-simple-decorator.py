from time import sleep
import functools
import os
os.system("clear")
"""
Simple Decorators:
  Decorator with no arguments.

In decorators, wrapper function has a reference of func in its enclosing scope (wrapper.__closure__),
so it can access to it.
Uncomment the print function to see it returns True.

Hint: __closere__ references are read only (immutable), so they aren't able to modify.
"""

def time_delay(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print(wrapper.__closure__[0].cell_contents is func)
        print("Waiting for 1 seconds...")
        sleep(1)
        output = func(*args, **kwargs)
        return output
    return wrapper

@time_delay
def factorial(n: int) -> int:
    """Calculate the factorial of n"""
    fact = 1
    for num in range(1, n + 1):
        fact *= num
    return fact

# factorial = time_delay(factorial) replace with syntactic suger @
print(f"factorial of input  : {factorial(5)}")
print(f"function name       : {factorial.__name__}")
print(f"function docstring  : {factorial.__doc__}")
print(f"function annotations: {factorial.__annotations__}")