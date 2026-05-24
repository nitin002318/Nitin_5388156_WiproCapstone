import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")


def get_logger():

    logger = logging.getLogger("MyntraLogger")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/test.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger