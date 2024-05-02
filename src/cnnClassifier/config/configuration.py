import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import create_directories, read_yaml
from cnnClassifier.entity.config_entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig,
    TrainingConfig,
    EvaluationConfig,
)


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH
    ) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories(
            path_to_directories=[self.config.artifacts_root, self.config.model_root]
        )

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories(path_to_directories=[config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories(path_to_directories=[config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_classes=self.params.CLASSES,
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_learning_rate=self.params.LEARNING_RATE,
            params_weights=self.params.WEIGHTS,
        )

        return prepare_base_model_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        training_data = self.config.data_ingestion.unzip_dir

        create_directories(path_to_directories=[training.root_dir])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            save_model_path=Path(training.save_model_path),
            training_data=os.path.join(training_data, "Chest-CT-Scan-data"),
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_augmentation=self.params.AUGMENTATION,
            params_image_size=self.params.IMAGE_SIZE,
        )

        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        training_data = self.config.data_ingestion.unzip_dir
        training = self.config.training

        evaluation_config = EvaluationConfig(
            path_of_model=training.trained_model_path,
            training_data=os.path.join(training_data, "Chest-CT-Scan-data"),
            all_params=self.params,
            mlflow_uri="https://dagshub.com/thinkingdatascience/Chest-Disease.mlflow",
            params_batch_size=self.params.BATCH_SIZE,
            params_image_size=self.params.IMAGE_SIZE,
        )

        return evaluation_config
