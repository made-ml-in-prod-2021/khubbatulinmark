import os
import json
import typing
import logging
import logging.config

import yaml
import hydra
import pandas as pd
from omegaconf import DictConfig, OmegaConf

from src.utils import setup_logging, construct_abs_path
from src.data import read_data, split_train_val_data
from src.entities import (
    RFConfig,
    LogregConfig,
    TrainingPipelineConfig,
    SplittingParams
)
from src.features import make_features
from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
)

from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate

APPLICATION_NAME = "train_pipeline"
logger = logging.getLogger(APPLICATION_NAME)


def prepare_val_features_for_predict(
    train_features: pd.DataFrame, val_features: pd.DataFrame
):
    train_features, val_features = train_features.align(
        val_features, join="left", axis=1
    )
    val_features = val_features.fillna(0)
    return val_features


def train_pipeline(params: TrainingPipelineConfig):
    """E2E train pipeline function"""
    logger.info("Starting train")

    data = read_data(params.general.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    train_df, val_df = split_train_val_data(
        data, params.split
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")
    transformer = build_transformer(params.general.feature_params)
    transformer.fit(train_df)
    train_features = make_features(transformer, train_df)
    train_target = extract_target(train_df, params.general.feature_params)

    logger.info(f"train_features.shape is {train_features.shape}")

    model = train_model(
        params.model.model_params,
        train_features, train_target
    )

    val_features = make_features(transformer, val_df)
    val_target = extract_target(val_df, params.general.feature_params)

    val_features_prepared = prepare_val_features_for_predict(
        train_features, val_features
    )
    logger.info(f"val_features.shape is {val_features_prepared.shape}")
    predicts = predict_model(
        model,
        val_features_prepared
    )

    metrics = evaluate_model(
        predicts,
        val_target
    )

    if params.general.output_hydra:
        metrics_output_dir = params.general.metric_dir
        model_output_dir = params.general.model_dir
    else:
        metrics_output_dir = construct_abs_path(params.general.metric_dir)
        model_output_dir = construct_abs_path(params.general.model_dir)

    os.makedirs(metrics_output_dir, exist_ok=True)
    metrics_filepath = os.path.join(metrics_output_dir, f"{params.model.model_name}.json")
    with open(metrics_filepath, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"metrics is {metrics}")
    logger.info(f"metrics saved to {metrics_filepath,}")

    os.makedirs(model_output_dir, exist_ok=True)
    models_filepath = os.path.join(model_output_dir, f"{params.model.model_name}.pkl")
    path_to_model = serialize_model(model, models_filepath)
    logger.info(f"model saved to {models_filepath,}")

    logger.info("Finish train")
    return path_to_model, metrics


@hydra.main(config_path='../configs', config_name='config')
def main(cfg: TrainingPipelineConfig) -> None:
    """Main function for setting logger and run train_pipeline"""
    os.makedirs("logs", exist_ok=True)
    setup_logging(cfg.logger)
    train_pipeline(cfg)


if __name__ == "__main__":
    main()

