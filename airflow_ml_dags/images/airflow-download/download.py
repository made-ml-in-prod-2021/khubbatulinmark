import logging
import os
import random
import argparse
from pathlib import Path
from typing import Tuple

import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir", type=str, required=True, help="Path to save dataset",
    )
    parser.set_defaults(callback=callback_download)
    arguments = parser.parse_args()
    return arguments


def callback_download(arguments):
    logging.info('Start Download')
    data = kaggle_download(arguments.output_dir)
    logging.info('Dataset len {dataset_size}'.format(dataset_size=len(data)))
    x, y = feature_target_split(data)
    output_dir_path = Path(arguments.output_dir)
    output_dir_path.mkdir(exist_ok=True, parents=True)
    x.to_csv(os.path.join(output_dir_path, "data.csv"), index=False)
    y.to_csv(os.path.join(output_dir_path, "target.csv"), index=False)
    logging.info('Dataset Downloaded')


def kaggle_download(output_dir: str):
    os.system("kaggle datasets download --unzip ronitf/heart-disease-uci --path data")
    print(os.listdir())
    data = pd.read_csv("data/heart.csv")
    data = data.iloc[random.sample(list(data.index), 150)]
    return data


def feature_target_split(df: pd.DataFrame) -> Tuple:
    x = df.drop(columns='target')
    y = df['target']
    return x, y


def main():
    arguments = parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
