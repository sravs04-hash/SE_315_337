import mysql.connector

def check_duplicate_pay_id():
    try:
        # Connect to the gym database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sravani2004",
            database="gym"
        )
        cursor = connection.cursor()

        # Step 1: Input Payment details and validate the amount
        pay_id1 = input("Enter unique Pay ID for the first payment: ").strip()
        gym_id1 = input("Enter gym ID for the first payment: ").strip()
        
        while True:
            amount1 = input("Enter amount for the first payment: ").strip()
            if amount1.isdigit() and int(amount1) >= 1000:
                break
            else:
                print("Error: The basic amount should be at least 1000. Please enter a valid amount.")

        cursor.execute("""
            INSERT INTO payment (pay_id, amount, gym_id)
            VALUES (%s, %s, %s)
        """, (pay_id1, amount1, gym_id1))

        connection.commit()
        print(f"Payment record with pay_id '{pay_id1}' inserted successfully.")

        # Step 2: Attempt to Insert Another Record with the Same pay_id
        pay_id2 = input("Enter Pay ID for the second payment (duplicate pay_id to test): ").strip()
        gym_id2 = input("Enter gym ID for the second payment: ").strip()

        while True:
            amount2 = input("Enter amount for the second payment: ").strip()
            if amount2.isdigit() and int(amount2) >= 1000:
                break
            else:
                print("Error: The basic amount should be at least 1000. Please enter a valid amount.")

        try:
            cursor.execute("""
                INSERT INTO payment (pay_id, amount, gym_id)
                VALUES (%s, %s, %s)
            """, (pay_id2, amount2, gym_id2))
            connection.commit()
            print(f"Payment record with pay_id '{pay_id2}' inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Duplicate payment attempt with pay_id '{pay_id2}' was blocked.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the test case
check_duplicate_pay_id()
