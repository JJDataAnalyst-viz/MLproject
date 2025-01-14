from src.exception import CustomException
import sys
import os
import numpy as np
from dataclasses import dataclass
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler 
from src.logger import logging
from src.utils import save_object
@dataclass
class TransformationConfig:
    preprocessed_path: str = os.path.join("atrifacts","preprocessed.pkl")

class Transformation:
    def __init__(self):
        self.transformation = TransformationConfig()

    def get_transformation_data(self):
        '''Transform our test and train data into numerical data'''
        try:

            numerical_features = ['reading_score','writing_score']
            categorical_features = [ "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",]
            logging.info('selecting dtypes of my columns')

            num_pipeline = Pipeline(
                steps=[
                ("SimpleImputer",SimpleImputer(strategy='mean')),
                ("StandardScaler",StandardScaler(with_mean=False))
                ])
            
            cat_pipeline = Pipeline(
                steps=[
                    ("SimpleImputer",SimpleImputer(strategy='most_frequent')),
                    ("OneHotEncoding",OneHotEncoder()),
                    ("StandardScaler",StandardScaler(with_mean=False))
                ]
            )
            
            logging.info('Creating pipelines for categorical and numerical features')

            preprocessor = ColumnTransformer(
               [
                 ("numerical tranformation",num_pipeline,numerical_features),
                ("categorical transformation",cat_pipeline,categorical_features)
               ]
                                                    )
            logging.info('making columntransformer for my dataset')
            #       ///Logging                                  
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
        # Defining type of data in parameter
    def initiate_data_transformation(self,train,test):
        '''This function help to preprocessing our data by ColumnTransformer
            param: train set 
            param: test set
        '''
        try:    
            train = pd.read_csv(train)
            test = pd.read_csv(test)
            logging.info('gathering test and train dataset')
            col_rm_train = ['math_score','Unnamed: 0']
            
            X_train_input_feature = train.drop(columns=col_rm_train,axis=1)
            y_train_input_feature = train['math_score']
            logging.info('Creating training datset')

            
            X_test_input_feature = test.drop(columns=col_rm_train,axis=1)
            y_test_input_feature = test['math_score']
            logging.info('Creating testing datset')

            preprocess = self.get_transformation_data()

            X_train_input_feature_arr =preprocess.fit_transform(X_train_input_feature)
            X_test_input_feature_arr =preprocess.transform(X_test_input_feature)
            train_arr = np.c_[X_train_input_feature_arr,np.array(X_train_input_feature)]
            test_arr = np.c_[X_test_input_feature_arr,np.array(X_test_input_feature)]
            logging.info('preprocessing data')
            
            save_object(
                file_path = self.transformation.preprocessed_path,
                obj = preprocess
            )


            return (train_arr,test_arr,self.transformation.preprocessed_path)
       
            
        except Exception as e:
            raise CustomException(e,sys)
   