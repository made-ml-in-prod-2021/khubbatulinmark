# -*- coding: utf-8 -*-
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from heart_disease.entities import SplittingParams


def read_data(path: str) -> pd.DataFrame:
    """Reading dataset from path

    :param
    ---------
    path : str
        Path to dataset
    :return
    ---------
    object
        Dataset
    """

    data = pd.read_csv(path)
    return data


def split_train_val_data(
                        data: pd.DataFrame,
                        params: SplittingParams
                        ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    :rtype: object

    """
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data
