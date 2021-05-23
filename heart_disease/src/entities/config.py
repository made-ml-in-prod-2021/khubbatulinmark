from dataclasses import dataclass

import yaml
from hydra.utils import instantiate
from hydra.core.config_store import ConfigStore

from .models_params import ModelConfig
from .general_params import GeneralConfig
from .split_params import SplittingParams


@dataclass
class TrainingPipelineConfig:
    model: ModelConfig
    split: SplittingParams
    general: GeneralConfig


@dataclass
class ReportConfig:
    dir: str
    filename: str
    input_data_path: str
