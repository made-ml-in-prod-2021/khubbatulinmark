from dataclasses import dataclass

from omegaconf import MISSING

from .split_params import SplittingParams
from .feature_params import FeatureParams


@dataclass
class GeneralConfig:
    model_dir: str == MISSING
    metric_dir: str == MISSING
    result_dir: str == MISSING
    feature_params: FeatureParams = MISSING
    input_data_path: str = MISSING
    output_hydra: bool = MISSING
    random_state: int = 42
