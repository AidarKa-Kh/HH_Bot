import logging
from hh_client.client import client
import time

logger = logging.getLogger(__name__)

def main():
    while True:
        client.process()
        time.sleep(14700)


if __name__ == '__main__':
    try:
        logger.info('Скрипт запущен.')
        main()
    except KeyboardInterrupt:
        logger.info('Скрипт остановлен.')
