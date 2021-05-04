from heart_disease.data.make_dataset import read_data


def test_load_dataset(dataset_path: str, target_col: str):
    data = read_data(dataset_path)
    assert len(data) == 10
    assert target_col in data.keys(), (
            "target_col not in dataset"
        )

