import os 
import sys 
import pandas as pd 
import numpy as np

from dataclasses import dataclass
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger  import logging

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler


from src.DimondPricePrediction.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifact","preprocessor.pkl") 


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    
    def get_data_transformation(self):
        
        try:
            logging.info("Data Transformation initiated ")
            
            # define which columns should be ordinal- encoded and which should be scaled 
            categorical_cols=["cut","color","clarity"]
            numerical_cols=["carat","depth","table","x","y","z"]
            
            # define the custome ranking for each ordinal variable
            cut_categories=["Fair","Good","Very Good","Premium","Ideal"]
            clarity_categories=["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
            color_categories=["D","E","F","G","H","I","J"]
            
            logging.info("Pipeline Initiated")
            
            # Numerical pipeline
            numerical_pipeline=Pipeline(
    
                steps=[
        
                    ('imputer',SimpleImputer()),
                    ('scaler',StandardScaler())     
                ]
    
            )
            
            # Categorical Pipeline
            categorical_pipeline=Pipeline(
    
                steps=[
        
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('OrdinalEncoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))
                ]    
            )
            
            preprocessor=ColumnTransformer(
    
                [
        
                    ('numerical_pipeline',numerical_pipeline,numerical_cols),
                    ('categorical_pipeline',categorical_pipeline,categorical_cols)
                ]  
            )
            
            return preprocessor
            
        except Exception as e :
            logging.info("Exception occured in the initiate_data_transformation")
            
            raise customexception(e,sys)   
            
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            
            
            logging.info("Read train and test data complete ")
            logging.info(f"Train DataFrame Head : \n {train_df.head().to_string()}")
            logging.info(f"Test DataFrame Head : \n {test_df.head().to_string()}")
            
            
            perprocessing_obj=self.get_data_transformation()
            
            target_column_name='price'
            drop_columns=[target_column_name,'id']
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df= train_df[target_column_name]
            
            input_feature_train_arr= perprocessing_obj.fit_transform(input_feature_train_df)
            
            # For Validation 
            input_feature_test_arr= perprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing onject on training and testing datasets .")
            
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path
                obj=perprocessing_obj
            )
            
        except Exception as e :
            logging.info("Exception occured in the initiate_data_transformation")
            
            raise customexception(e,sys) 
        
       
    