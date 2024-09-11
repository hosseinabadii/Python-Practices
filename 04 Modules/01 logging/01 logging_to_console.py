import logging
import os

os.system("clear")
"""
There are 5 level for logging
#1 CRITICAL
    show the logs:  critical
#2 ERROR
    show the logs:  critical  error
#3 WARNING
    show the logs:  critical  error  warning
#4 INFO
    show the logs:  critical  error  warning  info
#5 DEBUG
    show the logs:  critical  error  warning  info  debug

"""


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()
