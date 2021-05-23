import os
import yaml
import logging
import logging.config

import hydra
from omegaconf import DictConfig, OmegaConf


def construct_abs_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    root = hydra.utils.get_original_cwd()
    return os.path.join(root, path)


def setup_logging(logger_params):
    """Setup logging configurations from dict """
    logger_params_str = OmegaConf.to_yaml(logger_params)
    #logging.config.dictConfig(logger_params_dict) - Тут пришлось косыльнуть - пока не понял почему не работает
    logging.config.dictConfig(yaml.safe_load(logger_params_str))
