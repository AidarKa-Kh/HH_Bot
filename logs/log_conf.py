import logging
from logging.handlers import RotatingFileHandler
import os
import urllib3

# Общий лог-файл
LOG_FILE = os.path.join('logs/data', "app.log")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(module)15s:%(lineno)3d - %(levelname)8s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        encoding='Windows-1251',
        handlers=[
            RotatingFileHandler(LOG_FILE, maxBytes=10**6, backupCount=3),  # Ротация логов
            logging.StreamHandler(),  # Вывод в консоль
        ]
    )

    logging.getLogger("requests").setLevel(logging.WARNING)


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
