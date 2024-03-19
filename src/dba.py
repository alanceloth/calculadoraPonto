import sqlite3

# Function to create the database and tables
def create_database():
    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Create 'users' table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

    # Create 'records' table
    c.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    record TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (username) REFERENCES users(username)
                )''')

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Call the function to create the database and tables
if __name__ == "__main__":
    create_database()
