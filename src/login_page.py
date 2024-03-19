import streamlit as st
from backend import authenticate_user
import re

def is_valid_email(email):
    # Expressão regular para validar email
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def run_login_page() -> str:
    st.title("Login Page")

    st.header("Login")
    username = st.text_input("Username:")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        if not is_valid_email(email):
            st.error("Invalid email format")
        elif authenticate_user(username, password):
            st.success("Login successful!")
            return username
        else:
            st.error("Invalid username or password")

