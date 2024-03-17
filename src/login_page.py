import streamlit as st
from backend import authenticate_user

def run_login_page() -> str:
    st.title("Login Page")

    st.header("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            return username
        else:
            st.error("Invalid username or password")