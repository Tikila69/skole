USE ansattpersonal2022;

SELECT *
FROM stillingstype;

SELECT *
FROM Postkatalog;

SELECT *
FROM Postkatalog, Ansatt;

SELECT *
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt INNER JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;
    
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    
SELECT Etternavn, Fornavn, Stillingsbetegnelse
FROM Ansatt, Stillingstype
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode;

SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Stillingstype INNER JOIN
	(Ansatt INNER JOIN Avdeling
		ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr)
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Avdeling INNER JOIN
	(Ansatt INNER JOIN Stillingstype
		ON Ansatt.Stillingskode=Stillingstype.Stillingskode)
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;
    
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
FROM Stillingstype LEFT OUTER JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
SELECT *
FROM Ansatt RIGHT OUTER JOIN Stillingstype
	ON Ansatt.Stillingskode=Stillingstype.Stillingskode;
    
SELECT *
FROM Avdeling LEFT OUTER JOIN Ansatt 
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;

SELECT *
FROM Ansatt RIGHT OUTER JOIN Avdeling
	ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    
