import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"Finished function {func.__name__!r} in {stop - start}s.")
        return output
    return wrapper


@timer
def factorial(n: int) -> int:
    fact = 1
    for num in range(1, n +1):
        fact *= num
    time.sleep(2)
    return fact

n = 5
print(f"{n}! = {factorial(n)}")