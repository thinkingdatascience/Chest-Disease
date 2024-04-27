import gdown
from zipfile import ZipFile
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import create_directories
from cnnClassifier import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self) -> str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file

            create_directories(path_to_directories=[self.config.root_dir])
            logger.info(
                f"Downloading data from {dataset_url} into the file{zip_download_dir}"
            )

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=downloads&id="

            gdown.download(url=prefix + file_id, output=zip_download_dir)

            logger.info(
                f"Downloaded data from {dataset_url} into the file{zip_download_dir}"
            )
        except Exception as e:
            raise e

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        create_directories(path_to_directories=unzip_path)

        with ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
