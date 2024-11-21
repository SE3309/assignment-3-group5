import random
from datetime import datetime, timedelta


#   Trucks (100s)
#   Drivers (100s)
#   trips (1000s)
#   Supplier (10s - low 100s)
#   Deliveries (1000s)
#   Customer (1000s)
#   Payments/costs (mid-high 100s)


# Helper function for random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Define date ranges
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 1, 1)

# Open a file to write SQL INSERT statements
with open("populate_tables.sql", "w") as f:
    # Driver table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Driver (licenseNumber, driverName, homeAddress, yearsOfExperience, numberOfDeliveries, email, age, salary, employmentDate, workingStatus, truckOwnedorAssigned)
        VALUES ('ON{i:010}', 'Driver {i}', 'Address {i}', {random.randint(1, 20)}, {random.randint(1, 1000)}, 'driver{i}@example.com', {random.randint(25, 60)}, {random.uniform(40000, 80000):.2f}, '{random_date(start_date, end_date).date()}', 'ACTIVE', 'ASSIGNED');
        """
        f.write(sql)

    # DriverPhone table
    for i in range(1, 101):
        sql = f"INSERT INTO DriverPhone (driverID, phoneNumber, phoneType) VALUES ({i}, '416555{random.randint(1000, 9999)}', 'MOBILE');\n"
        f.write(sql)

    # EmergencyInformation table
    for i in range(1, 101):
        sql = f"INSERT INTO EmergencyInformation (driverID, contanctName, contactNumber) VALUES ({i}, 'Emergency Contact {i}', '416555{random.randint(1000, 9999)}');\n"
        f.write(sql)

    # bankInformation table
    for i in range(1, 101):
        sql = f"INSERT INTO bankInformation (driverID, transitNo, branchNo, accountNo) VALUES ({i}, {random.randint(10000, 99999)}, {random.randint(100, 999)}, {random.randint(100000000, 999999999)});\n"
        f.write(sql)

    # Truck table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Truck (driverID, mileage, licencePlateNumber, VIN, makeModelYear, maxTowWeight, insurancePolicyNo, registration)
        VALUES ({i}, {random.randint(50000, 300000)}, 'TRK{i:04}', '1HGCM82633A{random.randint(100000, 999999)}', 'MakeModelYear {random.randint(2010, 2023)}', {random.uniform(5000, 15000):.2f}, {random.uniform(100000, 500000):.2f}, '{random_date(start_date, end_date).date()}');
        """
        f.write(sql)

    # TruckDamageReport table
    for i in range(1, 101):
        sql = f"INSERT INTO TruckDamageReport (truckID, damageData, damageDescription) VALUES ({i}, 'Damage {i}', 'Description {i}');\n"
        f.write(sql)

    # Supplier table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Supplier (supplierName, contactPerson, contactName, supplierLongitude, supplierLatitude, supplierType, businessHours)
        VALUES ('Supplier {i}', 'Contact {i}', 'Name {i}', {random.uniform(-180, 180):.6f}, {random.uniform(-90, 90):.6f}, 'manufacturer', '9am-5pm');
        """
        f.write(sql)

    # Trailer table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Trailer (supplierID, truckID, trailerCapacity, maxLoadWeight, trailerLength, trailerType, licensePlateNumber, VIN, makeModelYear, registration)
        VALUES ({i}, {i}, {random.randint(500, 3000)}, {random.randint(1000, 8000)}, {random.uniform(5.0, 20.0):.2f}, 'DRY FRIEGHT', 'TRL{i:04}', 'VIN{i:08}', 'Model {i}', '{random_date(start_date, end_date).date()}');
        """
        f.write(sql)

    # TrailerDamageReport table
    for i in range(1, 101):
        sql = f"INSERT INTO TrailerDamageReport (trailerID, damageData, damageDescription) VALUES ({i}, 'Damage {i}', 'Description {i}');\n"
        f.write(sql)

    # SupplierContract table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO SupplierContract (supplierID, contractStart, contractEnd, productType)
        VALUES ({i}, '{random_date(start_date, end_date).date()}', '{random_date(start_date, end_date).date()}', 'Product {i}');
        """
        f.write(sql)

    # Customer table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Customer (customerLongitude, customerLatitude, customerName, typeOfStore, deliveryInstructions)
        VALUES ({random.uniform(-180, 180):.6f}, {random.uniform(-90, 90):.6f}, 'Customer {i}', 'CHAIN', 'Instructions {i}');
        """
        f.write(sql)

    # CustomerContactInfo table
    for i in range(1, 101):
        sql = f"INSERT INTO CustomerContactInfo (customerID, contactPerson, contactNumber) VALUES ({i}, 'Contact {i}', '416555{random.randint(1000, 9999)}');\n"
        f.write(sql)

    # Shipment table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Shipment (supplierID, customerID, trailerID, loadWeight, typeOfProduct, deliveryType)
        VALUES ({i}, {i}, {i}, {random.randint(500, 3000)}, 'ProductType {i}', 'DeliveryType {i}');
        """
        f.write(sql)

    # Route table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Route (driverID, shipmentID, truckID, trailerID, pickupLongitude, pickupLattitude, pickupTime)
        VALUES ({i}, {i}, {i}, {i}, {random.uniform(-180, 180):.6f}, {random.uniform(-90, 90):.6f}, '{random_date(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S")}');
        """
        f.write(sql)

    # ProofOfDelivery table
    for i in range(1, 101):
        sql = f"INSERT INTO ProofOfDelivery (routeID, proofOfDelivery, PODNo) VALUES ({i}, {random.choice([0, 1])}, 'POD{i:04}');\n"
        f.write(sql)

    # Trips table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Trips (routeID, destinationLongitude, destinationLatitude, tripIndex)
        VALUES ({i}, {random.uniform(-180, 180):.6f}, {random.uniform(-90, 90):.6f}, {random.randint(1, 5)});
        """
        f.write(sql)

    # Finance table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Finance (truckID, expense, totalAmount, paymentMethod, paymentDate)
        VALUES ({i}, 'Expense {i}', {random.uniform(100, 1000):.2f}, 'Method {i}', '{random_date(start_date, end_date).date()}');
        """
        f.write(sql)

    # Tax table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Tax (entryID, amount, tax, taxRate)
        VALUES ({i}, {random.uniform(100, 1000):.2f}, {random.uniform(10, 50):.2f}, {random.randint(5, 20)});
        """
        f.write(sql)

    # Invoice table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO Invoice (supplierID, shipmentID, invoiceNumber, invoiceDate, paymentDate)
        VALUES ({i}, {i}, 'INV-{i:03}', '{random_date(start_date, end_date).date()}', '{random_date(start_date, end_date).date()}');
        """
        f.write(sql)

    # InvoiceTax table
    for i in range(1, 101):
        sql = f"""
        INSERT INTO InvoiceTax (invoiceID, totalAmount, taxedAmount, currency, paymentTerms)
        VALUES ({i}, {random.uniform(100, 500):.2f}, {random.uniform(50, 300):.2f}, 'CAD', 'NET30');
        """
        f.write(sql)

print("populate_tables.sql has been generated.")
