class Counter:
    def __init__(self, func, *, start=0):
        self.func = func
        self.count = start

    def __call__(self, *args, **kwargs):    # It make the objects to be callable.
        self.count += 1
        print(f"\nCalling function {self.func.__name__!r} for {self.count} times...")
        return self.func(*args, **kwargs)

# @Counter
def introduce(firstname: str, lastname: str) -> None:
    """Introduce the new user"""
    print(f"Welcome {firstname} {lastname}")

# introduce = Counter(introduce)   ## Replaced by @Counter


introduce("Ali", "Ahmadi")

introduce("Neda", "Alavi")

print(f"\nfunction name = {introduce.__name__!r}")
print(f"function annotations: {introduce.__annotations__}")
print(f"function docstring: {introduce.__doc__}")