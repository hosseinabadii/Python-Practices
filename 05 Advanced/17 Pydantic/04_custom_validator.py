import os
import json
from pydantic import BaseModel, model_validator, field_validator


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Author(BaseModel):
    name: str
    verified: bool


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: str | None = None
    isbn_13: str | None = None
    subtitle: str | None = None
    author2: Author | None = None

    @model_validator(mode="before")
    @classmethod
    def check_isbn_10_or_13(cls, values):
        """Make sure there is either an isbn_10 or isbn_13 value defined"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    @field_validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value


if __name__ == "__main__":
    os.system("clear")

    with open("./data/books.json") as f:
        data = json.load(f)

    books = [Book(**info) for info in data]

    book = books[0]
    print("-" * 50)
    print("## book object:\n")
    print(book)
    print("-" * 50)

    print("## model_dump() -> dict:\n")
    print(book.model_dump())
    print("-" * 50)

    print("## model_dump_json() -> str (json serializable):\n")
    print(book.model_dump_json(indent=2))
    print("-" * 50)

    print("## model_fields:\n")
    print(book.model_fields)
