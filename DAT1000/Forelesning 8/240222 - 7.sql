USE Hobbyhuset;

SELECT VNr, Betegnelse, Pris
FROM vare
WHERE pris<(SELECT AVG(pris) FROM vare);

SELECT Vare1.VNr, Vare1.Betegnelse, Vare1.Katnr, Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris=
(
    SELECT MIN(Vare2.Pris)
    FROM Vare as Vare2
    WHERE Vare1.Katnr=Vare2.Katnr
);

DROP TABLE IF EXISTS BilligsteKategori 
CREATE VIEW BilligsteKategori AS(
    SELECT Vare1.VNr, Vare1.Betegnelse, Vare1.Katnr, Vare1.Pris
    FROM Vare AS Vare1
    WHERE Vare1.Pris=
    (
        SELECT MIN(Vare2.Pris)
        FROM Vare as Vare2
        WHERE Vare1.Katnr=Vare2.Katnr)
);

SELECT  *
FROM BilligsteKategori;