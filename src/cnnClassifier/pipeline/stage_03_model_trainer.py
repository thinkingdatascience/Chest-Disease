from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

STAGE_NAME = "Training Stage"


class TrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_updated_base_model()
        training.training_validation_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<\n\nx===========x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
