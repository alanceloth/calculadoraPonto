import streamlit as st
from backend import calculate_exit_time, save_record, get_user_calendar_id, delete_record
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import os
import pickle
from datetime import datetime, timedelta
from urllib.parse import unquote


# Defina as permissões necessárias para acessar o calendário do usuário
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    # Check if token.pickle file exists
    if os.path.exists('token.pickle'):
        # Load credentials from token file
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If credentials are missing, expired, or invalid, try to refresh or load from environment variables
    if not creds or not creds.valid:
        # If credentials exist and are expired, refresh them
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Load credentials from environment variables
            service_account_info = {
                "type": os.environ.get("GOOGLE_TYPE"),
                "project_id": os.environ.get("GOOGLE_PROJECT_ID"),
                "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID"),
                "private_key": os.environ.get("GOOGLE_PRIVATE_KEY").replace('\\n', '\n'),
                "client_email": os.environ.get("GOOGLE_CLIENT_EMAIL"),
                "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
                "auth_uri": os.environ.get("GOOGLE_AUTH_URI"),
                "token_uri": os.environ.get("GOOGLE_TOKEN_URI"),
                "auth_provider_x509_cert_url": os.environ.get("GOOGLE_AUTH_PROVIDER_CERT_URL"),
                "client_x509_cert_url": os.environ.get("GOOGLE_CLIENT_CERT_URL")
            }
            # Create credentials from service account info
            creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    # Return Google Calendar API service
    return build('calendar', 'v3', credentials=creds)


def send_calendar_event(username, exit_time):
    # Autentica e autoriza a aplicação
    service = authenticate_google_calendar()

    # Adiciona a data atual ao exit_time e converte para o formato necessário (YYYY-MM-DDTHH:MM:SS.MMMZ)
    current_date = datetime.now().strftime('%Y-%m-%d')
    formatted_exit_time = f"{current_date}T{exit_time}:00.000Z"  # Adiciona segundos e milissegundos e inclui o Z para indicar UTC
    exit_time_with_timezone = (datetime.strptime(formatted_exit_time, '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(hours=3)).strftime('%Y-%m-%dT%H:%M:%S.000Z')

    # Define o corpo do evento
    event = {
        'summary': 'Exit Time',
        'description': 'Time to leave work',
        'start': {
            'dateTime': exit_time_with_timezone,
            'timeZone': 'America/Sao_Paulo',  # Substitua pela timezone do usuário, se necessário
        },
        'end': {
            'dateTime': (datetime.strptime(exit_time_with_timezone, '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(minutes=5)).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            'timeZone': 'America/Sao_Paulo',  # Substitua pela timezone do usuário, se necessário
        },
    }

    # Insere o evento no calendário do usuário
    calendar_id = get_user_calendar_id(username)  # ID do calendário padrão do usuário

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    os.write(1, f'Event created: {event.get("htmlLink")}\n'.encode())




# Função para enviar um e-mail ao usuário
def send_email(email, exit_time):
    # Lógica para enviar um e-mail ao usuário com o horário de saída
    pass

def run_calculate_page(username, user_email):
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
        duration_str, exit_time_str, exit_time_clock = calculate_exit_time(enter_time, lunch_time, return_from_lunch_time)
        st.write(duration_str)
        st.write(exit_time_str)

        # Save the user's record in the database
        record = f"Enter Time: {enter_time}, Lunch Time: {lunch_time}, Return from Lunch Time: {return_from_lunch_time}, Exit Time: {exit_time_str}"
        save_record(username, record)

        # Enviar evento para o calendário
        send_calendar_event(username, exit_time_clock)

        # Enviar e-mail ao usuário
        #send_email(user_email, exit_time_str)

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



