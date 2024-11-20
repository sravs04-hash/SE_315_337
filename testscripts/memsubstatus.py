import mysql.connector

def check_membership_status(mem_id):
    try:
        # Connect to the gym database
        connection = mysql.connector.connect(
            host="localhost",       # Update with your MySQL host
            user="root",            # Update with your MySQL username
            password="Sravani2004",    # Update with your MySQL password
            database="gym"          # Ensure this matches the name of your gym database
        )
        cursor = connection.cursor()

        # Query to get membership package
        query = "SELECT package FROM member WHERE mem_id = %s"
        cursor.execute(query, (mem_id,))
        result = cursor.fetchone()

        if result:
            # Get the package value
            package = result[0]

            # Check if package is numeric and convert to integer for comparison
            if package.isdigit():
                package_value = int(package)
                
                # Simulating expired membership based on package value
                if package_value < 6000:
                    return "Your membership has expired. Please renew it."
                else:
                    return "Your membership is active."
            else:
                return "Invalid package value. Please check the package details."
        else:
            return "Member not found."

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Test the function
mem_id = input("Enter member ID: ")
status_message = check_membership_status(mem_id)
print(status_message)
