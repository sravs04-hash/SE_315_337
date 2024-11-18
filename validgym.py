import mysql.connector

def valid_gym_insertion():
    try:
        # Connect to the gym database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sravani2004",
            database="gym"
        )
        cursor = connection.cursor()

        # Input Gym details
        gym_id = input("Enter Gym ID: ").strip()
        gym_name = input("Enter Gym Name: ").strip()
        address = input("Enter Gym Address: ").strip()
        gym_type = input("Enter Gym Type (e.g., 'Yoga', 'Fitness', etc.): ").strip()

        # Check if any field is empty
        if not gym_id or not gym_name or not address or not gym_type:
            print("Test case failed: One or more required fields are empty.")
            return  # Return early if a field is empty

        # Insert Gym Record
        cursor.execute("""
            INSERT INTO gym (gym_id, gym_name, address, type)
            VALUES (%s, %s, %s, %s)
        """, (gym_id, gym_name, address, gym_type))

        connection.commit()
        print(f"Test case passed: Gym record with gym_id '{gym_id}' inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Test case failed: Error - {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function to test gym record insertion
valid_gym_insertion()
