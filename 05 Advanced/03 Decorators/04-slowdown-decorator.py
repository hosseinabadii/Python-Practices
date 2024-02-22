import functools
from time import sleep


def slowdown(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Waiting for 1 second...")
        sleep(1)
        output = func(*args, **kwargs)
        return output

    return wrapper


@slowdown
def stopwatch(timer: int) -> None:
    if timer < 1:
        print(f"{timer:0>3d}")
    else:
        print(f"{timer:0>3d}")
        timer -= 1
        stopwatch(timer)


stopwatch(10)
