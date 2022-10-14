USE Ansattpersonal2022;

DROP SCHEMA IF EXISTS Ansattliste;

CREATE VIEW Ansattliste (Etternavn, Fornavn, Stilling, Avdeling) AS
	(Select Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
    FROM Ansatt, Stillingstype, Avdeling
    WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
    AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr);

SELECT *
FROM Ansattliste
ORDER BY Etternavn;

SELECT *
FROM Ansatt INNER JOIN Postkatalog;

SELECT *
FROM Ansatt JOIN Postkatalog;

SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Stillingstype JOIN
	(Ansatt JOIN Avdeling
		USING(Avdelingsnr))
	USING (Stillingskode);
    
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	USING(Stillingskode);

