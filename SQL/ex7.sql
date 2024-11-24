USE my_database;

-- 1 
CREATE VIEW ActiveDriversWithShipments AS
SELECT 
    Driver.driverName, 
    Driver.workingStatus, 
    Shipment.shipmentID, 
    Shipment.typeOfProduct, 
    Shipment.loadWeight
FROM Driver
JOIN Truck ON Driver.driverID = Truck.driverID
JOIN Trailer ON Truck.truckID = Trailer.truckID
JOIN Shipment ON Trailer.trailerID = Shipment.trailerID
WHERE Driver.workingStatus = 'ACTIVE';

SELECT * 
FROM ActiveDriversWithShipments
ORDER BY loadWeight DESC;

-- 2 
CREATE VIEW CustomerShipmentDetails AS
SELECT 
    Shipment.shipmentID, 
    Customer.customerName, 
    Shipment.typeOfProduct, 
    Shipment.loadWeight, 
    Shipment.deliveryType, 
    Supplier.supplierName
FROM Shipment
JOIN Customer ON Shipment.customerID = Customer.customerID
JOIN Supplier ON Shipment.supplierID = Supplier.supplierID;

SELECT * 
FROM CustomerShipmentDetails
WHERE deliveryType = 'Expedited'; 
