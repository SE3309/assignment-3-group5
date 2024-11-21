import mysql.connector
import random
from datetime import datetime, timedelta
import logging

# Configure logging
log_file = "database_population_log.txt"
logging.basicConfig(filename=log_file, 
                    filemode="w", 
                    level=logging.INFO, 
                    format="%(asctime)s - %(message)s")


# Helper function for random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Define date ranges
start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 1, 1)

try:
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="", # Change this to your MySQL password
        database="my_database"
    )

    if connection.is_connected():
        message = "Connected to MySQL Trucking database"
        print(message)
        logging.info(message)

    # Open a cursor to execute queries
    cursor = connection.cursor()

    # Insert into Driver table
    
    first_names = ['John', 'Jane', 'Alex', 'Chris', 'Taylor', 'Jordan']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    statuses = ['ACTIVE', 'ON LEAVE', 'INACTIVE']
    truck_statuses = ['OWNED', 'ASSIGNED']
    
    driver_ids = []
    random.shuffle(driver_ids)
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Driver (licenseNumber, driverName, homeAddress, yearsOfExperience, numberOfDeliveries, email, age, salary, employmentDate, workingStatus, truckOwnedorAssigned)
        VALUES ('ON{i:010}', '{random.choice(first_names)} {random.choice(last_names)}', 
                '{random.randint(100, 999)} {random.choice(cities)} St.', {random.randint(1, 35)}, 
                {random.randint(50, 2000)}, 'driver{i}@example.com', {random.randint(25, 65)}, 
                {round(random.uniform(35000, 120000), 2)}, '{random_date(start_date, end_date).date()}', 
                '{random.choice(statuses)}', '{random.choice(truck_statuses)}');
        """
        cursor.execute(sql)
        driver_ids.append(cursor.lastrowid)
        message = f"Inserted Driver {i} with driverID {cursor.lastrowid}"
        print(message)
        logging.info(message)

    random.shuffle(driver_ids)
    # Insert into Truck table
    truck_makes = ['Ford', 'Chevrolet', 'Ram', 'Toyota', 'GMC', 'Nissan', 'Mack', 'Kenworth', 'Peterbilt', 'Volvo']
    truck_models = ['F-150', 'Silverado', '1500', 'Tundra', 'Sierra', 'Titan', 'Anthem', 'T680', '579', 'VNL']
    truck_ids = []
    random.shuffle(truck_ids)
    for i, driver_id in enumerate(driver_ids, start=1):
        make = random.choice(truck_makes)
        model = random.choice(truck_models)
        year = random.randint(2010, 2023)
        make_model_year = f"{make} {model} {year}"
        
        sql = f"""
        INSERT INTO Truck (driverID, mileage, licencePlateNumber, VIN, makeModelYear, maxTowWeight, insurancePolicyNo, registration)
        VALUES ({driver_id}, {random.randint(50000, 500000)}, 'TRK{i:04}', '1HGCM82633A{random.randint(100000, 999999)}', 
                '{make_model_year}', {round(random.uniform(5000, 15000), 2)}, 
                {round(random.uniform(100000, 500000), 2)}, '{random_date(start_date, end_date).date()}');
        """
        cursor.execute(sql)
        truck_ids.append(cursor.lastrowid)
        message = f"Inserted Truck {i} with truckID {cursor.lastrowid}"
        print(message)
        logging.info(message)
        

    # Insert into Supplier table
    supplier_types = ['MANUFACTURER', 'DISTRIBUTOR', 'WHOLESALER']
    supplier_ids = []
    random.shuffle(supplier_ids)
    # Generate valid longitude and latitude for suppliers
    for i in range(1, 101):
        longitude = random.uniform(-180.0, 180.0)  # Full range for longitude
        latitude = random.uniform(-90.0, 90.0)    # Full range for latitude
        supplier_type = random.choice(supplier_types)  # Random ENUM type

        sql = f"""
        INSERT INTO Supplier (supplierName, contactPerson, contactName, supplierLongitude, supplierLatitude, supplierType, businessHours)
        VALUES ('Supplier {i}', 'Contact {i}', 'Name {i}', {longitude:.8f}, {latitude:.8f}, '{supplier_type}', '9am-5pm');
        """
        cursor.execute(sql)
        supplier_ids.append(cursor.lastrowid)
        message = f"Inserted Supplier {i} with supplierID {cursor.lastrowid}, Longitude: {longitude:.8f}, Latitude: {latitude:.8f}"
        print(message)
        logging.info(message)


    random.shuffle(supplier_ids)
    random.shuffle(truck_ids)
    # Allowed ENUM values for trailerType
    trailer_types = ['DRY FRIEGHT', 'REFRIGERATED DRY FREIGHT', 'TANK', 'FLATBED', 'AUTO HAULER']
    trailer_makes = ['Utility', 'Great Dane', 'Wabash', 'Hyundai Translead', 'Stoughton']
    trailer_models = ['4000D-X Composite', 'Champion SE', 'Reef Carrier', 'Flatliner', 'Maximizer']
    trailer_ids = []
    random.shuffle(trailer_ids)
    # Insert into Trailer table
    for i, (supplier_id, truck_id) in enumerate(zip(supplier_ids, truck_ids), start=1):
        trailer_type = random.choice(trailer_types)  # Randomly select a valid trailer type
        make = random.choice(trailer_makes)
        model = random.choice(trailer_models)
        year = random.randint(2010, 2023)
        make_model_year = f"{make} {model} {year}"
        trailer_ids.append(cursor.lastrowid)
                
        sql = f"""
        INSERT INTO Trailer (supplierID, truckID, trailerCapacity, maxLoadWeight, trailerLength, trailerType, licensePlateNumber, VIN, makeModelYear, registration)
        VALUES ({supplier_id}, {truck_id}, {random.randint(500, 3000)}, {random.randint(1000, 8000)}, {random.uniform(5.0, 20.0):.2f}, '{trailer_type}', 
                'TRL{i:04}', 'VIN{i:08}', '{make_model_year}', '{random_date(start_date, end_date).date()}');
        """
        cursor.execute(sql)
        message = f"Inserted Trailer {i} with type '{trailer_type}' linked to SupplierID {supplier_id} and TruckID {truck_id}"
        print(message)
        logging.info(message)


    # Insert into Customer table
    store_types = ['CHAIN', 'INDIVIDUAL']
    customer_ids = []
    random.shuffle(customer_ids)
    for i in range(1, 101):
        longitude = random.uniform(-180.0, 180.0)  
        latitude = random.uniform(-90.0, 90.0)    
        store_type = random.choice(store_types)  
        
        sql = f"""
        INSERT INTO Customer (customerLongitude, customerLatitude, customerName, typeOfStore, deliveryInstructions)
        VALUES ({longitude:.6f}, {latitude:.6f}, 'Customer {i}', '{store_type}', 'Leave at back door or {i}');
        """
        cursor.execute(sql)
        customer_ids.append(cursor.lastrowid)
        message = f"Inserted Customer {i} with customerID {cursor.lastrowid}"
        print(message)
        logging.info(message)
        
        
    random.shuffle(supplier_ids)
    random.shuffle(customer_ids)
    random.shuffle(trailer_ids)
    # Insert into Shipment table
    # put something for type of product 
    delivery_types = ['EXPEDITED', 'STANDARD', 'PRIORITY']
    shipment_ids = []
    random.shuffle(shipment_ids)
    for i, (supplier_id, customer_id, trailer_id) in enumerate(zip(supplier_ids, customer_ids, trailer_ids), start=1):
        trailer_id = random.choice(truck_ids)  
        load_weight = random.randint(500, 3000)  
        product_type = f"ProductType {random.randint(1, 20)}"  
        delivery_type = random.choice(delivery_types)  
        shipment_ids.append(cursor.lastrowid)
        
        sql = f"""
        INSERT INTO Shipment (supplierID, customerID, trailerID, loadWeight, typeOfProduct, deliveryType)
        VALUES ({supplier_id}, {customer_id}, {trailer_id}, {load_weight}, '{product_type}', '{delivery_type}');
        """
        cursor.execute(sql)
        message = f"Inserted Shipment {i} linked to SupplierID {supplier_id}, CustomerID {customer_id}"
        print(message)
        logging.info(message)
        logging.info(f"Shipment: SupplierID={supplier_id}, CustomerID={customer_id}, TrailerID={trailer_id}, ShipmentID={cursor.lastrowid}")


    random.shuffle(driver_ids)
    random.shuffle(truck_ids)
    random.shuffle(trailer_ids)
    random.shuffle(shipment_ids)
    # Insert into Route table
    route_ids = []
    for i, (driver_id, truck_id, trailer_id, shipment_id) in enumerate(zip(driver_ids, truck_ids, trailer_ids, shipment_ids), start=1):
        # Generate random pickup location and time
        pickup_longitude = random.uniform(-180, 180)
        pickup_latitude = random.uniform(-90, 90)
        pickup_time = random_date(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S")

        # Construct SQL for insertion
        sql = f"""
        INSERT INTO Route (driverID, shipmentID, truckID, trailerID, pickupLongitude, pickupLattitude, pickupTime)
        VALUES ({driver_id}, {shipment_id}, {truck_id}, {trailer_id}, {pickup_longitude:.6f}, {pickup_latitude:.6f}, '{pickup_time}');
        """
        try:
            cursor.execute(sql)
            route_ids.append(cursor.lastrowid)
            logging.info(f"Inserted Route {i} linked to DriverID={driver_id}, ShipmentID={shipment_id}, TruckID={truck_id}, TrailerID={trailer_id}")
            print(f"Inserted Route {i} linked to DriverID {driver_id}, ShipmentID {shipment_id}, TruckID {truck_id}, TrailerID {trailer_id}")
        except Exception as e:
            logging.error(f"Failed to insert Route {i}: {e}")

    random.shuffle(route_ids)
    # Insert into Trips table using valid route_ids
    for i, route_id in enumerate(route_ids, start=1):
        destination_longitude = random.uniform(-180, 180)
        destination_latitude = random.uniform(-90, 90)
        trip_index = random.randint(1, 15)

        sql = f"""
        INSERT INTO Trips (routeID, destinationLongitude, destinationLatitude, tripIndex)
        VALUES ({route_id}, {destination_longitude:.6f}, {destination_latitude:.6f}, {trip_index});
        """
        try:
            cursor.execute(sql)
            logging.info(f"Inserted Trip linked to RouteID={route_id}")
            print(f"Inserted Trip {i} with RouteID {route_id}")
        except Exception as e:
            logging.error(f"Failed to insert Trip {i}: {e}")
            
     # ProofOfDelivery table
    for route_id in route_ids:
        proof = random.choice([True, False])
        pod_no = f"POD{i:05}"
        sql = f"INSERT INTO ProofOfDelivery (routeID, proofOfDelivery, PODNo) VALUES ({route_id}, {proof}, '{pod_no}');"
        cursor.execute(sql)
        logging.info(f"Inserted ProofOfDelivery for routeID {route_id}: {proof}, {pod_no}")        

    # DriverPhone table
    for driver_id in driver_ids:
        phone_types = ['MOBILE', 'HOME']
        phone_type = random.choice(phone_types)
        phone_number = f"{random.randint(100, 999)}{random.randint(1000000, 9999999)}"
        
        sql = f"INSERT INTO DriverPhone (driverID, phoneNumber, phoneType) VALUES ({driver_id}, '{phone_number}', '{phone_type}');"
        try:
            cursor.execute(sql)
            logging.info(f"Inserted DriverPhone for driverID {driver_id}: {phone_number} ({phone_type})")
        except Exception as e:
            logging.error(f"Failed to insert DriverPhone for driverID {driver_id}: {e}")

    random.shuffle(driver_ids)
    # EmergencyInformation table
    for driver_id in driver_ids:
        contact_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        contact_number = f"{random.randint(100, 999)}{random.randint(1000000, 9999999)}"  # Generate a random phone number

        sql = f"""
        INSERT INTO EmergencyInformation (driverID, contanctName, contactNumber) 
        VALUES ({driver_id}, '{contact_name}', '{contact_number}');
        """
        cursor.execute(sql)
        logging.info(f"Inserted EmergencyInformation for driverID {i}: {contact_name}, {contact_number}")

    random.shuffle(driver_ids)
    # BankInformation table
    for driver_id in driver_ids:
        transit_no = random.randint(10000, 99999)
        branch_no = random.randint(100, 999)
        account_no = random.randint(100000000, 999999999)
        sql = f"INSERT INTO bankInformation (driverID, transitNo, branchNo, accountNo) VALUES ({driver_id}, {transit_no}, {branch_no}, {account_no});"
        cursor.execute(sql)
        logging.info(f"Inserted BankInformation for driverID {i}: Transit {transit_no}, Branch {branch_no}, Account {account_no}")


    random.shuffle(truck_ids)
    # TruckDamageReport table
    for truck_id in truck_ids: 
        damage_data_array = [
            "Engine Malfunction",
            "Brake Failure",
            "Tire Blowout",
            "Transmission Issue",
            "Oil Leak",
            "Electrical System Failure",
            "Windshield Crack",
            "Suspension Damage",
            "Fuel Tank Leak",
            "Exhaust System Damage"
        ]
        # Array of damage_description
        damage_description_array = [
            "Engine overheated during operation, causing significant loss of power.",
            "Brake pads worn out completely, leading to reduced stopping power.",
            "Severe tire blowout on the highway, requiring immediate replacement.",
            "Transmission fluid leaking, causing difficulties in gear shifting.",
            "Oil leaking from the engine block, potentially damaging internal components.",
            "Electrical wiring short-circuited, resulting in non-functional headlights.",
            "Large crack observed on the windshield, obstructing driver visibility.",
            "Suspension system damaged, causing unstable driving conditions.",
            "Fuel tank leaking diesel, posing a fire hazard and environmental risk.",
            "Exhaust pipe rusted and detached, increasing noise and emissions."
        ]

        # Randomly select data and description
        damage = random.choice(damage_data_array)
        description = random.choice(damage_description_array)
        
        sql = f"INSERT INTO TruckDamageReport (truckID, damageData, damageDescription) VALUES ({truck_id}, '{damage}', '{description}');"
        cursor.execute(sql)
        logging.info(f"Inserted TruckDamageReport for truckID {truck_id}: {description}")

    random.shuffle(customer_ids)
    # CustomerContactInfo table
    for customer_id in customer_ids:
        contact_person = f"Customer Contact {i}"
        contact_number = f"{random.randint(100, 999)}{random.randint(1000000, 9999999)}"
        sql = f"INSERT INTO CustomerContactInfo (customerID, contactPerson, contactNumber) VALUES ({customer_id}, '{contact_person}', '{contact_number}');"
        cursor.execute(sql)
        logging.info(f"Inserted CustomerContactInfo for customerID {customer_id}: {contact_person}, {contact_number}")

    random.shuffle(truck_ids)
    # Finance table
    finance_ids = []
    for truck_id in truck_ids:
        expense_types = ['Fuel', 'Maintenance', 'Insurance', 'Tires', 'Brakes']
        expense = random.choice(expense_types)
        amount = round(random.uniform(100, 2000), 2)
        payment_method = random.choice(['Credit Card', 'Cash', 'Bank Transfer'])
        payment_date = random_date(start_date, end_date).date()
        finance_ids.append(cursor.lastrowid)
        sql = f"INSERT INTO Finance (truckID, expense, totalAmount, paymentMethod, paymentDate) VALUES ({truck_id}, '{expense}', {amount}, '{payment_method}', '{payment_date}');"
        cursor.execute(sql)
        logging.info(f"Inserted Finance record for truckID {truck_id}: {expense}, {amount}, {payment_method}, {payment_date}")

    random.shuffle(finance_ids)
    # Tax table
    for entry_id in finance_ids:
        amount = round(random.uniform(100, 1000), 2)
        tax_rate = random.randint(5, 20)
        tax = round(amount * (tax_rate / 100), 2)

        sql = f"INSERT INTO Tax (entryID, amount, tax, taxRate) VALUES ({entry_id}, {amount}, {tax}, {tax_rate});"
        try:
            cursor.execute(sql)
            logging.info(f"Inserted Tax record for entryID {entry_id}: Amount {amount}, Tax {tax}, Rate {tax_rate}%")
        except Exception as e:
            logging.error(f"Failed to insert Tax record for entryID {entry_id}: {e}")


    invoice_ids = []
    for i, (supplier_id, shipment_id) in enumerate(zip(supplier_ids, shipment_ids), start=1): 
        invoice_number = f"INV-{i:06}"  # Generate invoice number
        invoice_date = random_date(start_date, end_date).date()
        payment_date = random_date(datetime.combine(invoice_date, datetime.min.time()), end_date).date()

        try:
            # Insert into Invoice
            sql = f"""
            INSERT INTO Invoice (supplierID, shipmentID, invoiceNumber, invoiceDate, paymentDate) 
            VALUES ({supplier_id}, {shipment_id}, '{invoice_number}', '{invoice_date}', '{payment_date}');
            """
            cursor.execute(sql)
            connection.commit()  # Commit each transaction
            invoice_ids.append(cursor.lastrowid)  # Store the inserted invoice ID
            logging.info(f"Inserted Invoice for supplierID {supplier_id}: {invoice_number}, Invoice Date: {invoice_date}, Payment Date: {payment_date}")
        except Exception as e:
            logging.error(f"Failed to insert Invoice for supplierID {supplier_id} and shipmentID {shipment_id}: {e}")

    random.shuffle(invoice_ids)
    # InvoiceTax table
    currencies = ['USD', 'EUR', 'GBP', 'CAD']
    payment_terms = ['NET30', 'NET60', 'DUE_ON_RECEIPT', 'PREPAID']
    for invoice_id in invoice_ids:
        total_amount = round(random.uniform(500, 5000), 2)
        tax_rate = random.randint(5, 20)
        taxed_amount = round(total_amount * (tax_rate / 100), 2)
        currency = random.choice(currencies)
        payment_term = random.choice(payment_terms)

        try:
            # Insert into InvoiceTax
            sql = f"""
            INSERT INTO InvoiceTax (invoiceID, totalAmount, taxedAmount, currency, paymentTerms) 
            VALUES ({invoice_id}, {total_amount}, {taxed_amount}, '{currency}', '{payment_term}');
            """
            cursor.execute(sql)
            connection.commit()  # Commit each transaction
            logging.info(f"Inserted InvoiceTax for invoiceID {invoice_id}: Total {total_amount}, Taxed {taxed_amount}")
        except Exception as e:
            logging.error(f"Failed to insert InvoiceTax for invoiceID {invoice_id}: {e}")


    # TrailerDamageReport table
    for trailer_id in trailer_ids: 
        # Array of damage_data
        damage_data_array = [
            "Physical Damage - Dent",
            "Structural Damage - Rust",
            "Tire Damage",
            "Door Malfunction",
            "Paint Damage - Scratches",
            "Refrigeration Unit Failure",
            "Electrical Wiring Issue",
            "Broken Component - Axle",
            "Load Area Damage",
            "Safety Violation - Missing Reflectors"
        ]
        # Array of damage_description
        damage_description_array = [
            "Significant dent observed on the left side of the trailer, approximately 3 feet long.",
            "Extensive rust found on the trailers undercarriage, weakening the structural integrity.",
            "One tire is completely flat, and others show visible cracks on the treads.",
            "Rear trailer door does not close properly due to bent hinges, causing potential safety risks.",
            "Deep scratches observed on the right side, with paint chipped off in several places.",
            "Refrigeration unit non-functional, causing inability to maintain required temperature for perishable goods.",
            "Trailers lighting system is malfunctioning, with several rear lights not operational.",
            "Visible crack on the trailers rear axle, requiring immediate replacement.",
            "Wooden floor inside the trailer has large cracks and broken planks, affecting cargo stability.",
            "Several reflectors on the trailers rear and sides are missing, making it unsafe for nighttime driving."
        ]

        # Randomly select data and description
        damage = random.choice(damage_data_array)
        description = random.choice(damage_description_array)

        sql = f"INSERT INTO TrailerDamageReport (trailerID, damageData, damageDescription) VALUES ({trailer_id}, '{damage}', '{description}');"
        cursor.execute(sql)
        logging.info(f"Inserted TrailerDamageReport for trailerID {trailer_id}: {description}")

    # SupplierContract table
    product_types = [
    'Electronics', 'Furniture', 'Clothing', 'Automotive Parts', 'Food Products',
    'Pharmaceuticals', 'Building Materials', 'Office Supplies', 'Appliances', 'Toys',
    'Sporting Goods', 'Cosmetics', 'Cleaning Supplies', 'Gardening Tools', 'Pet Supplies',
    'Books', 'Stationery', 'Beverages', 'Kitchenware', 'Hardware Tools'
]
    for supplier_id in supplier_ids:
        contract_start = random_date(start_date, end_date)  # Both start_date and end_date are datetime objects
        contract_end = random_date(contract_start, end_date)  # Ensure contract_end is after contract_start
        product_type = random.choice(product_types)

        sql = f"""
        INSERT INTO SupplierContract (supplierID, contractStart, contractEnd, productType) 
        VALUES ({supplier_id}, '{contract_start}', '{contract_end}', '{product_type}');
        """
        cursor.execute(sql)
        logging.info(f"Inserted SupplierContract for supplierID {supplier_id}: {product_type}, Start: {contract_start}, End: {contract_end}")

    # SupplierContactInfo table
    phone_number_length = 10  # Standard phone number length
    for supplier_id in supplier_ids:
        contact_person = f"{random.choice(first_names)} {random.choice(last_names)}"
        contact_number = ''.join([str(random.randint(0, 9)) for _ in range(phone_number_length)])  # Generate a random 10-digit number

        sql = f"""
        INSERT INTO SupplierContactInfo (supplierID, contactPerson, contactNumber)
        VALUES ({supplier_id}, '{contact_person}', '{contact_number}');
        """
        try:
            cursor.execute(sql)
            logging.info(f"Inserted SupplierContactInfo for supplierID {supplier_id}: Contact Person: {contact_person}, Contact Number: {contact_number}")
            print(f"Inserted SupplierContactInfo for supplierID {supplier_id}: Contact Person: {contact_person}, Contact Number: {contact_number}")
        except Exception as e:
            logging.error(f"Failed to insert SupplierContactInfo for supplierID {supplier_id}: {e}")

    # Commit all transactions
    connection.commit()
    message = "Data population complete and committed to the database."
    print(message)
    logging.info(message)

except mysql.connector.Error as err:
    error_message = f"Database error: {err}"
    print(error_message)
    logging.error(error_message)

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        message = "MySQL connection closed"
        print(message)
        logging.info(message)
