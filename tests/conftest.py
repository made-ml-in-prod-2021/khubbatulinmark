import os

import pytest
from typing import List


@pytest.fixture()
def dataset_path():
    curr_dir = os.path.dirname(__file__)
    return os.path.join(curr_dir, "train_data_sample.csv")


@pytest.fixture()
def target_col():
    return "target"
#
#
# @pytest.fixture()
# def categorical_features() -> List[str]:
#     return [
#         "MSZoning",
#         "Neighborhood",
#         "RoofStyle",
#         "MasVnrType",
#         "BsmtQual",
#         "BsmtExposure",
#         "HeatingQC",
#         "CentralAir",
#         "KitchenQual",
#         "FireplaceQu",
#         "GarageType",
#         "GarageFinish",
#         "PavedDrive",
#     ]
#
#
# @pytest.fixture
# def numerical_features() -> List[str]:
#     return [
#         "OverallQual",
#         "MSSubClass",
#         "OverallCond",
#         "GrLivArea",
#         "GarageCars",
#         "1stFlrSF",
#         "Fireplaces",
#         "BsmtFullBath",
#         "YrSold",
#         "YearRemodAdd",
#         "LotFrontage",
#     ]
#
#
# @pytest.fixture()
# def features_to_drop() -> List[str]:
#     return ["YrSold"]
