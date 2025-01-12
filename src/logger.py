import logging 
import os
from datetime import datetime



LOG_FILE = f'%{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
log_file = os.path.join(os.getcwd(),'src','logs')
os.makedirs(log_file,exist_ok=True)

LOG_FILE_PATH = os.path.join(os.getcwd(),'src','logs',LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format= "[%(asctime)s] --%(lineno)d--  %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    )

logging.info('Hello world')