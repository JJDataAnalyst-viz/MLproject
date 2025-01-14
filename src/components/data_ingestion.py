import yaml
import pandas as pd
import sys
import os 
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import Transformation

@dataclass
class DataIngestionConfig:
        train_data_path: str=os.path.join("artifacts","train.csv")
        test_data_path: str=os.path.join("artifacts","test.csv")
        raw_data_path: str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_Config = DataIngestionConfig()
         

    def initiate_data_ingestion(self):
         '''Function for extract data from source and create train test split'''
         logging.info('Starting ingestion part.....')
         try:
            # Copy path from raw folder, yet still we can give first hand link there to dataset
            yml_data = yaml.safe_load(open('data.yml'))['ingestion']
            logging.info('Upload yaml file')

            df = pd.read_csv(filepath_or_buffer=yml_data['data_extract'])
            logging.info('Create a dataframe')

            os.makedirs(os.path.dirname(self.ingestion_Config.raw_data_path),exist_ok=True)
            logging.info('Creating an artifacts folder')

            df.to_csv(self.ingestion_Config.raw_data_path,index=False,header=True)
            logging.info('Loading raw dataset info artifacts folder')
        
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            logging.info('Train_test split of dataframe')
            train_set = pd.DataFrame(train_set)
            test_set = pd.DataFrame(test_set)
            train_set.to_csv(self.ingestion_Config.train_data_path,index=False)
            logging.info('train data send to artifacts path')

            test_set.to_csv(self.ingestion_Config.test_data_path,index=False)
            logging.info('test data send to artifacts path')

            return(
                 self.ingestion_Config.train_data_path,
                 self.ingestion_Config.test_data_path,
                 
            )

         except Exception as e:
              raise CustomException(e,sys)


if __name__=="__main__":
    obj = DataIngestion()
    train,test = obj.initiate_data_ingestion()
    obj = Transformation()
    data = obj.initiate_data_transformation(train,test)

    # train_set,test_set=transformation(train,test)








