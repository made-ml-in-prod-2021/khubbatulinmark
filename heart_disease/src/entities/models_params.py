from dataclasses import dataclass
from typing import Any, Optional

from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate


@dataclass
class RFConfig:
    max_depth: Optional[int] = None
    _target_: str = 'sklearn.ensemble.RandomForestClassifier'
    n_estimators: int = 100
    random_state: int = 42


@dataclass
class LogregConfig:
    _target_: str = 'sklearn.linear_model.LogisticRegression'
    penalty: str = 'l1'
    solver: str = 'liblinear'
    C: float = 1.0
    random_state: int = 42
    max_iter: int = 42


@dataclass
class ModelConfig:
    # We will populate db using composition.
    model_name: str
    model_params: Any = LogregConfig()
