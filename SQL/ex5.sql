-- 5.1: SELECT-FROM-WHERE (Sub queries)
SELECT d.driverID, d.driverName, (SELECT COUNT(r.routeID)
								  FROM Route r 
								  WHERE r.driverID = d.driverID) AS totalDeliveries
FROM Driver d
WHERE d.workingStatus = 'ACTIVE'
  AND (SELECT COUNT(r.routeID)
       FROM Route r 
       WHERE r.driverID = d.driverID) > 1;
       
-- 5.2: SELECT-FROM-WHERE (Three table Join & ORDER BY)
SELECT t.truckID,t.licencePlateNumber, d.driverID, d.driverName, f.expense, f.totalAmount
FROM Truck t, Driver d, Finance f
WHERE t.driverID=d.driverID
	AND t.truckID=f.truckID
ORDER BY f.truckID,f.totalAmount; -- first orders by truckID and then orders by total amount

-- 5.3: SELECT-FROM-WHERE (LEFT JOIN and GROUP BY)
SELECT t.truckID, t.licencePlateNumber, d.driverID, d.driverName
FROM Driver d LEFT JOIN Truck t ON t.driverID = d.driverID
			  LEFT JOIN Route r ON r.truckID = t.truckID
WHERE d.workingStatus = 'ACTIVE'
GROUP BY d.driverID, t.truckID, t.licencePlateNumber, d.driverName;

-- 5.4: SELECT-FROM-WHERE (UNION AND ORDER BY)
(SELECT truckID AS ID, damageData, damageDescription, 'Truck' AS VehicleType 
FROM TruckDamageReport
WHERE damageDescription IS NOT NULL)
UNION ALL
(SELECT trailerID AS ID, damageData, damageDescription, 'Trailer' AS VehicleType  
FROM TrailerDamageReport
WHERE damageDescription IS NOT NULL
ORDER BY ID, damageData);

-- 5.5: SELECT-FROM-WHERE (COUNT & SUM)
SELECT
    S.typeOfProduct, 
    COUNT(S.shipmentID) AS totalShipments, 
    SUM(S.loadWeight) AS totalLoadWeight
FROM Shipment S
JOIN Route R ON S.shipmentID = R.shipmentID
WHERE R.pickupTime BETWEEN '2000-01-01 00:00:00' AND '2024-01-31 23:59:59' -- set to a long range for timebeing (generally used for monthly tallying)
GROUP BY S.typeOfProduct
ORDER BY totalLoadWeight DESC;

-- 5.6: SELECT-FROM-WHERE (SELCT DISTINCT OR INTERSECT)
SELECT DISTINCT s.supplierName, t.trailerType, COUNT(t.trailerID) AS totalTrailers
FROM Supplier s, Trailer t
WHERE s.supplierID = t.supplierID
GROUP BY s.supplierName, t.trailerType;

-- 5.7: SELECT-FROM-WHERE (RANK FUNCTION FROM EXTERNAL SOURCE)
-- ranks active drivers based on number of deliveries in descending order
SELECT 
    driverName, 
    numberOfDeliveries, 
    RANK() OVER (ORDER BY numberOfDeliveries DESC) AS deliveryRank
FROM Driver
WHERE workingStatus = 'ACTIVE';

-- 5.8: SELECT-FROM-WHERE (NOT EXISTS)
-- get all drivers who do not have their banking information registered with the organization
SELECT d.driverID, d.driverName, dp.phoneNumber, d.salary
FROM Driver d
LEFT JOIN DriverPhone dp ON d.driverID = dp.driverID
WHERE NOT EXISTS (
        SELECT * 
        FROM bankInformation b 
        WHERE b.driverID = d.driverID);