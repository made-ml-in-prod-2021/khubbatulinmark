# -*- coding: utf-8 -*-
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from ..entities import SplittingParams


def read_data(dataset_path: str) -> pd.DataFrame:
    """Reading dataset from path"""

    data = pd.read_csv(dataset_path)
    return data


def split_train_val_data(
                        data: pd.DataFrame,
                        params: SplittingParams
                        ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split dataset into random train and test subsets

    :param
    ---------
    data : object
        Dataset for splitting
    params : object
        Param`s for splitting dataset
    :return
    ---------
    Tuple
        [train_object, test_object]
    """
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data
