from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger



STAGE_NAME=" DATA TRANSFORMATION STAGE"
class DataTransformationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            with open('artifacts/data_validation/status.txt', 'r') as f :
                status= f.read().split(' ')[-1]
                print(status)
            if status=='True':

                manag_config=ConfigurationManager()
                configM=manag_config.get_data_transformation_config()
                data_val=DataTransformation(configM)
                data_val.train_test_split()
            else: raise Exception("Data Validation Failed")
        except Exception as e:
            raise e   

if __name__== '__main__':
    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e :
        logger.exception(e)
