import functools

def repeat(_func=None, *, num_repeat=2):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_repeat):
                output = func(*args, **kwargs)
                print(output)
            return output
        return wrapper
    
    
    if _func is None:
        print(f"*** The _func is None ***")
        return repeat_decorator
    
    print(f"*** The _func is {_func.__name__!r} ***")
    return repeat_decorator(_func)
    

print(f"\nUsing decorator with keyword only argument: num_repeat=4")
@repeat(num_repeat=4)  # In this case _func is None
def welcome(fname, lname):
    return (f'{fname} {lname} welcome to Python')

welcome('khosro', 'HosseinAbadi')


print("\nUsing decorator without argument: default num_repeat=2")
@repeat               # In this case _func is 'welcome' function
def welcome(fname, lname):
    return (f'{fname} {lname} welcome to Python')

welcome('khosro', 'HosseinAbadi')