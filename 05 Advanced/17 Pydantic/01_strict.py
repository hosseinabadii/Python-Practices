import os
from pydantic import BaseModel, ValidationError
from pydantic import StrictStr, StrictInt, StrictFloat, StrictBool


class Test1(BaseModel):
    var1: str
    var2: int
    var3: float
    var4: bool


class Test2(BaseModel):
    var1: StrictStr
    var2: StrictInt
    var3: StrictFloat
    var4: StrictBool


if __name__ == "__main__":
    os.system("clear")
    print(Test1(var1="John", var2="20.0", var3="15.8", var4="True"))
    print("-" * 50)

    try:
        print(Test2(var1="John", var2=20.0, var3=15.8, var4=True))
    except ValidationError as e:
        print(e)
    print("-" * 50)

    try:
        print(Test2(var1="John", var2=20, var3=14.5, var4="True"))
    except ValidationError as e:
        print(e)
    print("-" * 50)
