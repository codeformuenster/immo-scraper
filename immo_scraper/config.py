""" Utils related to config. """

import json5

from immo_scraper import paths


def read_config() -> dict:
    with open(str(paths.CONFIG_JSON5), "r") as f:
        return json5.load(f)
