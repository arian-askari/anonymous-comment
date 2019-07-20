import os
import sys
from utils.file_utils import FileUtils


def load_project_config():
    """Loads nordlys config file. If local file is provided, global one is ignored."""
    config_path = os.sep.join([PROJECT_DIR, "config", "config.ini"])
    try:
        if os.path.exists(config_path):
            return FileUtils.load_config(config_path)
    except Exception as e:
        print("Error loading config file: ", e)
        sys.exit(1)


# global variables

# DIRs
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.sep.join([PROJECT_DIR, "data"])

# config for data

DATASET_PATH_ORIGINAL = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["original"]]
)

DATASET_PATH_A_GOOGLE_USER = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["a_google_user"]]
)

DATASET_PATH_ONE_TO_ONE = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["one_to_one"]]
)

DATASET_PATH_MACHINE_TRANSLATION = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["machine_translation"]]
)

DATASET_PATH_OBFUSCATE = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["obfuscate"]]
)

GREEDY_DATASET_PATH = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["random"]]
)

RANDOM_DATASET_PATH = os.sep.join(
    [DATA_DIR, load_project_config()["dataset"]["greedy"]]
)


# config for algorithms - one-to-one

ONE_TO_ONE_RETRY_NUMBER = int(
    load_project_config()["one_to_one"]["retry_number"]
)

ONE_TO_ONE_PERCENTAGE = int(
    load_project_config()["one_to_one"]["retry_number"]
)
ONE_TO_ONE_MOST_FREQUENT_WORD_PER_USER = int(
    load_project_config()["one_to_one"]["most_frequent_word_per_user"]
)
