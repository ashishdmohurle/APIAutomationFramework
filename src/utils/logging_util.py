import logging


# Configure the logger
def setup_logger(name='test_logger', level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console handler for logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Add the console handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    return logger


def log_with_delimiter(logger, message):
    delimiter = "=" * 20
    logger.info(f"{delimiter}{message}{delimiter}")


# Set up logger instance
logger = setup_logger()


def test_logger():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.info("Logger is working correctly")


test_logger()
