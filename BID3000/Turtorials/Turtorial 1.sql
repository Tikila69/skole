CREATE DATABASE coffeemerchent_dw;

USE coffeemerchent_dw;

DROP TABLE IF EXISTS dim_time;

CREATE TABLE dim_time (
	date_sk INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    dato DATE,
    monthname VARCHAR(9),
    monthno INT(2),
    quarter INT(1),
    year INT(4)
    );

DROP procedure if exists pre_fill_timedimention;
DELIMITER //

DROP PROCEDURE IF EXISTS pre_fill_fimedimention;
create procedure pre_fill_timedimention(IN start_date DATE, in end_date DATE)
begin
	while start_date < end_date do
		insert into dim_time VALUES (
			NULL,
            start_date,
            monthname(start_date),
            month(start_date),
            quarter(start_date),
            year(start_date));
            SET start_date = ADDDATE(start_date,1);
	END WHILE;
END; //
DELIMITER ;

CALL pre_fill_timedimention("2005-01-01","2006-12-31");

SELECT *
FROM dim_time;

DROP TABLE IF EXISTS dim_inventory;

CREATE TABLE dim_inventory (
	inventory_sk INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    inventoryID INT,
    name VARCHAR(40) NOT NULL,
    price FLOAT(6,2),
    itemType VARCHAR(1),
    countryname VARCHAR(49)
    );
    
TRUNCATE TABLE dim_inventory;
INSERT INTO dim_inventory
SELECT 
	NULL,
	inventoryID,
	name,
	price,
	itemType,
	countryname
FROM coffeemerchent.inventory
LEFT JOIN coffeemerchent.countries
ON coffeemerchent.inventory.countryID = coffeemerchent.countries.countryID;

SELECT *
FROM dim_inventory;
    
DROP TABLE IF EXISTS dim_customers;
CREATE TABLE dim_customers (
	customer_sk INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customerID INT,
    firstName VARCHAR(30),
    lastName VARCHAR(30),
    street VARCHAR(50),
    zipcode VARCHAR(5),
    city VARCHAR(50),
    state VARCHAR(2)
    );

INSERT INTO dim_customers
SELECT
	NULL,
    consumerID,
    firstName,
    lastName,
    street,
    zipcode,
    city,
    state
FROM coffeemerchent.consumers;

SELECT *
FROM dim_customers;