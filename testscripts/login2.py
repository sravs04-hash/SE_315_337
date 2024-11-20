import sqlite3

# Function to set up the database and create the login table
def setup_database():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # Create login table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS login (
            uname TEXT PRIMARY KEY,
            pwd TEXT NOT NULL
        )
    ''')
    
    # Insert a test user (optional)
    cursor.execute("INSERT OR IGNORE INTO login (uname, pwd) VALUES ('member1', 'password1')")
    
    conn.commit()
    conn.close()

# Function to register a new user
def register_user(uname, pwd):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO login (uname, pwd) VALUES (?, ?)", (uname, pwd))
        conn.commit()
        print("User  registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

# Function to log in a user
def login_user(uname, pwd):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM login WHERE uname=? AND pwd=?", (uname, pwd))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Main function to run the program
def main():
    setup_database()  # Ensure the database and table are set up
    
    # Register a new user
    while True:
        register_choice = input("Do you want to register a new user? (yes/no): ").strip().lower()
        if register_choice == 'yes':
            uname = input("Enter a username: ")
            pwd = input("Enter a password: ")
            register_user(uname, pwd)
        elif register_choice == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    # Attempt to log in
    uname = input("Enter username to log in: ")
    pwd = input("Enter password: ")
    login_user(uname, pwd)

if __name__ == "__main__":
    main()