from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger



STAGE_NAME=" DATA VALIDATION STAGE"
class DataValidationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        manag_config=ConfigurationManager()
        configM=manag_config.get_data_validation_config()
        data_val=DataValidation(configM)
        data_val.validate_all_columns()
    

if __name__== '__main__':
    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e :
        logger.exception(e)
