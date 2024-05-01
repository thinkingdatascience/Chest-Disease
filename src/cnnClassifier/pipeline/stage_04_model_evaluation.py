from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(
            f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<\n\nx===========x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
