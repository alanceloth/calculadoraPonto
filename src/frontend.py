import streamlit as st
import register_page
import login_page
import calculate_page
from dba import create_database

# Inicializando a variável username na sessão
st.session_state.username = None

def main():
    create_database()
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", options=["Register", "Login", "Calculate"])

    if selected_page == "Register":
        register_page.run_register_page()

    elif selected_page == "Login":
        st.session_state.username = login_page.run_login_page()

    elif selected_page == "Calculate":
        # Verifica se há um nome de usuário armazenado na sessão
        if st.session_state.username:
            calculate_page.run_calculate_page(st.session_state.username, st.session_state.email)
        else:
            st.error("Please login first to access this page.")

    if st.session_state.get("logged_in", False):
        st.sidebar.write(f"Logged in as: {st.session_state.username}")
        
if __name__ == "__main__":
    main()
