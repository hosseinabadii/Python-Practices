import functools
"""
Add a 'counter' attribute to 'wrapper' function to store the state.
"""
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        print(f'\nFunction {func.__name__!r} is calling for {wrapper.counter} times.')
        return func(*args, **kwargs)
    
    wrapper.counter = 0
    return wrapper


@count_calls
def hello():
    print('Hello beginner')

hello()
hello()
hello()