from NetworkSecurity.components.dataingestion import DataIngestion

from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig

from NetworkSecurity.entity.config_entity import ModelTrainerConfig
 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)