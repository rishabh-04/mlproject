# for logging - any execution info must be logged inorder to track - exception also log into text file
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #log file name with timestamp - txtfile
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #logs folder path + log file name
os.makedirs(logs_path,exist_ok=True) #if logs folder not present - create it
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) #complete log file path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s", #level name, filename, line number, message#
    level=logging.INFO,
)#logging configuration - log file path, format of log message , level of logging - info, debug, error

if __name__ == "__main__":
    logging.info("Logging has started") #test log message - info level