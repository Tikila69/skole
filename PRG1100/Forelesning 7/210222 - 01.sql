USE heltnydatabase;

SELECT *
FROM vare;

DROP USER IF EXISTS "Lagersjefen2022"@"localhost";
CREATE USER "Lagersjefen2022"@"localhost" IDENTIFIED BY "Lagerpw";
GRANT SELECT ON Vare TO "Lagersjefen2022";
GRANT INSERT ON Vare TO "Lagersjefen2022";

