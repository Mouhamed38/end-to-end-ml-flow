from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger



STAGE_NAME=" DATA INGESTION STAGE"
class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        manag_config=ConfigurationManager()
        configM=manag_config.get_data_ingestion_config()
        data_ing=DataIngestion(configM)
        data_ing.dowload_file()
        data_ing.extract_zip_file()
    

if __name__== '__main__':
    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e :
        logger.exception(e)
