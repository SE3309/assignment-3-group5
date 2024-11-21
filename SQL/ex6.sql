-- USE THE BBELOE STATEMENT TO VERIFY SAFE MODE IS TURNED OFF
SET SQL_SAFE_UPDATES = 0;

-- 6.1: INSERT
-- increase pay by 5% for all drivers with more that 5 years of total experience
UPDATE Driver
SET salary = salary * 1.05
WHERE (yearsOfExperience + DATEDIFF(CURDATE(),employmentDate)/365) > 5; -- CURDATE() gives the curent time

-- USE prior and post updation to see salary hike
SELECT *
FROM Driver;

-- 6.2: DELETE
-- remove drivers who are not active and haven’t delivered anything for more that 2 years
DELETE 
-- SELECT *
FROM Driver d
WHERE workingStatus != 'ACTIVE'
AND NOT EXISTS (SELECT *
				FROM Route r
				JOIN Shipment s ON r.shipmentID=s.shipmentID
				WHERE r.driverID=d.driverID
				AND r.pickupTime>=DATE_SUB(CURDATE(), INTERVAL 2 YEAR))
AND DATEDIFF(CURDATE(),employmentDate)/365 > 2;

  
-- 6.3: DELETE
-- removes all records from the ProofOfDelivery, Trips, Invoice, Route, Shipment, and Trailer tables associated with trailers with maxLoadWeight less than 2500
DELETE ProofOfDelivery, Trips, Invoice, Route, Shipment, Trailer
FROM Trailer
LEFT JOIN Route ON Trailer.trailerID = Route.trailerID
LEFT JOIN ProofOfDelivery ON Route.routeID = ProofOfDelivery.routeID
LEFT JOIN Trips ON Route.routeID = Trips.routeID
LEFT JOIN Shipment ON Trailer.trailerID = Shipment.trailerID
LEFT JOIN Invoice ON Shipment.shipmentID = Invoice.shipmentID
WHERE Trailer.maxLoadWeight < 2500;


-- USE prior and post deletion to check for values
SELECT *
FROM ProofOfDelivery;

SELECT *
FROM Trips;

SELECT *
FROM Invoice;

SELECT *
FROM Route;

SELECT *
FROM Shipment;

SELECT *
FROM Trailer;