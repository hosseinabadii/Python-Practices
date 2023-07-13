"""
By using classmethods you can call __init__() method with specific arguments.
"""
class Person:
    nationality: str = "Iranian"  # this is a class attribute.

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name)
    
person = Person.from_full_name('Reza Hosseini')
print(f"person first name  : {person.first_name}")
print(f"person last name   : {person.last_name}")
print(f"person nationality : {person.nationality}")
