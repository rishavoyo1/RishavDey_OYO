import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
creds = Credentials.from_service_account_info(
    json.loads(os.environ["GCP_SERVICE_ACCOUNT"]),
    scopes=SCOPES,
)

client = gspread.authorize(creds)

sheet = client.open("TP Scanner").worksheet("Tracking")


def append_submission(booking, name, email, trustpilot_link):

    sheet.append_row([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        booking,
        name,
        email,
        trustpilot_link
    ])
