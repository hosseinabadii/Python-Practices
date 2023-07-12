import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k!r}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"\nCalling {func.__name__}({signature}) \n")
        output = func(*args, **kwargs)
        print(f"\n{func.__name__!r} returned {output!r}")
        return output
    return wrapper


@debug
def signup(firstname, lastname, * , username, password):
    print(f"Hello {firstname} {lastname}")
    print(f"Your username is {username}")
    print(f"Your password is {password}")

signup("Khosro", "HosseinAbadi", username="python10", password="123456")