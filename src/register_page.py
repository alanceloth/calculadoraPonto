import streamlit as st
from backend import create_new_user

def run_register_page():
    st.title("Registration Page")

    st.header("New User Registration")
    new_username = st.text_input("New Username:", key="new_username_input")
    new_email = st.text_input("New Email:", key="new_email_input")
    new_password = st.text_input("New Password:", type="password", key="new_password_input")
    if st.button("Register New User"):
        create_new_user(new_username,new_email ,new_password)
        st.success("New user registered successfully!")
        return new_username  # Return the registered username
