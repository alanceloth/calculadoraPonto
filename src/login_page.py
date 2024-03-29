import streamlit as st
from backend import authenticate_user, get_user_email


def run_login_page() -> (str, str):
    st.title("Login Page")

    st.header("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            user_email = get_user_email(username)
            if user_email:
                return username, user_email
            else:
                st.error("Failed to retrieve user's email")
                return None, None
        else:
            st.error("Invalid username or password")
            return None, None
    return None, None  # Handle case when button is not clicked