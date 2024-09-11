import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    fmt="%(name)s:%(levelname)s | %(asctime)s | %(message)s",
    datefmt="%m-%d %H:%M",
)
console_handler.setFormatter(console_formatter)
console_handler.setLevel(level=logging.DEBUG)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("debug.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(level=logging.ERROR)
logger.addHandler(file_handler)


def main():
    logger.debug("This is a debug log")
    logger.debug("This is a debug log")
    logger.info("This is an info log")
    logger.warning("This is an warning log")
    logger.error("This is an error log")
    logger.critical("This is a critical log")


if __name__ == "__main__":
    main()
