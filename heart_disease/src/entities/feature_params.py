from dataclasses import dataclass, field
from typing import List, Optional

from omegaconf import MISSING


@dataclass()
class FeatureParams:
    categorical_features: List[str]
    numerical_features: List[str]
    target_col: List[str]
    use_log_trick: bool = field(default=True)
    features_to_drop: List[str] = MISSING


@dataclass()
class TransformerConfig:
    feature_params: FeatureParams
