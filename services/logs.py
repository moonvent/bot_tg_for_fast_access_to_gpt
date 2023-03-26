import os
from loguru import logger


if logs_file_path := os.environ.get('LOGS_FILE'):
    logger.add(logs_file_path)


log = logger
