import sqlite3

# Function to set up the
#  database and create the subscriptions table
def setup_database():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # Create subscriptions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            mem_id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT NOT NULL,
            duration INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to calculate the price based on the duration
def calculate_price(duration):
    # Define pricing rules
    pricing = {
        1: 10000.00,
        3: 25000.00,
        6: 57000.00,
        12: 100000.00
    }
    return pricing.get(duration, 0.00)  # Default to 0 if duration is invalid

# Function to add a subscription
def add_subscription(exercise, duration):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    try:
        # Validate input
        if not exercise or duration is None:
            print("Test Case Failed: Missing subscription details!")
            return False

        # Calculate price based on duration
        price = calculate_price(duration)
        if price == 0.00:
            print(f"Test Case Failed: Invalid duration '{duration}'!")
            return False

        # Insert subscription into the database
        cursor.execute("INSERT INTO subscriptions (exercise, duration, price) VALUES (?, ?, ?)", 
                       (exercise, duration, price))
        conn.commit()
        print(f"Subscription added successfully! Calculated Price: {price}")
        return True
    except sqlite3.IntegrityError as e:
        print("Error adding subscription:", e)
        return False
    finally:
        conn.close()

# Function to interact with the user for adding subscriptions
def run_test_cases():
    print("Welcome to the Gym Subscription Management System!")
    print("Enter subscription details to add a new subscription. Duration determines price automatically.")

    # Test case loop
    while True:
        exercise = input("Enter Exercise Name (or leave blank): ").strip()
        duration_input = input("Enter Duration in Months (or leave blank): ").strip()

        # Convert duration to integer, or set to None
        duration = int(duration_input) if duration_input.isdigit() else None

        # Run the test case
        result = add_subscription(exercise, duration)
        
        # Display the test case result
        if result:
            print("Test Case Passed: Subscription added successfully.")
        else:
            print("Test Case Failed: Invalid subscription details.")

        # Ask if the user wants to add another subscription or exit
        choice = input("Do you want to add another subscription? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

# Main function
def main():
    setup_database()  # Ensure the database and table are set up
    run_test_cases()  # Run test cases with user input

if __name__ == "__main__":
    main()
