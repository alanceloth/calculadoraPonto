from datetime import datetime, timedelta
import sqlite3

def calculate_exit_time(enter_time: str, lunch_time: str, return_from_lunch_time: str) -> str:
    # Convert strings to datetime objects
    enter_time_dt = datetime.strptime(enter_time, '%H:%M')
    lunch_time_dt = datetime.strptime(lunch_time, '%H:%M')
    return_from_lunch_time_dt = datetime.strptime(return_from_lunch_time, '%H:%M')

    # Calculate lunch duration
    lunch_duration = return_from_lunch_time_dt - lunch_time_dt

    # Calculate total time until now
    total_time_until_now = (lunch_time_dt - enter_time_dt) + (datetime.now() - return_from_lunch_time_dt)

    # Calculate remaining time for 8 hours of work
    remaining_time = timedelta(hours=8) - total_time_until_now

    # Calculate time to clock out
    exit_time = datetime.now() + remaining_time

    # Format and return the results
    duration_str = f"Your total lunch duration was: {lunch_duration}"
    exit_time_str = f"You can clock out at: {exit_time.strftime('%H:%M')}"

    return duration_str, exit_time_str

# Function to create a new user in the database
def create_new_user(username, email, password):
    """
    Create a new user in the database.

    Parameters:
    - username (str): The username of the new user.
    - email (str): The email of the new user.
    - password (str): The password of the new user.
    """
    # Connect to the database (assuming you have a SQLite database file named 'users.db')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Insert the new user into the database
    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()


# Function to get the user's email from the database
def get_user_email(username):
    """
    Retrieve the email of a user from the database.

    Parameters:
    - username (str): The username of the user.

    Returns:
    - email (str): The email of the user if found, otherwise None.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Retrieve the email of the user with the provided username
    c.execute('SELECT email FROM users WHERE username=?', (username,))
    result = c.fetchone()

    conn.close()

    if result:
        return result[0]  # Return the email if found
    else:
        return None  # Return None if the user is not found
    
    
# Function to authenticate the user in the database
def authenticate_user(username, password):
    """
    Authenticate the user in the database.

    Parameters:
    - username (str): The username provided by the user.
    - password (str): The password provided by the user.

    Returns:
    - bool: True if the credentials are valid, False otherwise.
    """
    # Connect to the database (assuming you have a SQLite database file named 'users.db')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Query the database to check if the provided username and password match a valid user
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    # Close the database connection
    conn.close()

    # If a user with the provided credentials is found, return True; otherwise, return False
    if user:
        return True
    else:
        return False

# Function to save the user's record in the database
def save_record(username, record):
    """
    Save the user's record in the database.

    Parameters:
    - username (str): The username of the user.
    - record (str): The record to be saved in the database.
    """
    # Connect to the database (assuming you have a SQLite database file named 'users.db')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Insert the record into the database
    c.execute('INSERT INTO records (username, record, timestamp) VALUES (?, ?, ?)', (username, record, datetime.now()))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Function to retrieve the user's record history from the database
def get_user_records(username):
    """
    Retrieve the user's record history from the database.

    Parameters:
    - username (str): The username of the user.

    Returns:
    - list: A list of tuples containing the records retrieved from the database.
    """
    # Connect to the database (assuming you have a SQLite database file named 'users.db')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Query the database to retrieve the user's records
    c.execute('SELECT timestamp, record FROM records WHERE username=? ORDER BY timestamp DESC', (username,))
    records = c.fetchall()

    # Close the database connection
    conn.close()

    return records

# Function to delete a record from the database
def delete_record(username, timestamp):
    """
    Delete a record from the database.

    Parameters:
    - username (str): The username of the user.
    - timestamp (str): The timestamp of the record to be deleted.

    Returns:
    - bool: True if the record was successfully deleted, False otherwise.
    """
    # Connect to the database (assuming you have a SQLite database file named 'users.db')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Check if the record exists before deleting it
    c.execute('SELECT * FROM records WHERE username=? AND timestamp=?', (username, timestamp))
    record = c.fetchone()
    if record:
        # Delete the record from the database
        c.execute('DELETE FROM records WHERE username=? AND timestamp=?', (username, timestamp))
        
        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
        
        return True
    else:
        # Record not found, return False
        conn.close()
        return False
