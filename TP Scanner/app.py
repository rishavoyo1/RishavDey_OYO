import streamlit as st
from trustpilot import generate_invitation_link
from sheets import append_submission
st.set_page_config(page_title="Leave a Review",page_icon="⭐",layout="centered")
st.markdown("<style>.block-container{max-width:650px;padding-top:2rem}.stButton>button{background:#00B67A;color:white}</style>",unsafe_allow_html=True)
st.title("⭐ Leave a Review")
booking=st.text_input("Booking ID")
name=st.text_input("Full Name")
email=st.text_input("Email")
if st.button("Continue"):
    if booking and name and email:
        link=generate_invitation_link(booking,name,email)
        append_submission(booking,name,email,link)
        st.success("Redirecting...")
        st.markdown(f'<meta http-equiv="refresh" content="1;url={link}">',unsafe_allow_html=True)
        st.link_button("Open Trustpilot",link)
    else:
        st.error("Fill all fields")
