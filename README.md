# Database Setup and Usage Guide

This guide provides instructions on how to set up the database, modify the database name, provide credentials, and run the provided script (`Insertion.py`) to input data into the database.

## Prerequisites

1. **MySQL Server**: Ensure you have a MySQL server installed and running.
2. **Python**: Install Python (version 3.x or above).
3. **Required Python Library**: Install `mysql-connector` for database interaction.

## Steps to Set Up the Database

### 1. Modify the Database Name
In the script, replace the placeholder database name `my_database` with the desired database name. Update the following line accordingly:

```sql
USE my_database;
```

For example, if your database name is `trucking_db`, change it to:

```sql
USE trucking_db;
```

### 2. Input Your MySQL Credentials
When connecting to the database in the script, ensure you input your MySQL username and password in the connection setup. The script should look something like this:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="your_password",
    database="trucking_db"
)
```

Replace `your_password` with your MySQL credentials.

---

### 3. Import the Tables into the Database
Run the SQL schema provided in this guide in your MySQL environment:

1. Open your MySQL Workbench or terminal.
2. Copy the entire SQL schema from this document, `ex2.sql`
3. Paste it into your SQL editor or command line.
4. Execute the script to create all the tables.


## Running the Python Script

### 1. Install Required Python Library
Install the `mysql-connector` library using pip:

```bash
pip install mysql-connector
```

### 2. Execute the Python Script
To populate the database with sample data or perform insert operations, run the `Insertion.py` script:

```bash
python Insertion.py
```

### 3. Database Population Log
After running the script, a new text file named `database_population_log.txt` will be created in the same directory as the script. This file will contain a detailed log of all the data populated into the database, including any success or error messages for each table. 

Example contents of `database_population_log.txt`:

```
2024-11-20 14:08:03,752 - Connected to MySQL Trucking database
2024-11-20 14:08:03,754 - Inserted Driver 1 with driverID 1
...
2024-11-20 14:08:03,972 - Inserted SupplierContactInfo for supplierID 36: Contact Person: John Jones, Contact Number: 7729709344
2024-11-20 14:08:03,973 - Data population complete and committed to the database.
2024-11-20 14:08:03,973 - MySQL connection closed

```
This addition makes it clear that a log file will be generated and explains its purpose. 


## Additional Notes

1. Ensure the database connection details in the `Insertion.py` script match your MySQL setup.
2. Check for any dependencies or additional scripts required for your project to function as intended.
3. Use the `localhost` server unless you have a specific remote database server to connect to.

---
