import streamlit as st
from backend import calculate_exit_time

def run_frontend():
    st.title("Work Time Calculator")

    st.text("Enter Time (HH:MM)")
    enter_time = st.text_input(" ", value='09:00')
    st.text("Lunch Time (HH:MM)")
    lunch_time = st.text_input(" ", value='12:00')
    st.text("Return from Lunch Time (HH:MM)")
    return_from_lunch_time = st.text_input(" ", value='13:30')

    if st.button("Calculate"):
        duration_str, exit_time_str = calculate_exit_time(enter_time, lunch_time, return_from_lunch_time)
        st.write(duration_str)
        st.write(exit_time_str)

if __name__ == "__main__":
    run_frontend()
