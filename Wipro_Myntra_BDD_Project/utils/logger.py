import logging
import os


# Logs folder create karega agar nahi hai
if not os.path.exists("logs"):
    os.makedirs("logs")


# Logger Create
logger = logging.getLogger()

logger.setLevel(logging.INFO)


# File Handler
file_handler = logging.FileHandler("logs/test.log")

file_handler.setLevel(logging.INFO)


# Format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)


# Duplicate logs avoid
if not logger.handlers:
    logger.addHandler(file_handler)