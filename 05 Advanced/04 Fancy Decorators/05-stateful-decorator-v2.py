"""
Rather than adding a `counter` attribute to `wrapper` function
we can use `nonlocal counter` to access and modify the counter
variable from the enclosing scope.
"""

import functools


def count_calls(func):
    counter = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"\nFunction {func.__name__!r} is calling for {counter} times.")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def hello():
    print("Hello beginner")


hello()
hello()
hello()
