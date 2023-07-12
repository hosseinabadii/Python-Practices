import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            print("\nCreating instance for the first time...")
            instance = cls(*args, **kwargs)
            wrapper.instance = instance
            return instance
        print("\nThis instance is already exists!")
        return wrapper.instance
    
    wrapper.instance = None
    return wrapper


class Singleton:
    def __init__(self, cls):
        # functools.update_wrapper(self, cls)
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            print("\nCreating instance for the first time...")
            instance = self.cls(*args, **kwargs)
            self.instance = instance
            return instance
        print("\nThis instance is already exists!")
        return self.instance
    

# @Singleton   
@singleton
class Admin:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def __str__(self) -> str:
        return f"username: {self.username}, password: {self.password}"


admin1 = Admin("Khosro", "123456")
print(admin1)

admin2 = Admin("Mahdi", "789789")
print(admin2)

admin3 = Admin("Yalda", "Hrf%$5")
print(admin3)

print(f"'admin1' is 'admin2' is 'admin3' : {admin1 is admin2 is admin3}")

print(admin1.__annotations__)
print(type(admin1))