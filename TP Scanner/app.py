import streamlit as st
import streamlit.components.v1 as components

from trustpilot import generate_invitation_link
from sheets import append_submission

st.set_page_config(
    page_title="Leave a Review",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    max-width:520px;
    padding-top:0.8rem;
    padding-bottom:0.8rem;
}

h1{
    margin:0;
    padding:0;
    font-size:34px;
    font-weight:700;
    color:#173D2C;
    text-align:center;
}

.subtitle{
    text-align:center;
    color:#6b6b6b;
    font-size:15px;
    line-height:1.45;
    margin-top:8px;
    margin-bottom:22px;
}

.logo{
    text-align:center;
    margin-bottom:10px;
}

.logo img{
    width:180px;
}

.stTextInput label{
    font-weight:600;
}

.stTextInput input{
    border-radius:10px;
    height:46px;
}

.stButton>button{
    width:100%;
    height:48px;
    border-radius:10px;
    border:none;
    background:#00B67A;
    color:white;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover{
    background:#009966;
    color:white;
}

.success{
    background:#F2FFF8;
    border:1px solid #00B67A;
    padding:18px;
    border-radius:12px;
    text-align:center;
    margin-top:15px;
}

.success h3{
    margin-bottom:8px;
    color:#0C5C38;
}

.manual{
    margin-top:15px;
}

.small{
    text-align:center;
    color:#888;
    font-size:13px;
    margin-top:18px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOGO
# --------------------------------------------------

st.markdown("""
<div class="logo">
<img src="https://www.dancenter.dk/pubweb/graphics/static/bgid=55/bsk=LD3FRZC4/fdmd5=9d372f6dea4ea3d7f8cb227d470b619e/design5-salesrel-logo.svg">
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    "<h1>Leave a Review on Trustpilot ⭐</h1>",
    unsafe_allow_html=True,
)

st.markdown("""
<div class="subtitle">
Your feedback helps us improve our services and provide an even better stay experience.
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FORM
# --------------------------------------------------

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
        placeholder="Enter your email"
    )

    submit = st.form_submit_button("Submit Review")

# --------------------------------------------------
# SUBMIT
# --------------------------------------------------

if submit:

    if not booking or not name or not email:
        st.error("Please fill in all the fields.")

    else:

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

        st.markdown("""
        <div class="success">
        <h3>✅ Redirecting to Trustpilot...</h3>

        Thank you for taking a moment to share your experience.
        <br>
        You will be redirected automatically in a few seconds.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='manual'>", unsafe_allow_html=True)
        st.link_button("Open Trustpilot Now", link)
        st.markdown("</div>", unsafe_allow_html=True)

        components.html(
            f"""
            <script>
            setTimeout(function(){{
                window.location.href="{link}";
            }},2000);
            </script>
            """,
            height=0,
        )

st.markdown("""
<div class="small">
Thank you for choosing DanCenter ❤️
</div>
""", unsafe_allow_html=True)
