import mysql.connector

def add_trainer():
    try:
        # Connect to the gym database
        connection = mysql.connector.connect(
            host="localhost",       # Update with your MySQL host
            user="root",            # Update with your MySQL username
            password="Sravani2004",    # Update with your MySQL password
            database="gym"          # Ensure this matches the name of your gym database
        )
        cursor = connection.cursor()

        # Asking user for trainer details
        print("\nEnter Trainer Details:")
        trainer_id = input("Trainer ID (e.g., T9): ").strip()
        name = input("Name: ").strip()
        time = input("Time (e.g., 5:00 AM): ").strip()
        mobileno = input("Mobile Number: ").strip()
        pay_id = input("Payment ID (e.g., Payment9): ").strip()

        # Validate inputs
        if not trainer_id or not name or not time or not mobileno or not pay_id:
            print("Test Case Failed: Missing details. All fields are required!")
            return

        if not mobileno.isdigit() or len(mobileno) != 10:
            print("Test Case Failed: Invalid mobile number. It must be a 10-digit number.")
            return

        # Insert data into the trainer table
        insert_query = """
        INSERT INTO trainer (trainer_id, name, time, mobileno, pay_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (trainer_id, name, time, mobileno, pay_id))
        connection.commit()

        print("Trainer added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function
if __name__ == "__main__":
    add_trainer()
