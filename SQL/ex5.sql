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