import logging
import os
from datetime import datetime
import sys

#Log File Name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H_%M_%S')}.log"


#Create folder if not available
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_FILE_DIR,exist_ok=True)


#Log file Path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)

