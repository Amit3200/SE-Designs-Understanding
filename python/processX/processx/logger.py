import logging
import os

DEFAULT_LOG_LEVEL = logging.INFO  # Default to INFO level logging
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = os.getenv('JOB_PROCESSOR_LOG_FILE', None)  # Optional log file from environment

def get_logger(name="job_processor", level=DEFAULT_LOG_LEVEL, log_format=DEFAULT_LOG_FORMAT):
    """
    Returns a configured logger instance.
    :param name: Name of the logger (default is "job_processor").
    :param level: Logging level (default is INFO).
    :param log_format: Format of the log messages (default format provided).
    :return: Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # Optionally log to a file if LOG_FILE is set
    if LOG_FILE:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    # Prevent logging from propagating to the root logger
    logger.propagate = False

    return logger
