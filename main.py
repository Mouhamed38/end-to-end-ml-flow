from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME=" DATA INGESTION STAGE"

try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e :
        logger.exception(e)

STAGE_NAME=" DATA VALIDATION STAGE"

try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e :
        logger.exception(e)

STAGE_NAME=" DATA TRANSFORMATION STAGE"
try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e :
        logger.exception(e)


STAGE_NAME=" MODEL TRAINING STAGE"
try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e :
        logger.exception(e)

STAGE_NAME=" MODEL EVALUATION STAGE"
try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<")
        obj= ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e :
        logger.exception(e)
