import streamlit as st
from backend import calculate_exit_time, save_record, get_user_records, delete_record

def run_calculate_page(username):
    st.title("Calculate Page")
    st.sidebar.write(f"Logged in as: {st.session_state.username}")

    # If the user is authenticated
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

        # Save the user's record in the database
        record = f"Enter Time: {enter_time}, Lunch Time: {lunch_time}, Return from Lunch Time: {return_from_lunch_time}, Exit Time: {exit_time_str}"
        save_record(username, record)

    # # Display user's record history
    # if st.button("Show History"):
    #     records = get_user_records(username)
    #     for idx, (timestamp, record) in enumerate(records):
    #         st.write(f"Id: {idx}, Timestamp: {timestamp}, Record: {record}")
    #         if st.button(f"Delete", key=timestamp):  # Use unique key for each delete button
    #             print(timestamp)
    #             if delete_record(username, timestamp):
    #                 st.success("Record deleted successfully!")
    #             else:
    #                 st.error("Failed to delete record.")


    # # Display user's record history
    # if st.button("Show History"):
    #     records = get_user_records(username)
        
    #     # Lista para armazenar os registros selecionados para exclusão
    #     records_to_delete = []
        
    #     for idx, (timestamp, record) in enumerate(records):
    #         # Exibir o registro
    #         st.write(f"Id: {idx}, Timestamp: {timestamp}, Record: {record}")

    #         # Verificar se o usuário selecionou este registro para exclusão
    #         if st.checkbox(f"Delete", key=timestamp):
    #             print(records_to_delete)
    #             records_to_delete.append((timestamp, record))  # Adicionar o registro à lista
        
    #     # Botão para excluir os registros selecionados
    #     if st.button("Delete Selected"):
    #         # Processar os registros a serem excluídos
    #         for timestamp, record in records_to_delete:
    #             if delete_record(username, timestamp):
    #                 st.success("Record deleted successfully!")
    #             else:
    #                 st.error("Failed to delete record.")



