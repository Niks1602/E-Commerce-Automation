import logging
from datetime import datetime
from typing import Literal
import os


def logger_setup(testName: str):
    '''
       sets up the logger
    '''
    logs_directory = 'reports/logs'
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)

    if testName:
        filename = f"reports/logs/{'_'.join(testName.split('--')[0].split(' '))}_{datetime.now().strftime('%Y%m%d%H%M%S')}_logs.log"
    else:
        filename = f"reports/logs/{datetime.now().strftime('%Y%m%d%H%M%S')}_logs.log"
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a',
        force=True
    )
    logging.info('Logger setup is done')


def log_message(level: Literal['info', 'error', 'debug', 'warning', 'exception'], message: str):
    '''
        log the message with level
    '''
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'debug':
        logging.debug(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'exception':
        logging.exception(message)



