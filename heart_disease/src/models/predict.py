from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression


SklearnRegressionModel = Union[RandomForestRegressor, LogisticRegression]


def predict_model(
    model: SklearnRegressionModel, features: pd.DataFrame
) -> np.ndarray:
    predicts = model.predict(features)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series
) -> Dict[str, float]:
    return {
        "accuracy": accuracy_score(target, predicts),
        "roc_auc": roc_auc_score(target, predicts),
    }
