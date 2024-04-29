from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<\n\nx===========x"
    )
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(
        f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<\n\nx===========x"
    )
except Exception as e:
    logger.exception(e)
    raise e
