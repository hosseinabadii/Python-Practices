import os
from pydantic import BaseModel, Field, ValidationError


class Test(BaseModel):
    var1: str = Field(min_length=4, max_length=8)
    var2: int = Field(ge=10, lt=15)
    var3: float = Field(default=51)
    var4: list = Field(default_factory=list)


if __name__ == "__main__":
    os.system("clear")
    print(Test(var1="John", var2="10.0", var4=[30, 40]))
    print("-" * 50)
    print(Test(var1="John", var2=10, var3=15.8))
    print("-" * 50)
    try:
        print(Test(var1="Joh", var2=10, var3=14.5))
    except ValidationError as e:
        print(e)
    print("-" * 50)
