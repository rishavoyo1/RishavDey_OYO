import requests
 
import base64
 
import time
_token = None
 
_expiry = 0
# ---------------------------------
 
# HARDCODE FOR TESTING
 
# ---------------------------------
import streamlit as st

import streamlit as st

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
BUSINESS_UNIT_ID = st.secrets["BUSINESS_UNIT_ID"]

def token():
 
    global _token, _expiry
    if _token and time.time() < _expiry:
 
        return _token
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
 
    encoded = base64.b64encode(credentials.encode()).decode()
    response = requests.post(
 
        "https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken",
 
        headers={
 
            "Authorization": f"Basic {encoded}",
 
            "Content-Type": "application/x-www-form-urlencoded"
 
        },
 
        data={
 
            "grant_type": "client_credentials"
 
        }
 
    )
    print("Status Code:", response.status_code)
 
    print("Response:", response.text)
    response.raise_for_status()
    data = response.json()
    _token = data["access_token"]
 
    _expiry = time.time() + int(data["expires_in"]) - 60
    return _token

def generate_invitation_link(reference, name, email):
    access_token = token()
    response = requests.post(
 
        f"https://invitations-api.trustpilot.com/v1/private/business-units/{BUSINESS_UNIT_ID}/invitation-links",
 
        headers={
 
            "Authorization": f"Bearer {access_token}",
 
            "Content-Type": "application/json"
 
        },
 
        json={
 
            "referenceId": reference,
 
            "email": email,
 
            "name": name,
 
            "locale": "en-US"
 
        }
 
    )
    print("Invitation Status:", response.status_code)
 
    print("Invitation Response:", response.text)
    response.raise_for_status()
    return response.json()["url"]
