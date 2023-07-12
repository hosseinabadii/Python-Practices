import functools
import os
os.system("clear")

def repeat(num_repeat=2):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_repeat+1):
                print(i)
                output = func(*args, **kwargs)
                print(output)
            return output
        return wrapper
    return repeat_decorator

@repeat(num_repeat=6)
def welcome(fname, lname):
    return (f'{fname} {lname} welcome to Python')


welcome('khosro', 'HosseinAbadi')