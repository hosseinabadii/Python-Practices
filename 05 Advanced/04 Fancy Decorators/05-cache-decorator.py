import functools

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nCalling function {wrapper.__name__!r}...")
        key = str(args) + str(kwargs)
        value = wrapper.cached.get(key)
        if not value:
            output = func(*args, **kwargs)
            wrapper.cached[key] = output
            return output
        print(f"\nRetrieving value from cache...")
        return value
    
    wrapper.cached = {}
    return wrapper

# @functools.lru_cache      ## You can easily use 'lru_cache' decorator from functools module.
# @functools.cache          ## You can easily use 'cache' decorator from functools module.
@cache
def computation(n, *, value_name):
    for _ in range(n):
        x = [value ** 2 for value in range(n)]
    return f"{value_name} result is {sum(x) / len(x)}"

print(computation(5000, value_name="first"))

print(computation(5000, value_name="first"))

print(computation(5000, value_name="first"))

print(computation(5000, value_name="second"))

print(computation(4000, value_name="first"))

