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