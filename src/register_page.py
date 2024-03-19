import streamlit as st
import re
from backend import create_new_user

def is_valid_email(email):
    # Expressão regular para validar email
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def run_register_page():
    st.title("Registration Page")

    st.header("New User Registration")
    new_username = st.text_input("New Username:", key="new_username_input")
    new_email = st.text_input("New Email:", key="new_email_input")
    new_calendar_id = st.text_input("New Calendar ID:", key="new_calendar_id_input")
    new_password = st.text_input("New Password:", type="password", key="new_password_input")
    
    if st.button("Register New User"):
        if not is_valid_email(new_email):
            st.error("Invalid email format")
        else:
            create_new_user(new_username, new_email, new_calendar_id, new_password)
            st.success("New user registered successfully!")
            return new_username  # Return the registered username
        
    st.text("Tutorial to register new user:")
    st.markdown("1. [Go To](https://calendar.google.com/)")
    st.markdown("2. On the left, next to Other calendars, click Add other calendars")
    st.markdown("3. Add a name and description for your calendar.")
    st.markdown("4. Click Create calendar.")
    st.markdown("5. Click Settings in this calendar.")
    st.markdown("6. Click share with specific people.")
    st.markdown("7. Add this email calculadora-calendario@calculadora-ponto.iam.gserviceaccount.com with writing privileges.")
    st.markdown("8. Copy the calendar ID below the integration area.")
    st.markdown("9. Use the calendar ID in the register form above.")