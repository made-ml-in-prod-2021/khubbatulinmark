import os
import pytest

from py._path.local import LocalPath

from src.train_pipeline import train_pipeline
from src.entities import (
    TrainingPipelineConfig,
    ModelConfig,
    GeneralConfig,
    SplittingParams,
)


@pytest.mark.parametrize(
    "model, model_name",
    [
        pytest.param(pytest.lazy_fixture('log_reg_model'), 'log-reg', id="log-reg"),
        pytest.param(pytest.lazy_fixture('rf_model'), 'rf', id="rf"),
    ],
)
def test_train_e2e(
    tmpdir: LocalPath,
    general_config_v1: GeneralConfig,
    split_config_v1: SplittingParams,
    model,
    model_name,
    caplog, capsys
):
    expected_output_model_path = tmpdir.join("model.pkl")
    expected_metric_path = tmpdir.join("metrics.json")
    params = TrainingPipelineConfig(
        model=ModelConfig(
            model_name=model_name,
            model_params=model,
        ),
        general=general_config_v1,
        split=split_config_v1,
    )
    with caplog.at_level("DEBUG"):

        real_model_path, metrics = train_pipeline(params)
        assert metrics["accuracy"] > 0
        assert os.path.exists(real_model_path)
        assert os.path.exists(params.general.model_dir)
        captured = capsys.readouterr()
        assert '' == captured.out
        assert '' == captured.err
