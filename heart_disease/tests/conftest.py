import os

import pytest
from typing import List

from src.entities import (
    LogregConfig,
    RFConfig,
    SplittingParams,
    FeatureParams,
    GeneralConfig
)
from tests.data_generator import generate_dataset


@pytest.fixture()
def dataset_path() -> str:
    path = os.path.join(os.path.dirname(__file__), "dataset.zip")
    data = generate_dataset()
    data.to_csv(path, compression="zip")
    return path


@pytest.fixture()
def target_col():
    return "target"


@pytest.fixture()
def categorical_features() -> List[str]:
    return [
        "sex",
        "cp",
        "fbs",
        "restecg",
        "exang",
        "slope",
        "ca",
        "thal",
    ]


@pytest.fixture
def numerical_features() -> List[str]:
    return [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak",
    ]


@pytest.fixture()
def features_to_drop() -> List[str]:
    return []


@pytest.fixture()
def log_reg_model() -> LogregConfig:
    return LogregConfig(
            _target_='sklearn.linear_model.LogisticRegression',
            penalty='l1',
            solver='liblinear',
            C=1.0,
            random_state=42,
            max_iter=100,
    )


@pytest.fixture()
def rf_model() -> RFConfig:
    return RFConfig(
            _target_='sklearn.ensemble.RandomForestClassifier',
            max_depth=100,
            n_estimators=100,
            random_state=42
    )


@pytest.fixture()
def feature_param_v1(categorical_features,
                     numerical_features,
                     target_col,
                     features_to_drop
                     ) -> FeatureParams:
    return FeatureParams(
        categorical_features,
        numerical_features,
        target_col,
        True,
        features_to_drop
    )


@pytest.fixture()
def general_config_v1(dataset_path, feature_param_v1) -> GeneralConfig:
    return GeneralConfig(
        model_dir='models',
        metric_dir='metrics',
        result_dir='result',
        feature_params=feature_param_v1,
        input_data_path=dataset_path,
        random_state=42
    )


@pytest.fixture()
def split_config_v1() -> SplittingParams:
    return SplittingParams(
        val_size=0.25,
        random_state=42
    )
