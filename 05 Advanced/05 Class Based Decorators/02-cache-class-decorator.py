class Cache:
    def __init__(self, func):
        self.func = func
        self.cached = {}

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        value = self.cached.get(key)
        if not value:
            print(f"\nCalling function {self.func.__name__!r}...")
            value = self.func(*args, **kwargs)
            self.cached[key] = value
            return value
        
        print(f"\nRetrieving value from cache...")
        return value
    

@Cache
def computation(n, *, value_name):
    for _ in range(n):
        x = [value ** 2 for value in range(n)]
    return f"{value_name} result is {sum(x) / len(x)}"

print(computation(5000, value_name="first"))

print(computation(5000, value_name="first"))

print(computation(5000, value_name="first"))

print(computation(5000, value_name="second"))

print(computation(4000, value_name="first"))

print(computation(4000, value_name="first"))
