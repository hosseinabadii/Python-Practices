import random
import string
from dataclasses import dataclass, field

@dataclass
class Information:
    first_name: str
    last_name: str
    phone_number: str = "09151234567"
    country: str = "Iran"
    salary: int = 1000
    id_: str = field(init=False)

    def __post_init__(self):
        self.id_ = "".join(random.choices(string.ascii_uppercase, k=8))

    def __str__(self) -> str:
        return f"This information is for {self.first_name} {self.last_name}"
    
# When you use 'dataclass' decorator, __init__() automatically created.
person1 = Information("Khosro", "HosseinAbadi")
print(person1)
print(person1.phone_number, person1.country, person1.salary, person1.id_)