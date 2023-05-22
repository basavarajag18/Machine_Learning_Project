import logging
from datetime import datetime
import os

LOG_DIR= "housing_logs" # directory in which log in our project 
# (All the files which can be stored in this directory )

CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

LOG_FILE_NAME=F"log_{CURRENT_TIME_STAMP}.log"

# check if my directory exists or not? if not then create directory
os.makedirs(LOG_DIR, exist_ok=True) # directory folder for us, whithin that we specify 

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s-%(levelname)s-%(message)s', # time stamp formetting
level=logging.INFO
)

