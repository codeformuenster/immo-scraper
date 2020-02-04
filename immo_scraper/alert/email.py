import logging
from typing import Text

import pandas as pd

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from immo_scraper import config

CONFIG = config.read_config()


def compose_html(df_alerts: pd.DataFrame) -> Text:
    logging.info("Composing email text...")
    text = f"Found {len(df_alerts)} new relevant alerts:</br></br>"
    for id in df_alerts.id:
        link = df_alerts[df_alerts.id == id].lister_url.values[0]
        text += f"- <a href='{link}'>offer</a>.</br>"
    logging.debug(f"Email html: {text}")
    return text


def send(text: Text):
    logging.info("Sending email...")
    message = Mail(
        from_email=CONFIG["email"]["from"],
        to_emails=CONFIG["email"]["to"],
        subject="Immo-scraper: new relevant offer(s).",
        html_content=text,
    )
    try:
        sg = SendGridAPIClient(CONFIG["email"]["token"])
        response = sg.send(message)
        logging.debug(response.status_code)
        logging.debug(response.body)
        logging.debug(response.headers)
    except Exception as e:
        logging.error(e.message)
