import streamlit as st
from trustpilot import generate_invitation_link
from sheets import append_submission

st.set_page_config(
    page_title="Leave a Review",
    page_icon="⭐",
    layout="centered"
)

st.markdown("""
<style>
.block-container {
    max-width: 650px;
    padding-top: 2rem;
}
.stButton > button {
    background: #00B67A;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("⭐ Leave a Review")

with st.form("review_form"):
    booking = st.text_input("Booking ID")
    name = st.text_input("Full Name")
    email = st.text_input("Email")

    submitted = st.form_submit_button("Submit")

if submitted:
    if booking and name and email:
        try:
            # Generate Trustpilot link
            link = generate_invitation_link(booking, name, email)

            # Save submission
            append_submission(booking, name, email, link)

            st.success("Redirecting to Trustpilot...")

            st.markdown(
                f"""
                <script>
                    setTimeout(function() {{
                        window.location.href = "{link}";
                    }}, 2000);
                </script>
                """,
                unsafe_allow_html=True,
            )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please fill all fields.")
