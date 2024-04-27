from cnnClassifier.constants import *
from cnnClassifier.utils.common import create_directories, read_yaml
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH) -> None:
        self.config = read_yaml(config_file_path)

        create_directories(path_to_directories=[self.config.artifacts_root])

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
