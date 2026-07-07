import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES,
)

client = gspread.authorize(creds)

sheet = client.open("TP Scanner").worksheet("Dump")


def append_submission(booking, name, email, trustpilot_link):

    sheet.append_row([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        booking,
        name,
        email,
        trustpilot_link
    ])
