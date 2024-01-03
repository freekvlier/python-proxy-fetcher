# logger_config.py

import logging

def setup_logger():
    # Create a logger object
    logger = logging.getLogger('ProxyFetcherLogger')
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s')

    # Add formatter to console handler
    ch.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(ch)

    return logger
