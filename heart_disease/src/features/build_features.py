import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from ..entities.feature_params import FeatureParams, TransformerConfig


def process_categorical_features(categorical_df: pd.DataFrame) -> pd.DataFrame:

    categorical_pipeline = build_categorical_pipeline()
    return pd.DataFrame(categorical_pipeline.fit_transform(categorical_df).toarray())


def build_categorical_pipeline() -> Pipeline:
    categorical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
            ("ohe", OneHotEncoder()),
        ]
    )
    return categorical_pipeline


def process_numerical_features(numerical_df: pd.DataFrame) -> pd.DataFrame:
    num_pipeline = build_numerical_pipeline()
    return pd.DataFrame(num_pipeline.fit_transform(numerical_df))


def build_numerical_pipeline() -> Pipeline:
    num_pipeline = Pipeline(
        [
            ('outlier', OutlierRemover()),
            ("impute", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ]
    )
    return num_pipeline


def make_features(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(transformer.transform(df))


def extract_target(df: pd.DataFrame, params: FeatureParams) -> pd.Series:
    target = df[params.target_col].values.ravel()
    return target


class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, factor=1.5):
        self.factor = factor

    def outlier_removal(self, x: pd.DataFrame):
        x = pd.Series(x).copy()
        q1 = x.quantile(0.25)
        q3 = x.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (self.factor * iqr)
        upper_bound = q3 + (self.factor * iqr)
        x.loc[((x < lower_bound) | (x > upper_bound))] = np.nan
        return pd.Series(x)

    def fit(self, x, y=None):
        return self

    def transform(self, x: np.array):
        return pd.DataFrame(x).apply(self.outlier_removal)


def build_transformer(params: TransformerConfig) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "categorical_pipeline",
                build_categorical_pipeline(),
                [c for c in params.categorical_features],
            ),
            (
                "numerical_pipeline",
                build_numerical_pipeline(),
                [n for n in params.numerical_features],
            ),
        ]
    )
    return transformer
