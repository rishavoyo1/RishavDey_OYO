import streamlit as st
from trustpilot import generate_invitation_link
from sheets import append_submission

st.set_page_config(
    page_title="Leave a Review",
    page_icon="⭐",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.block-container{
    max-width:620px;
    padding-top:2rem;
    padding-bottom:3rem;
}

.logo{
    display:flex;
    justify-content:center;
    margin-bottom:20px;
}

h1{
    text-align:center;
    color:#143D2A;
    font-size:38px;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    color:#666666;
    font-size:17px;
    margin-bottom:35px;
    line-height:1.5;
}

.stTextInput>div>div>input{
    border-radius:10px;
}

.stButton>button{
    width:100%;
    height:52px;
    border:none;
    border-radius:10px;
    background:#00B67A;
    color:white;
    font-size:18px;
    font-weight:600;
}

.stButton>button:hover{
    background:#009966;
    color:white;
}

.footer{
    margin-top:50px;
    text-align:center;
    color:#888888;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Logo
# -----------------------------
st.markdown("""
<div class="logo">
<img src="https://www.dancenter.dk/pubweb/graphics/static/bgid=55/bsk=LD3FRZC4/fdmd5=9d372f6dea4ea3d7f8cb227d470b619e/design5-salesrel-logo.svg" width="260">
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Heading
# -----------------------------
st.markdown(
    "<h1>Leave a Review on Trustpilot ⭐</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="subtitle">
Fill in your details to continue.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Inputs
# -----------------------------
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

# -----------------------------
# Submit Button
# -----------------------------
submit = st.button(
    "Submit",
    use_container_width=True
)

# -----------------------------
# Submit Logic
# -----------------------------
if submit:

    if not booking or not name or not email:
        st.error("Please fill in all the required fields.")
        st.stop()

    with st.spinner("Generating your review invitation..."):

        trustpilot_link = generate_invitation_link(
            booking,
            name,
            email
        )

        append_submission(
            booking,
            name,
            email,
            trustpilot_link
        )

    st.success("✅ Details submitted successfully.")

    st.link_button(
        "⭐ Continue to Trustpilot",
        trustpilot_link,
        use_container_width=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
Thank you for choosing <b>DanCenter</b> ❤️
</div>
""", unsafe_allow_html=True)
