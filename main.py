from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_validation import DataValidation
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig , DataValidationConfig

import sys
from dotenv import load_dotenv
load_dotenv()

import os

if __name__ == "__main__":
    try:
          # Load environment variables
        logging.info("Starting the training pipeline configuration.")
        
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating Data Ingestion")
        
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        
        logging.info("Data Ingestion Completed Successfully.")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiating Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data Validation Completed")


        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)

    
