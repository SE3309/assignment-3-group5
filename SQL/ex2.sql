USE my_database;

-- Create Driver Table
CREATE TABLE Driver(
driverID				INT NOT NULL AUTO_INCREMENT,
licenseNumber			VARCHAR(15) NOT NULL UNIQUE, -- Ontario licenses are 15 characters
driverName				VARCHAR(75) NOT NULL,
homeAddress				VARCHAR(100) NOT NULL,
yearsOfExperience		INT,
numberOfDeliveries		INT,
email					VARCHAR(50) UNIQUE,
age						INT,
salary					DECIMAL (10,2), 
employmentDate			DATE,
workingStatus			ENUM ('ACTIVE','INACTIVE','ON LEAVE') DEFAULT 'ACTIVE',
truckOwnedorAssigned	ENUM ('OWNED','ASSIGNED') DEFAULT 'ASSIGNED',
PRIMARY KEY (driverID)
);

CREATE TABLE DriverPhone(
phoneID					INT NOT NULL AUTO_INCREMENT,
driverID				INT NOT NULL, 
phoneNumber				VARCHAR(10), 
phoneType				ENUM ('HOME', 'MOBILE') DEFAULT 'MOBILE',
PRIMARY KEY (phoneID),
FOREIGN KEY (driverID) REFERENCES Driver(driverID)
);

CREATE TABLE EmergencyInformation(
emergencyContactID		INT NOT NULL AUTO_INCREMENT,
driverID 				INT NOT NULL, 
contanctName			VARCHAR(75),
contactNumber			VARCHAR(10),
PRIMARY KEY (emergencyContactID),
FOREIGN KEY (driverID) REFERENCES Driver(driverID)
);

CREATE TABLE bankInformation(
accountID				INT NOT NULL AUTO_INCREMENT,
driverID				INT NOT NULL,
transitNo				INT NOT NULL,
branchNo				INT NOT NULL,
accountNo				INT NOT NULL,
PRIMARY KEY (accountID),
FOREIGN KEY (driverID) REFERENCES Driver(driverID)
);

-- Create Truck Table
CREATE TABLE Truck(
truckID					INT NOT NULL AUTO_INCREMENT,
driverID				INT NOT NULL,
mileage					INT,
licencePlateNumber		VARCHAR(10) UNIQUE,
VIN						VARCHAR(17) UNIQUE, -- VIN numbers are 17 characters
makeModelYear			VARCHAR(100),
maxTowWeight			DECIMAL,
insurancePolicyNo		INT,
registration			DATE,
PRIMARY KEY (truckID),
FOREIGN KEY (driverID) REFERENCES Driver(driverID)
);

CREATE TABLE TruckDamageReport(
damageReportID			INT NOT NULL AUTO_INCREMENT,
truckID					INT NOT NULL,
damageData				TEXT, 
damageDescription		TEXT,
PRIMARY KEY (damageReportID),
FOREIGN KEY (truckID) REFERENCES Truck(truckID)
);

-- Create Supplier Table
CREATE TABLE Supplier(
supplierID				INT NOT NULL AUTO_INCREMENT,
supplierName			VARCHAR(50) NOT NULL,
contactPerson			VARCHAR(75),
contactName				VARCHAR(75),
supplierLongitude		DECIMAL(11,8) NOT NULL,
supplierLatitude		DECIMAL(10,8) NOT NULL, 
supplierType			ENUM('MANUFACTURER', 'DISTRIBUTOR', 'WHOLESALER') NOT NULL,
businessHours			VARCHAR(50),
PRIMARY KEY (supplierID)
);

-- Create Trailer Table
CREATE TABLE Trailer(
trailerID				INT NOT NULL AUTO_INCREMENT,
supplierID				INT NOT NULL,
truckID					INT NOT NULL,
trailerCapacity			INT,
maxLoadWeight			INT,
trailerLength			DECIMAL(10,2),
trailerType 			ENUM('DRY FRIEGHT','REFRIGERATED DRY FREIGHT','TANK','FLATBED','AUTO HAULER') DEFAULT 'DRY FRIEGHT',
licensePlateNumber		VARCHAR(10) UNIQUE,
VIN						VARCHAR(17) UNIQUE,
makeModelYear			VARCHAR(100),
registration			DATE,
PRIMARY KEY (trailerID),
FOREIGN KEY (truckID) REFERENCES Truck(truckID),
FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
);

CREATE TABLE TrailerDamageReport(
damageReportID			INT NOT NULL AUTO_INCREMENT,
trailerID				INT NOT NULL,
damageData				TEXT, -- NOT SURE!!
damageDescription		TEXT,
PRIMARY KEY (damageReportID),
FOREIGN KEY (trailerID) REFERENCES Trailer(trailerID)
);

CREATE TABLE SupplierContract(
contractID				INT NOT NULL AUTO_INCREMENT,
supplierID				INT NOT NULL,
contractStart			DATE NOT NULL,
contractEnd				DATE NOT NULL,
productType				VARCHAR(50),
PRIMARY KEY (contractID),
FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
);

CREATE TABLE SupplierContactInfo(
supplierContactInfoID	INT NOT NULL AUTO_INCREMENT,
supplierID				INT NOT NULL,
contactPerson			VARCHAR(75),
contactNumber			VARCHAR(10),
PRIMARY KEY (supplierContactInfoID),
FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
);

-- Create Customer Table
CREATE TABLE Customer(
customerID				INT NOT NULL AUTO_INCREMENT,
customerLongitude		DECIMAL(11,8) NOT NULL,
customerLatitude		DECIMAL(10,8) NOT NULL,
customerName			VARCHAR(50) NOT NULL,
typeOfStore				ENUM ('CHAIN','INDIVIDUAL') NOT NULL,
deliveryInstructions	TEXT,
PRIMARY KEY (customerID)
);

CREATE TABLE CustomerContactInfo(
customerContactInfoID	INT NOT NULL AUTO_INCREMENT,
customerID				INT NOT NULL,
contactPerson			VARCHAR(75),
contactNumber			VARCHAR(10),
PRIMARY KEY (customerContactInfoID),
FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

-- Create Shipment Table
CREATE TABLE Shipment(
shipmentID				INT NOT NULL AUTO_INCREMENT,
supplierID				INT NOT NULL,
customerID				INT NOT NULL,
trailerID				INT NOT NULL,
loadWeight				INT,
typeOfProduct			VARCHAR(50),
deliveryType			ENUM ('EXPEDITED', 'STANDARD', 'PRIORITY') DEFAULT 'STANDARD',
PRIMARY KEY (shipmentID),
FOREIGN KEY (customerID) REFERENCES Customer(customerID),
FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID),
FOREIGN KEY (trailerID) REFERENCES Trailer(trailerID)
);

-- Create Routes Table
CREATE TABLE Route(
routeID					INT NOT NULL AUTO_INCREMENT,
driverID				INT NOT NULL,
shipmentID				INT NOT NULL,
truckID					INT NOT NULL,
trailerID				INT NOT NULL,
pickupLongitude			DECIMAL(11,8) NOT NULL,
pickupLattitude			DECIMAL(10,8) NOT NULL,
pickupTime				DATETIME,
PRIMARY KEY (routeID),
FOREIGN KEY (driverID) REFERENCES Driver(driverID),
FOREIGN KEY (truckID) REFERENCES Truck(truckID),
FOREIGN KEY (trailerID) REFERENCES Trailer(trailerID),
FOREIGN KEY (shipmentID) REFERENCES Shipment(shipmentID)
);

CREATE TABLE ProofOfDelivery(
podID					INT NOT NULL AUTO_INCREMENT,
routeID					INT NOT NULL,
proofOfDelivery			BOOLEAN DEFAULT FALSE,
PODNo					VARCHAR(20),
PRIMARY KEY (podID),
FOREIGN KEY (routeID) REFERENCES Route(routeID)
);

-- Create Trips Table
CREATE TABLE Trips(
tripID					INT NOT NULL AUTO_INCREMENT,
routeID					INT NOT NULL,
destinationLongitude	DECIMAL(11,8) NOT NULL,
destinationLatitude		DECIMAL(10,8) NOT NULL,
tripIndex				INT NOT NULL,
PRIMARY KEY (tripID),
FOREIGN KEY (routeID) REFERENCES Route(routeID)
);

-- Create Finance Table
CREATE TABLE Finance(
entryID					INT NOT NULL AUTO_INCREMENT,
truckID					INT NOT NULL,
expense					VARCHAR(100),
totalAmount				DECIMAL(10,2) NOT NULL,
paymentMethod			VARCHAR(50),
paymentDate				DATE,
PRIMARY KEY (entryID),
FOREIGN KEY (truckID) REFERENCES Truck(truckID)
);

CREATE TABLE Tax(
taxID					INT NOT NULL AUTO_INCREMENT,
entryID					INT NOT NULL,
amount					DECIMAL(10,2) NOT NULL,
tax						DECIMAL(10,2) NOT NULL,
taxRate					INT NOT NULL,
PRIMARY KEY (taxID),
FOREIGN KEY (entryID) REFERENCES Finance(entryID)
);

-- Create Invoice Table
CREATE TABLE Invoice(
invoiceID				INT NOT NULL AUTO_INCREMENT,
supplierID				INT NOT NULL,
shipmentID				INT NOT NULL,
invoiceNumber			VARCHAR(25) NOT NULL,
invoiceDate				DATE NOT NULL,
paymentDate				DATE,
PRIMARY KEY (invoiceID),
FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID),
FOREIGN KEY (shipmentID) REFERENCES Shipment(shipmentID)
);

CREATE TABLE InvoiceTax(
invoiceTaxID			INT NOT NULL AUTO_INCREMENT,
invoiceID				INT NOT NULL,
totalAmount				DECIMAL(10, 2) NOT NULL,
taxedAmount				DECIMAL(10, 2) NOT NULL,
currency				VARCHAR(5) NOT NULL,
paymentTerms			VARCHAR(20),
PRIMARY KEY (invoiceTaxID),
FOREIGN KEY (invoiceID) REFERENCES Invoice(invoiceID)
);