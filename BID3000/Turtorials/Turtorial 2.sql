USE coffeemerchent_dw;

DROP TABLE IF EXISTS fact_stage_order;
CREATE TABLE fact_stage_order (
	orderID INT,
    orderdate DATE,
    date_sk INT,
    consumerID INT,
    consumer_sk INT,
    employeeID INT,
    employee_SK INT,
    invertoryID INT,
	inventory_SK INT,
    quantity INT,
    price FLOAT(10,2),
    actual_price FLOAT(10,2),
    actual_sold FLOAT(10,2));



TRUNCATE fact_stage_order;

INSERT INTO fact_stage_order
SELECT
	o.orderID,
    o.orderdate,
    NULL,
    o.consumerID,
    NULL,
    o.employeeID,
    NULL,
    ol.inventoryID,
    NULL,
    ol.quantity,
    ol.price,
    ol.price - ol.price*ol.discount,
    (ol.price - ol.price*ol.discount)*ol.quantity
FROM coffeemerchent.orders o, coffeemerchent.orderlines ol
WHERE o.OrderID = ol.orderID;


SELECT *
FROM fact_stage_order;

UPDATE fact_stage_order, dim_time
SET fact_stage_order.date_sk = dim_time.date_sk
WHERE fact_stage_order.orderdate = dim_time.dato;

UPDATE fact_stage_order, dim_customers
SET fact_stage_order.consumer_sk = dim_customers.customer_sk
WHERE fact_stage_order.consumerID = dim_customers.customerID;

UPDATE fact_stage_order, dim_inventory
SET fact_stage_order.inventory_sk = dim_inventory.inventory_sk
WHERE fact_stage_order.invertoryID = dim_inventory.inventoryID;

SELECT *
FROM fact_stage_order;

DROP TABLE IF EXISTS dim_employee;

CREATE TABLE dim_employee (
	employee_sk INT NOT NULL auto_increment primary key,
	employeeID INT,
    firstName VARCHAR(30),
    lastName VARCHAR(30),
    workPhone VARCHAR(8),
    commissionRate FLOAT(4,4),
    horeDate DATE,
    birthDate DATE,
    gender VARCHAR(1)
    );

TRUNCATE TABLE dim_employee;
INSERT INTO dim_employee
SELECT 
	null,
	EmployeeID,
	FirstName,
	LastName,
	WorkPhone,
	CommissionRate,
    HireDate,
    BirthDate,
    Gender
FROM coffeemerchent.employees;

UPDATE fact_stage_order, dim_employee
SET fact_stage_order.employee_sk = dim_employee.employee_sk
WHERE fact_stage_order.employeeID = dim_employee.employeeID;

SELECT *
FROM fact_stage_order;