import os
import json
import logging
import logging.config
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import yaml
import pandas as pd

from src.data import read_data, split_train_val_data
from src.entities import (
    TrainingPipelineParams,
    read_training_pipeline_params
)

from src.features import make_features
from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
)

DEFAULT_DATASET = "./data/raw/heart.csv"
DEFAULT_CONFIG = '.configs/train_config_log_reg.yaml'

APPLICATION_NAME = "train_pipeline"
DEFAULT_LOGGING_CONF_FILEPATH = "./configs/logging.conf.yml"
logger = logging.getLogger(APPLICATION_NAME)


def train_pipeline(training_pipeline_params: TrainingPipelineParams):
    logger.info(f"start train pipeline with params {training_pipeline_params}")
    data = read_data(training_pipeline_params.input_data_path)
    logger.info(f"data.shape is {data.shape}")


def prepare_val_features_for_predict(
    train_features: pd.DataFrame, val_features: pd.DataFrame
):
    train_features, val_features = train_features.align(
        val_features, join="left", axis=1
    )
    val_features = val_features.fillna(0)
    return val_features


def train_pipeline_callback(params):
    """Main train_pipeline callback"""
    logger.info("Starting train train")
    data = read_data(params.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    train_df, val_df = split_train_val_data(
        data, params.splitting_params
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")

    transformer = build_transformer(params.feature_params)
    transformer.fit(train_df)
    train_features = make_features(transformer, train_df)
    train_target = extract_target(train_df, params.feature_params)

    logger.info(f"train_features.shape is {train_features.shape}")

    model = train_model(
        train_features, train_target, params.train_params
    )

    val_features = make_features(transformer, val_df)
    val_target = extract_target(val_df, params.feature_params)

    val_features_prepared = prepare_val_features_for_predict(
        train_features, val_features
    )

    val_features = make_features(transformer, val_df)
    val_target = extract_target(val_df, params.feature_params)

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

    os.makedirs("metrics", exist_ok=True)
    with open(params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"metrics is {metrics}")
    logger.info(f"metrics saved to {params.metric_path,}")

    os.makedirs("models", exist_ok=True)
    path_to_model = serialize_model(model, params.output_model_path)
    logger.info(f"model saved to {params.metric_path,}")

    return path_to_model, metrics

    logger.info("Finish train")


def setup_logging(filepath=DEFAULT_LOGGING_CONF_FILEPATH):
    """Setup logging configurations from file"""
    with open(filepath) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))


def setup_parser(parser):
    """Function for setup the parser"""
    parser.add_argument(
        "-c", "--configs", dest="config_filepath",
        help="Path to configfile to load, default path is %(default)s",
        metavar='CONFIG', default=DEFAULT_CONFIG,
    )
    parser.set_defaults(callback=train_pipeline_callback)


def main():
    """Main function of the module"""
    os.makedirs("logs", exist_ok=True)
    setup_logging()
    parser = ArgumentParser(
        prog="train-pipeline",
        description="This app allows you to train a model for Heart Disease UCI prediction",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    params = read_training_pipeline_params(arguments.config_filepath)
    arguments.callback(params)


if __name__ == "__main__":
    main()

