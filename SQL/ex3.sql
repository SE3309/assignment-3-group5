INSERT INTO Driver (licenseNumber, driverName, homeAddress, yearsOfExperience, numberOfDeliveries, email, age, salary, employmentDate, workingStatus, truckOwnedorAssigned)
VALUES
('ON1234567890123', 'John Doe', '123 Main St, Toronto, ON', 10, 200, 'johndoe@trucking.com', 35, 60000.00, '2015-06-01', 'ACTIVE', 'ASSIGNED'),
('ON9876543210987', 'Jane Smith', '456 Elm St, Ottawa, ON', 8, 180, 'janesmith@trucking.com', 29, 55000.00, '2017-09-15', 'ACTIVE', 'OWNNED'),
('ON4567890123456', 'Michael Brown', '789 Pine Rd, Kingston, ON', 15, 350, 'michaelbrown@trucking.com', 45, 75000.00, '2010-02-25', 'ACTIVE', 'ASSIGNED'),
('ON2345678901234', 'Emily Davis', '321 Oak Ln, Hamilton, ON', 12, 300, 'emilydavis@trucking.com', 38, 68000.00, '2012-08-10', 'ON LEAVE', 'ASSIGNED'),
('ON3456789012345', 'Chris Wilson', '555 Maple Ave, London, ON', 5, 120, 'chriswilson@trucking.com', 27, 52000.00, '2019-01-20', 'ACTIVE', 'OWNNED');

INSERT INTO Truck (truckID, driverID, mileage, licencePlateNumber, VIN, makeModelYear, maxTowWeight, insurancePolicyNo, registration) 
VALUES 
(1, 1, 150000, 'AB123CD', '1HGCM82633A123456', 'Freightliner Cascadia 2018', 20000, 1234567890, '2018-05-01'),
(2, 2, 175000, 'EF456GH', '2T1BU4EE8BC567890', 'Volvo VNL 2020', 22000, 987654321, '2020-07-15'),
(3, 3, 120000, 'IJ789KL', '3N1BC1CP5CK987654', 'Kenworth T680 2019', 19000, 564738291, '2019-03-20'),
(4, 4, 200000, 'MN012OP', '5UXWX7C59BA123789', 'Peterbilt 579 2016', 21000, 345678901, '2016-09-25'),
(5, 5, 185000, 'QR345ST', 'JN8AS58T78W098765', 'Mack Anthem 2017', 20000, 456789012, '2017-11-10');

INSERT INTO Supplier (supplierID, supplierName, contactPerson, contactName, supplierLongitude, supplierLatitude, supplierType, businessHours)
VALUES
(1, 'Supplier A', 'John Supplier', 'Supplier Contact 1', -79.3832, 43.6532, 'manufacturer', '9:00 AM - 6:00 PM'),
(2, 'Supplier B', 'Jane Supplier', 'Supplier Contact 2', -78.3991, 43.7632, 'distributor', '8:00 AM - 5:00 PM'),
(3, 'Supplier C', 'Michael Supplier', 'Supplier Contact 3', -77.3811, 44.7632, 'wholesaler', '10:00 AM - 7:00 PM'),
(4, 'Supplier D', 'Emily Supplier', 'Supplier Contact 4', -76.3031, 45.5632, 'manufacturer', '7:00 AM - 4:00 PM'),
(5, 'Supplier E', 'Chris Supplier', 'Supplier Contact 5', -75.2022, 46.2632, 'distributor', '6:00 AM - 3:00 PM');

INSERT INTO Trailer (supplierID, truckID, trailerCapacity, maxLoadWeight, trailerLength, trailerType, licensePlateNumber, VIN, makeModelYear, registration)
VALUES
(1, 1, 500, 10000, 40.5, 'DRY FRIEGHT', 'TR12345', '1G1JC5244R1234567', 'Utility 2020', '2020-03-01'),
(2, 2, 600, 12000, 45.0, 'REFRIGERATED DRY FREIGHT', 'TR67890', '1G6AS5340L5678901', 'Great Dane 2021', '2021-06-15'),
(3, 3, 700, 15000, 50.0, 'TANK', 'TR09876', '1FVACXDJ47HZ56789', 'Wabash 2019', '2019-12-20'),
(4, 4, 800, 18000, 55.0, 'FLATBED', 'TR54321', '1XP5D49X1XD456789', 'Fontaine 2018', '2018-05-30'),
(5, 5, 900, 20000, 60.0, 'AUTO HAULER', 'TR11223', '2WKPDDDJ4WN123456', 'Hyundai Translead 2022', '2022-09-01');

INSERT INTO Customer (customerLongitude, customerLatitude, customerName, typeOfStore, deliveryInstructions)
VALUES
(-79.3832, 43.6532, 'Customer 1', 'CHAIN', 'Leave at front desk.'),
(-78.3991, 43.7632, 'Customer 2', 'INDIVIDUAL', 'Deliver to back door.'),
(-77.3811, 44.7632, 'Customer 3', 'CHAIN', 'Leave with security.'),
(-76.3031, 45.5632, 'Customer 4', 'INDIVIDUAL', 'Deliver to front porch.'),
(-75.2022, 46.2632, 'Customer 5', 'CHAIN', 'Drop off at loading dock.');

INSERT INTO Shipment (supplierID, customerID, trailerID, loadWeight, typeOfProduct, deliveryType)
VALUES
(1, 1, 1, 8000, 'Electronics', 'Expedited'),
(2, 2, 2, 12000, 'Frozen Goods', 'Standard'),
(3, 3, 3, 7000, 'Chemicals', 'Expedited'),
(4, 4, 4, 10000, 'Lumber', 'Standard'),
(5, 5, 5, 15000, 'Vehicles', 'Priority');


INSERT INTO Route (driverID, shipmentID, truckID, trailerID, pickupLongitude, pickupLattitude, pickupTime)
VALUES
(1, 1, 1, 1, -79.4000, 43.7000, '2023-01-01 08:00:00'),
(2, 2, 2, 2, -78.3500, 43.7500, '2023-01-02 09:00:00'),
(3, 3, 3, 3, -77.3000, 44.7000, '2023-01-03 10:00:00'),
(4, 4, 4, 4, -76.2500, 45.6500, '2023-01-04 11:00:00'),
(5, 5, 5, 5, -75.2000, 46.6000, '2023-01-05 12:00:00');

INSERT INTO Trips (routeID, destinationLongitude, destinationLatitude, tripIndex)
VALUES
(1, -78.3832, 44.6532, 1),
(2, -77.3991, 45.7632, 2),
(3, -76.3811, 46.7632, 3),
(4, -75.3031, 47.5632, 4),
(5, -74.2022, 48.2632, 5);

INSERT INTO DriverPhone (driverID, phoneNumber, phoneType)
VALUES
(1, '4161234567', 'MOBILE'),
(2, '6139876543', 'HOME'),
(3, '5192345678', 'MOBILE'),
(4, '9053456789', 'MOBILE'),
(5, '7058765432', 'HOME');

INSERT INTO EmergencyInformation (driverID, contanctName, contactNumber)
VALUES
(1, 'Sarah Doe', '4167654321'),
(2, 'Paul Smith', '6138765432'),
(3, 'Anna Brown', '5196543210'),
(4, 'Linda Davis', '9054321098'),
(5, 'Mark Wilson', '7055678901');

INSERT INTO bankInformation (driverID, transitNo, branchNo, accountNo)
VALUES
(1, 123, 45678, 987654321),
(2, 124, 12345, 876543210),
(3, 125, 98765, 765432109),
(4, 126, 65432, 654321098),
(5, 127, 34567, 543210987);

INSERT INTO TruckDamageReport (truckID, damageData, damageDescription)
VALUES
(1, 'Minor scratches on left door.', 'Superficial scratches from a small collision.'),
(2, 'Broken rear bumper.', 'Severe impact damage from reversing into a pole.'),
(3, 'Worn-out tires.', 'Front tires need replacement.'),
(4, 'Cracked windshield.', 'Small crack on the lower right corner.'),
(5, 'Dented right side.', 'Collision with a parked car.');


INSERT INTO CustomerContactInfo (customerID, contactPerson, contactNumber)
VALUES
(1, 'Alice Johnson', '4165551234'),
(2, 'Bob Williams', '6135555678'),
(3, 'Carol Adams', '5195559876'),
(4, 'David Taylor', '9055554321'),
(5, 'Eve Martinez', '7055558765');


INSERT INTO ProofOfDelivery (routeID, proofOfDelivery, PODNo)
VALUES
(1, TRUE, 'POD123456'),
(2, TRUE, 'POD654321'),
(3, FALSE, 'POD789012'),
(4, TRUE, 'POD345678'),
(5, FALSE, 'POD987654');


INSERT INTO Finance (truckID, expense, totalAmount, paymentMethod, paymentDate)
VALUES
(1, 'Fuel', 500.00, 'Credit Card', '2023-01-01'),
(2, 'Maintenance', 1200.00, 'Cash', '2023-01-02'),
(3, 'Insurance', 1500.00, 'Bank Transfer', '2023-01-03'),
(4, 'Tires', 800.00, 'Credit Card', '2023-01-04'),
(5, 'Brakes', 600.00, 'Cash', '2023-01-05');

INSERT INTO Tax (entryID, amount, tax, taxRate)
VALUES
(1, 500.00, 65.00, 13),
(2, 1200.00, 156.00, 13),
(3, 1500.00, 195.00, 13),
(4, 800.00, 104.00, 13),
(5, 600.00, 78.00, 13);


INSERT INTO Invoice (supplierID, shipmentID, invoiceNumber, invoiceDate, paymentDate)
VALUES 
(1, 1, 'INV123456', '2023-01-01', '2023-01-10'),
(2, 2, 'INV654321', '2023-01-02', '2023-01-12'),
(3, 3, 'INV789012', '2023-01-03', '2023-01-13'),
(4, 4, 'INV345678', '2023-01-04', '2023-01-14'),
(5, 5, 'INV987654', '2023-01-05', '2023-01-15');


INSERT INTO InvoiceTax (invoiceID, totalAmount, taxedAmount, currency, paymentTerms)
VALUES
(1, 5000.00, 650.00, 'USD', 'Net30'),
(2, 12000.00, 1560.00, 'USD', 'Net15'),
(3, 15000.00, 1950.00, 'USD', 'Net30'),
(4, 8000.00, 1040.00, 'USD', 'Net15'),
(5, 6000.00, 780.00, 'USD', 'Net30');

INSERT INTO TrailerDamageReport (trailerID, damageData, damageDescription)
VALUES
(1, 'Broken door hinge.', 'The trailer door hinge is broken.'),
(2, 'Scratched side panels.', 'Scratches found on the left side panels.'),
(3, 'Flat tire.', 'One of the trailer tires is flat.'),
(4, 'Damaged roof.', 'Roof of the trailer has dents from hail.'),
(5, 'Corroded floor.', 'The trailer floor shows signs of corrosion.');


INSERT INTO SupplierContract (supplierID, contractStart, contractEnd, productType)
VALUES
(1, '2023-01-01', '2024-01-01', 'Electronics'),
(2, '2023-02-01', '2024-02-01', 'Frozen Goods'),
(3, '2023-03-01', '2024-03-01', 'Chemicals'),
(4, '2023-04-01', '2024-04-01', 'Lumber'),
(5, '2023-05-01', '2024-05-01', 'Vehicles');

INSERT INTO SupplierContactInfo (supplierID, contactPerson, contactNumber)
VALUES
(1, 'John Supplier Contact', '4165551234'),
(2, 'Jane Supplier Contact', '6135555678'),
(3, 'Michael Supplier Contact', '5195559876'),
(4, 'Emily Supplier Contact', '9055554321'),
(5, 'Chris Supplier Contact', '7055558765');

-- adds data (new tuples) to Route table for location and pickup time for Shipments for a specific supplier (here supplier 6)
INSERT INTO Route (driverID, shipmentID, truckID, trailerID, pickupLongitude, pickupLattitude, pickupTime)
SELECT d.driverID, s.shipmentID, t.truckID, tr.trailerID, sp.customerLongitude, sp.customerLatitude, '2024-11-19 10:00:00'
FROM Shipment s
JOIN Trailer tr ON s.trailerID = tr.trailerID
JOIN Truck t ON tr.truckID = t.truckID
JOIN Driver d ON t.driverID = d.driverID
JOIN Supplier sp ON s.supplierID = sp.supplierID
WHERE sp.supplierName = 'Supplier 6';

-- Adds taxed amount and tax rate as 13% for any non insurance expense as insurance is not taxed
INSERT INTO Tax (entryID, amount, tax, taxRate)
SELECT f.entryID, f.totalAmount, f.totalAmount * 0.13, 13
FROM Finance f
WHERE NOT EXISTS (
      SELECT f2.entryID
      FROM Finance f2
      WHERE f2.entryID = f.entryID 
        AND f2.expense = 'Insurance'
  );


