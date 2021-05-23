import os
import pickle
from typing import List, Tuple

import pandas as pd
import pytest
from py._path.local import LocalPath
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from src.entities.feature_params import FeatureParams
from src.features import build_transformer, extract_target, make_features
from src.models.fit import serialize_model, train_model


@pytest.fixture
def features_and_target(
    dataset: pd.DataFrame, categorical_features: List[str], numerical_features: List[str]
) -> Tuple[pd.DataFrame, pd.Series]:
    params = FeatureParams(
        categorical_features=categorical_features,
        numerical_features=numerical_features,
        features_to_drop=[],
        target_col="target",
    )
    transformer = build_transformer(params)
    transformer.fit(dataset)
    features = make_features(transformer, dataset)
    target = extract_target(dataset, params)
    return features, target


@pytest.mark.parametrize(
    "model, model_class",
    [
        pytest.param(pytest.lazy_fixture('log_reg_model'), LogisticRegression, id="age"),
        pytest.param(pytest.lazy_fixture('rf_model'), RandomForestClassifier, id="rf"),
    ],
)
def test_train_model(features_and_target: Tuple[pd.DataFrame, pd.Series], model, model_class):
    features, target = features_and_target
    model = train_model(model, features, target)
    assert isinstance(model, model_class)


def test_serialize_model(tmpdir: LocalPath):
    expected_output = tmpdir.join("model.pkl")
    n_estimators = 100
    model = RandomForestClassifier(n_estimators=n_estimators)
    real_output = serialize_model(model, expected_output)
    assert real_output == expected_output
    assert os.path.exists
    with open(real_output, "rb") as f:
        model = pickle.load(f)
    assert isinstance(model, RandomForestClassifier)
