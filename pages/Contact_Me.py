import streamlit as st
import send_email as semail

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address", placeholder="Enter your email...")
    message = st.text_area("Your message", placeholder="Enter your message...")
    button = st.form_submit_button()
    if button:
        semail.send_email(user_email, message)
        st.success("Your email was sent successfully!")

