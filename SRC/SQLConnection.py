import mysql.connector

try:
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Obaid.2004",
        database="Trucking"
    )

    if connection.is_connected():
        print("Connected to MySQL Trucking database")

    # Open a cursor to execute queries
    cursor = connection.cursor()

    # Read SQL file containing INSERT statements
    with open("populate_tables.sql", "r") as f:
        sql_script = f.read()
        # Split the file contents into individual statements
        statements = sql_script.split(";")

        for statement in statements:
            if statement.strip():  # Only execute non-empty statements
                try:
                    cursor.execute(statement + ";")  # Add semicolon back for each statement
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                else:
                    print("Successfully executed an insert statement.")

    # Commit all transactions to save the changes
    connection.commit()
    print("Data population complete and committed to the database.")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")
