import os
import yaml
import logging.config
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from pandas_profiling import ProfileReport

from heart_disease.data import read_data

DEFAULT_DATASET = "./data/raw/heart.csv"
DEFAULT_CONFIG = '.configs/make_report_config.yaml'
DEFAULT_REPORT = 'reports/data_report.html'

APPLICATION_NAME = "make_report"
DEFAULT_LOGGING_CONF_FILEPATH = "./configs/logging.conf.yml"
logger = logging.getLogger(APPLICATION_NAME)


def make_profile(arguments):
    logger.info("Starting make report...")
    data = read_data(arguments.dataset_filepath)
    prof = ProfileReport(data, title='Pandas Profiling Report', explorative=True)
    prof.to_file(arguments.output_filepath)
    logger.info(f"Saving report in {arguments.output_filepath}")


def setup_logging(filepath=DEFAULT_LOGGING_CONF_FILEPATH):
    """Setup logging configurations from file"""
    with open(filepath) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))


def setup_parser(parser):
    """Function for setup the parser"""
    parser.add_argument(
        "-d", "--dataset", dest="dataset_filepath",
        help="Path to dataset to load, default path is %(default)s",
        metavar='DATASET', default=DEFAULT_DATASET,
    )
    parser.add_argument(
        "-c", "--config", dest="config_filepath",
        help="Path to configfile to load, default path is %(default)s",
        metavar='CONFIG', default=DEFAULT_CONFIG,
    )
    parser.add_argument(
        "-o", "--output", dest="output_filepath",
        help="Path to save report, default path is %(default)s",
        metavar='REPORT', default=DEFAULT_REPORT,
    )
    parser.set_defaults(callback=make_profile)


def main() -> None:
    """Main function of the module"""
    os.makedirs("logs", exist_ok=True)
    setup_logging()
    parser = ArgumentParser(
        prog="make-report",
        description="This app allows you to make report Heart Disease UCI dataset",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
