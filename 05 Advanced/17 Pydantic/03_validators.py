import os
from pydantic import BaseModel, ValidationError
from pydantic import PositiveInt, NonNegativeInt, HttpUrl, EmailStr


class Test(BaseModel):
    var1: PositiveInt
    var2: NonNegativeInt
    var3: HttpUrl
    var4: EmailStr


if __name__ == "__main__":
    os.system("clear")
    print(Test(var1=10, var2=0, var3="https://www.pytopia.ai", var4="me@gmail.com"))
    print("-" * 50)

    try:
        print(
            Test(var1=-10, var2=0, var3="https://www.pytopia.ai", var4="me@gmail.com")
        )
    except ValidationError as e:
        print(e)
    print("-" * 50)

    try:
        print(Test(var1=10, var2=0, var3="www.pytopia.ai", var4="me@gmail.com"))
    except ValidationError as e:
        print(e)
    print("-" * 50)

    try:
        print(Test(var1=10, var2=0, var3="https://www.pytopia.ai", var4="megmail.com"))
    except ValidationError as e:
        print(e)
    print("-" * 50)
