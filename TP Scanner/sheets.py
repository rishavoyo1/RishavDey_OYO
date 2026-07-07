import oyoms as om
import pandas as pd
from datetime import datetime

# =====================================
# CONFIG
# =====================================

USER_EMAIL = "rishav.dey1@oyorooms.com"

EXCEL_LINK = "https://oyoenterprise-my.sharepoint.com/:x:/r/personal/rishav_dey1_oyorooms_com/_layouts/15/Doc.aspx?sourcedoc=%7B8B74D613-B7E8-4720-8335-51AC2BE3F082%7D&file=Book.xlsx&action=editnew&mobileredirect=true&wdPreviousSession=c33c55c4-b724-7da3-4540-f8c22346c63d&wdNewAndOpenCt=1783371192173&wdo=4&wdOrigin=wacFileNew&wdPreviousCorrelation=c48526b1-3ae2-4f58-84a5-ea0762c335d2&wdnd=1"

SHEET_NAME = "Dump"

# =====================================
# CONNECT
# =====================================

wb = om.WorkbookClient(
    USER_EMAIL,
    EXCEL_LINK
)

# =====================================
# FUNCTION
# =====================================

def append_submission(booking, name, email, trustpilot_link):

    df = pd.DataFrame([{
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Booking ID": booking,
        "Guest Name": name,
        "Email": email,
        "Trustpilot Link": trustpilot_link
    }])

    wb.append_data(
        sheet_name=SHEET_NAME,
        df=df,
        include_header=False
    )