import streamlit as st

from trustpilot import generate_invitation_link
from sheets import append_submission

st.set_page_config(
    page_title="Leave a Review",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.block-container{
    max-width:520px;
    padding-top:0.6rem;
    padding-bottom:0.6rem;
}

.logo{text-align:center;margin-bottom:10px;}
.logo img{width:180px;max-width:80%;}

h1{
    text-align:center;
    color:#123D2C;
    font-size:30px;
    margin:0;
}

.subtitle{
    text-align:center;
    color:#666;
    font-size:15px;
    margin:8px 0 22px 0;
    line-height:1.45;
}

.stTextInput input{
    border-radius:10px;
}

.stButton>button{
    width:100%;
    height:48px;
    border:none;
    border-radius:10px;
    background:#00B67A;
    color:white;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover{
    background:#009966;
    color:white;
}

.redirect{
    text-align:center;
    margin-top:18px;
    color:#00B67A;
    font-size:18px;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="logo">
<img src="https://www.dancenter.dk/pubweb/graphics/static/bgid=55/bsk=LD3FRZC4/fdmd5=9d372f6dea4ea3d7f8cb227d470b619e/design5-salesrel-logo.svg">
</div>
""", unsafe_allow_html=True)

st.markdown("<h1>Leave a Review on Trustpilot ⭐</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Your feedback helps us improve our services and provide an even better stay experience.
</div>
""", unsafe_allow_html=True)

with st.form("review_form"):

    booking = st.text_input(
        "Booking ID",
        placeholder="Enter your booking ID"
    )

    name = st.text_input(
        "Guest Name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email address"
    )

    submit = st.form_submit_button("Submit Review")


if submit:

    if booking and name and email:

        link = generate_invitation_link(
            booking,
            name,
            email
        )

        append_submission(
            booking,
            name,
            email,
            link
        )

        st.markdown(
            """
            <div class="redirect">
                Redirecting to Trustpilot...
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <meta http-equiv="refresh" content="2;url={link}">
            """,
            unsafe_allow_html=True,
        )

    else:
        st.error("Please fill in all fields.")
