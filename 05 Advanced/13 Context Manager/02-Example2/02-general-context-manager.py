import logging
import os
from contextlib import contextmanager
os.system("clear")
logging.basicConfig(level=logging.INFO)


class DecoratorContextManager:

    def __init__(self, generator):
        logging.info("Calling __init__...")
        self.generator = generator

    def __call__(self, *args, **kwargs):
        logging.info("Calling __call__...")
        self.gen_instance = self.generator(*args, **kwargs)
        return self

    def __enter__(self):
        logging.info("Calling __enter__...")
        return next(self.gen_instance)

    def __exit__(self, *args):
        logging.info("Calling __exit__...")
        next(self.gen_instance, None)


# @DecoratorContextManager   # it can be easily replaced by @contextmanager
@contextmanager
def open_file_generator(file_path, mode="r"):
    logging.info("Opening file...")
    f = open(file_path, mode)
    yield f
    logging.info("Closing file...")
    f.close()


def main():

    with open_file_generator("data/file.txt", "w+") as f:
        print(f"\n{'=' * 5} The Context {'=' * 30}")
        f.write("This is a new line.")
        f.seek(0)
        print(f.read())
        print("=" * 50)


if __name__ == "__main__":
    main()