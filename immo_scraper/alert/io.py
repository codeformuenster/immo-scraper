""" I/O utils related to alerts. """

from typing import Text

from immo_scraper import paths


def get_ids_previous_alerts() -> Text:
    alerts_log = []
    if paths.ALERTS_IDS.exists():
        with open(str(paths.ALERTS_IDS), "r") as f:
            alerts_log = f.read().splitlines()
    return alerts_log


def log_alert(id):
    with open(str(paths.ALERTS_IDS), "a") as f:
        f.write(id + "\n")
