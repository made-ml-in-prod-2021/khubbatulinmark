from src.data.make_dataset import read_data, split_train_val_data
from src.entities import SplittingParams


def test_load_dataset(dataset_path: str, target_col: str):
    data = read_data(dataset_path)
    assert len(data) == 10
    assert target_col in data.keys(), (
            "target_col not in dataset"
        )


def test_split_dataset(tmpdir, dataset_path: str):
    val_size = 0.2
    splitting_params = SplittingParams(random_state=42, val_size=val_size,)
    data = read_data(dataset_path)
    train, val = split_train_val_data(data, splitting_params)
    assert 8 == train.shape[0]
    assert 2 == val.shape[0]