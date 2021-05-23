import os
import logging
import typing

import hydra
import pandas as pd
from omegaconf import DictConfig, OmegaConf
from pandas_profiling import ProfileReport

from ..data import read_data
from ..entities import ReportConfig
from ..utils import setup_logging, construct_abs_path

APPLICATION_NAME = "make_report"
logger = logging.getLogger(APPLICATION_NAME)


def make_profile(config: ReportConfig) -> None:

    logger.info("Starting make report...")
    input_dir = construct_abs_path(config.input_data_path)
    logger.info(f"Reading data from {input_dir}")
    data = read_data(input_dir)

    prof = ProfileReport(data, title='Pandas Profiling Report', explorative=True)
    output_dir = construct_abs_path(config.dir)
    os.makedirs(output_dir, exist_ok=True)

    output_filepath = os.path.join(output_dir, config.filename)
    prof.to_file(output_filepath)
    logger.info(f"Saving report in {output_filepath}")

    logger.info("Ending make report.")


@hydra.main(config_path='../configs', config_name='config')
def main(cfg: DictConfig) -> None:
    """Main function of the module"""
    os.makedirs("logs", exist_ok=True)
    setup_logging(cfg.logger)
    make_profile(typing.cast(ReportConfig, cfg.report))


if __name__ == "__main__":
    main()
