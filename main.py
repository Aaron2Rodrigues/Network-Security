from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.exceptions.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

import sys
from dotenv import load_dotenv
load_dotenv()

import os

if __name__ == "__main__":
    try:
          # Load environment variables
        logging.info("Starting the training pipeline configuration.")
        
        trainingpipeline = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipeline)
        
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating Data Ingestion")
        
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        
        logging.info("Data Ingestion Completed Successfully.")
        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)
