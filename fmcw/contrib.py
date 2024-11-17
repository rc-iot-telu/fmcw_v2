from pathlib import Path


# Predefined path to make it easy pointing a directory
ROOT_PATH = Path(__file__).resolve().parent
DB_PATH = ROOT_PATH.joinpath("db/")

# Chosen Style
CARD_STYLE = "flat bordered"


def set_port(port_number: str) -> None:
    with open(DB_PATH.joinpath("settings.dat"), "wb") as f:
        pass
