__version__ = "1.0.0.0"

import rentalunits.db.database
import rentalunits.db.models

import logging.config
import pathlib
import sys
import configparser

import yaml


LOGGING_CONFIG =  pathlib.Path(__file__).parent / "logger_config.yaml"

with open(LOGGING_CONFIG) as f:
    config_dict = yaml.safe_load(f)
    logging.config.dictConfig(config_dict)


# get root loger
def log():
    logger = logging.getLogger(__name__)
    # the __name__ resolve to main since we are at the root of the project

    if sys.gettrace() is not None:
        logger.level = 10

    return logger


def log_config():
    return config_dict


def config():
    config_file = pathlib.Path(__file__).parent / "app_settings.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
    return config
