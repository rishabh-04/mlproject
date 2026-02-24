#reading data#

import os                         # Used for interacting with operating system (file paths, directories)
import sys                        # Used for system-specific parameters & exception handling
from src.exception import CustomException   # Custom exception class for better error handling
from src.logger import logging    # Logging module to track execution & debug errors
import pandas as pd               # Used for data manipulation using DataFrames
import numpy as np                # Used for numerical operations on arrays

from sklearn.model_selection import train_test_split   # Used to split dataset into training & testing sets
from dataclasses import dataclass   # Used to create classes for storing configuration data

@dataclass #decorator to automatically generate special methods like __init__() for the class
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path to save training data
    test_data_path: str = os.path.join('artifacts', 'test.csv')   # Path to save testing data
    raw_data_path: str = os.path.join('artifacts', 'data.csv')   # Path to save raw data

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self): #method to start data ingestion process
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info("Train test split initiated")
            train_set , test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path , index = False, header = True)

            logging.info("Ingestion of the data is completed")

            return(
                   self.ingestion_config.train_data_path,
                     self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
            
