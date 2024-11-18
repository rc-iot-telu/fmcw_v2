import pickle

from pathlib import Path


# Predefined path to make it easy pointing a directory
ROOT_PATH = Path(__file__).resolve().parent
DB_PATH = ROOT_PATH.joinpath("db/")

# Chosen Style
CARD_STYLE = "flat bordered"

SETTING_FILE_NAME = "settings.isiot"


def read_setting() -> dict:
    try:
        with open(DB_PATH.joinpath(SETTING_FILE_NAME), "rb") as f:
            settings_data: dict = pickle.load(f)
    except FileNotFoundError:
        settings_data =  {
            "PORT_NUMBER": ""
        }

    return settings_data
