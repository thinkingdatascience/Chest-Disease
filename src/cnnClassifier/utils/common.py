from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import os

from cnnClassifier import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, mode="r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directories at path: {path}")
